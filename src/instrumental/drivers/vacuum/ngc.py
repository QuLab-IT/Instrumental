# -*- coding: utf-8 -*-
"""
Driver for NGC2D Pressure Gauge Controller.

The controller supports communication via RS232 serial interface at 9600 baud,
8 data bits, 1 stop bit, no parity, and no handshaking.
"""
from enum import Enum
import glob
import sys
from typing import Dict, List, Optional, Tuple, Union, Any
from serial import Serial, SerialException
from serial.tools.list_ports import comports
from abc import ABC, abstractmethod

from .. import Instrument, ParamSet
from ... import u

_INST_PARAMS = ['port']
_INST_CLASSES = ["NGC2", "NGC2D", "NGC2_D", "NGC3"]

def matches_arun_gauge(response: bytes) -> bool:
    """
    Check if the response from the NGC2D controller matches an Arun gauge.
    Byte fingerprint is given in NGC2D User Manual, Section State & Error byte coding.
    Args:
        response: bytes
            The response from the NGC2D controller

    Returns:
        bool
        True if the response matches an Arun gauge, False otherwise
    """
    if len(response) != 4:
        return False
    b1, b2 = response[0], response[1]
    return (
        (b1 & 0b00001111) == 0b0010 and  # bits 7–4 of byte 1
        (b1 & 0b00100000) != 0 and           # bit 6 of byte 1 is 1
        (b2 & 0b01000000) != 0 and           # bit 7 of byte 2 is 1
        (b2 & 0b00100000) == 0 and           # bit 5 of byte 2 is 0
        (b2 & 0b00010000) == 0               # bit 4 of byte 2 is 0
    )

def find_arun_gauge_ports(baudrate=9600, timeout=0.5):
    arun_ports = []
    for port in comports():
        try:
            with Serial(port.device, baudrate=baudrate, timeout=timeout) as ser:
                ser.write(Command.POLL.format().encode())
                response = ser.readline()
                if matches_arun_gauge(response):
                    arun_ports.append(port.device)
        except Exception as e:
            continue
    return arun_ports

def list_instruments() -> List[ParamSet]:
    """List all available NGC2D instruments.

    Returns
    -------
    list of ParamSet
        A list of parameter sets for each available instrument
    """
    ports = find_arun_gauge_ports()

    return [
        ParamSet(class_name, port=port) 
            for port in ports 
                for class_name in [
                    NGC2,
                    NGC2D,
                    NGC2_D,
                    NGC3,
                ]
    ]



class Command(Enum):
    """Commands supported by the NGC2D controller"""

    POLL: str = "P"
    CONTROL: str = "C"
    RELEASE: str = "R"
    RESET_ERROR: str = "E"
    GET_STATUS: str = "S"
    GAUGE_ON: str = "i"
    SELECT_ION_GAUGE: str = "j"
    GAUGE_OFF: str = "o"
    OVERRIDE_RELAY: str = "O"
    INHIBIT_RELAY: str = "I"
    BAKE: str = "b"

    def format(self, ignored_byte: str = "0", param: Optional[str] = None) -> str:
        """Format the command with ignored byte and optional parameter."""
        cmd = f"*{self.value}{ignored_byte}"
        if param is not None:
            cmd += param
        cmd += "\r\n"
        return cmd


class GaugeSelection(Enum):
    """Types of gauges supported by the NGC2D controller"""

    ION_GAUGE_1: str = "1"
    PIRANI_1: str = "2"
    PIRANI_2: str = "3"
    CAPACITANCE_MANOMETER: str = "4"
    ION_GAUGE_2: str = "5"

class IonGaugeSelection(Enum):
    """Gauges selected by the NGC2D controller"""

    IG1: str = "1"
    IG2: str = "2"


class GaugeType(Enum):
    """Types of gauges supported by the NGC2D controller"""

    ION_GAUGE: str = "I"
    PIRANI: str = "P"
    CAPACITANCE_MANOMETER: str = "M"


class PressureUnit(Enum):
    """Supported pressure units"""

    TORR: str = "T"
    PASCAL: str = "P"
    MBAR: str = "M"


class DeviceMode(Enum):
    """Modes of the NGC2D controller"""

    LOCAL: bool = False
    REMOTE: bool = True

class EmissionCurrent(Enum):
    """Emission current of the NGC2D controller"""

    mA0_5: str = "0"
    mA5: str = "1"

class BakeState(Enum):
    """Bake state of the NGC2D controller"""

    START: str = "1"
    STOP: str = "0"


class Relay(Enum):
    """Relays on the NGC2D controller"""

    A: str = "A"
    B: str = "B"
    C: str = "C"
    D: str = "D"


class OptionalFeature(Enum):
    """Feature flags for the NGC2D controller"""
    DUAL_ION_GAUGE = "dual_ion_gauge"
    BAKE = "bake"


class GaugeStatus:
    """Class representing the status of a gauge in the NGC2D controller."""


    def __init__(self, status_byte: int):
        """Initialize the gauge status from a status byte.

        Parameters
        ----------
        status_byte : int
            The status byte from the device
        """

    def __str__(self) -> str:
        return "GaugeStatus()"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the status to a dictionary."""
        pass


class IonGaugeStatus(GaugeStatus):
    """Class representing the status of a Ion gauge in the NGC2D controller."""

    in_emission: bool
    controlling_bakeout: bool
    in_degas: bool
    filament_2: bool

    def __init__(self, status_byte: int):
        """Initialize the gauge status from a status byte.

        Parameters
        ----------
        status_byte : int
            The status byte from the device
        """
        self.in_emission = bool(status_byte & 0x01)  # Bit 0
        self.controlling_bakeout = bool(status_byte & 0x04)  # Bit 2
        self.in_degas = bool(status_byte & 0x08)  # Bit 3
        self.filament_2 = bool(status_byte & 0x20)  # Bit 5


    def to_dict(self) -> Dict[str, Any]:
        """Convert the status to a dictionary."""
        return {
            "in_emission": self.in_emission,
            "controlling_bakeout": self.controlling_bakeout,
            "in_degas": self.in_degas,
            "filament_2": self.filament_2,
        }
    
    def __str__(self) -> str:
        return (
            "GaugeStatus("
            f"in_emission={self.in_emission}, "
            f"controlling_bakeout={self.controlling_bakeout}, "
            f"in_degas={self.in_degas}, "
            f"filament_2={self.filament_2})"
        )



class PiraniStatus(GaugeStatus):
    """Class representing the status of a Pirani gauge in the NGC2D controller."""

    operating: bool

    def __init__(self, status_byte: int):
        """Initialize the gauge status from a status byte.

        Parameters
        ----------
        status_byte : int
            The status byte from the device
        gauge_type : str
            The type of gauge ('I' for Ion, 'P' for Pirani, 'M' for Manometer)
        """
        self.operating = bool(status_byte & 0x01)  # Bit 0

    def __str__(self) -> str:
        return (
            "GaugeStatus("
            f"operating={self.operating})"
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert the status to a dictionary."""
        return {
            "operating": self.operating,
        }


class GaugeError:
    """Class representing the error state of a gauge in the NGC2D controller."""

    open_cicuit: bool
    overemission: bool
    underemission: bool
    overpressure: bool
    pirani_prevents_starting: bool
    filament_leads: bool

    def __init__(self, error_byte: int, gauge_type: GaugeType):
        """Initialize the gauge error from an error byte.

        Parameters
        ----------
        error_byte : int
            The error byte from the device
        gauge_type : str
            The type of gauge ('I' for Ion, 'P' for Pirani, 'M' for Manometer)
        """
        self.gauge_type = gauge_type

        match gauge_type:
            case GaugeType.ION_GAUGE:
                # Ion Gauge Error
                self.open_cicuit = bool(error_byte & 0x01)  # Bit 0
                self.overemission = bool(error_byte & 0x02)  # Bit 1
                self.underemission = bool(error_byte & 0x04)  # Bit 2
                self.overpressure = bool(error_byte & 0x08)  # Bit 3
                self.pirani_prevents_starting = bool(error_byte & 0x10)  # Bit 4 (always 0)
                self.filament_leads = bool(error_byte & 0x80)  # Bit 7 (always 0)

            case GaugeType.PIRANI:
                # Pirani Gauge Error
                self.open_cicuit = bool(error_byte & 0x01)  # Bit 0

            case GaugeType.CAPACITANCE_MANOMETER:
                # Manometer Error
                pass

    def __str__(self) -> str:
        match self.gauge_type:
            case GaugeType.ION_GAUGE:
                return (
                    f"GaugeError(type=Ion, open_cicuit={self.open_cicuit}, "
                    f"overemission={self.overemission}, "
                    f"underemission={self.underemission}, "
                    f"underemission={self.overpressure}, "
                    f"pirani_prevents_starting={self.pirani_prevents_starting}, "
                    f"filament_leads={self.filament_leads})"
                )
            case GaugeType.PIRANI:
                return (
                    "GaugeError(type=Pirani, "
                    f"open_cicuit={self.open_cicuit})"
                )
            case GaugeType.CAPACITANCE_MANOMETER:
                return (
                    "GaugeError(type=Manometer)"
                )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the error to a dictionary."""
        match self.gauge_type:
            case GaugeType.ION_GAUGE:
                return {
                    "open_cicuit": self.open_cicuit,
                    "overemission": self.overemission,
                    "underemission": self.underemission,
                    "underemission": self.overpressure,
                    "pirani_prevents_starting": self.pirani_prevents_starting,
                    "filament_leads": self.filament_leads,
                }
            case GaugeType.PIRANI:
                return {
                    "open_cicuit": self.open_cicuit,
                }
            case GaugeType.CAPACITANCE_MANOMETER:
                return {}


class Gauge:
    """Class representing a gauge in the NGC2D controller."""

    type: GaugeType
    number: GaugeSelection
    status: GaugeStatus
    error: GaugeError
    pressure: Optional[float]
    unit: PressureUnit
    def __init__(self, line: str):
        """Initialize the gauge from a status line.

        Parameters
        ----------
        line : str
            The gauge status line in format G<type><num><status><error><pressure>,<unit>
            Example: 'GP2A@  2E-02,M0'
        """
        self.type = GaugeType(line[1])  # P for Pirani, I for Ion, etc.
        self.number = GaugeSelection(line[2])  # Gauge number

        match self.type:
            case GaugeType.ION_GAUGE:
                self.status = IonGaugeStatus(ord(line[3]))
            case GaugeType.PIRANI:
                self.status = PiraniStatus(ord(line[3]))
            case GaugeType.CAPACITANCE_MANOMETER:
                self.status = GaugeStatus(ord(line[3]))

        self.error = GaugeError(ord(line[4]), self.type)
        pressure_str = line[5:].split(",")[0].strip()
        self.pressure = float(pressure_str) if pressure_str.strip() else None
        self.unit = PressureUnit(line[13])

    def __str__(self) -> str:
        return (
            f"Gauge(type={self.type.name}, "
            f"number={self.number.name}, "
            f"status={self.status}, "
            f"error={self.error}, "
            f"pressure={self.pressure}, "
            f"unit={self.unit.name})"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the gauge to a dictionary."""
        return {
            "type": self.type.name,
            "status": self.status.to_dict(),
            "error": self.error.to_dict(),
            "pressure": self.pressure,
            "unit": self.unit.name,
        }


class State:
    """Class representing the state of the NGC2D controller."""

    instrument_type: int
    mode: DeviceMode
    selected_gauge: IonGaugeSelection
    ig_connected: bool

    def __init__(self, state_byte: str):
        """Initialize the state from a state byte.

        Parameters
        ----------
        state_byte : str
            The state byte from the device
        """
        state_byte = ord(state_byte)
        self.instrument_type = state_byte & 0x0F  # Bits 3-0
        self.mode = DeviceMode(bool(state_byte & 0x10))  # Bit 4
        self.selected_gauge = IonGaugeSelection("2" if bool(state_byte & 0x40) else "1")  # Bit 6
        self.ig_connected = not bool(state_byte & 0x80)  # Bit 7

    def __str__(self) -> str:
        return (
            f"State(instrument_type={self.instrument_type}, "
            f"mode={self.mode.name}, "
            f"selected_gauge={self.selected_gauge.name}, "
            f"ig_connected={self.ig_connected})"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Union[int, str, bool]]:
        return {
            "instrument_type": self.instrument_type,
            "mode": self.mode.name,
            "selected_gauge": self.selected_gauge.name,
            "ig_connected": self.ig_connected,
        }


class Error:
    """Class representing the error state of the NGC2D controller."""

    gauge_error: bool
    over_temp_trip: bool
    temp_warning: bool

    def __init__(self, error_byte: str):
        """Initialize the error state from an error byte.

        Parameters
        ----------
        error_byte : str
            The error byte from the device
        """
        error_byte = ord(error_byte)
        self.gauge_error = bool(error_byte & 0x01)  # Bit 0
        self.over_temp_trip = bool(error_byte & 0x02)  # Bit 1
        self.temp_warning = bool(error_byte & 0x08)  # Bit 3

    def __str__(self) -> str:
        return (
            f"Error(gauge_error={self.gauge_error}, "
            f"over_temp_trip={self.over_temp_trip}, "
            f"temp_warning={self.temp_warning})"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, bool]:
        return {
            "gauge_error": self.gauge_error,
            "over_temp_trip": self.over_temp_trip,
            "temp_warning": self.temp_warning,
        }


class RelayStatus:
    """Class representing the status of the relays in the NGC2D controller."""

    A: bool
    B: bool
    C: bool
    D: bool

    def __init__(self, relay_status_byte: str):
        """Initialize the relay status from a relay status byte."""
        relay_status_byte = ord(relay_status_byte)
        self.A = bool(relay_status_byte & 0x01)  # Bit 0
        self.B = bool(relay_status_byte & 0x02)  # Bit 1
        self.C = bool(relay_status_byte & 0x04)  # Bit 2
        self.D = bool(relay_status_byte & 0x08)  # Bit 3

    def __str__(self) -> str:
        return f"RelayStatus(A={self.A}, B={self.B}, C={self.C}, D={self.D})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, bool]:
        return {
            "A": self.A,
            "B": self.B,
            "C": self.C,
            "D": self.D,
        }


class DeviceStatus:
    """Class representing the status of the NGC2D controller."""

    state: State
    error: Error
    relay_status: RelayStatus
    gauges: List[Gauge]

    def __init__(self, response_lines: List[str]):
        """Initialize the status from a status byte.

        Parameters
        ----------
        status_byte : int
            The status byte from the device
        """

        if len(response_lines) == 0:
            raise ValueError("No response received from device")

        self.state = State(response_lines[0][0])  # Bits 3-0
        self.error = Error(response_lines[0][1])  # Bit 4
        self.relay_status = RelayStatus(response_lines[0][2])  # Bit 4

        lines = [response_lines[0][4:]] + response_lines[1:]
        self.gauges = []
        if len(lines) > 0:
            self.gauges = [Gauge(line) for line in lines]

    def __str__(self) -> str:
        return (
            f"DeviceStatus(state={self.state}, "
            f"error={self.error}, "
            f"relay_status={self.relay_status}, "
            f"gauges={self.gauges})"
        )

    def to_dict(self) -> Dict[str, Union[int, str, bool]]:
        return {
            "state": self.state.to_dict(),
            "error": self.error.to_dict(),
            "relay_status": self.relay_status.to_dict(),
            "gauges": [gauge.to_dict() for gauge in self.gauges],
        }


class NGC(Instrument, ABC):
    """NGC Pressure Gauge Controller driver.

    This class provides an interface to control and read from the NGC pressure
    gauge controller. The controller supports multiple gauge types and pressure
    measurement units.

    This is an abstract base class and should not be instantiated directly.
    Use one of the specific model classes (NGC2, NGC2D, NGC2_D, or NGC3) instead.

    Parameters
    ----------
    port : str
        The serial port to connect to (e.g., 'COM1' or '/dev/ttyUSB0')
    """

    def __new__(cls, *args, **kwargs):
        if cls is NGC:
            raise TypeError("Cannot instantiate abstract class NGC directly. Use one of the specific model classes (NGC2, NGC2D, NGC2_D, or NGC3) instead.")
        return super().__new__(cls, *args, **kwargs)

    @abstractmethod
    def _initialize_features(self) -> None:
        """Initialize device-specific features.
        
        This method must be implemented by subclasses to set up model-specific features.
        """
        pass

    def _initialize(self) -> None:
        """Initialize the instrument connection"""
        self._remote_mode = False
        self._features: Dict[str, bool] = {
            OptionalFeature.DUAL_ION_GAUGE: False,
            OptionalFeature.BAKE: False,
        }
        self._ser = Serial(
            self._paramset["port"],
            baudrate=9600,
            bytesize=8,
            stopbits=1,
            parity="N",
            timeout=1.0,
        )
        self._initialize_features()

    def has_feature(self, feature: OptionalFeature) -> bool:
        """Check if the device has a specific feature"""
        return self._features.get(feature, False)

    def close(self) -> None:
        """Close the serial connection"""
        if self._remote_mode:
            self.release()
        self._ser.close()

    def _send_command(
        self,
        command: Command,
        ignored_byte: str = "0",
        param: Optional[str] = None,
    ) -> Optional[Tuple[State, Error, List[str]]]:
        """Send a command to the controller and read the response.

        Parameters
        ----------
        command : Command
            Command to send
        ignored_byte : str
            Ignored byte (for compatibility with PGC1)
        param : str, optional
            Additional command parameter

        Returns
        -------
        tuple
            (State, Error, [response_lines]) or None if no response
        """
        self._ser.write(command.format(ignored_byte, param).encode())
        
        response_lines: List[str] = []
        while True:
            line = self._ser.readline().decode().strip()
            if not line:
                break
            response_lines.append(line)

        return response_lines

    def poll(self) -> Tuple[State, Error]:
        """Poll the instrument for state and error information.

        Returns
        -------
        tuple
            (State, Error)
        """
        print("polling")
        response_lines = self._send_command(Command.POLL)
        if response_lines == []:
            raise ValueError("No response received from device")
        return State(response_lines[0][0]), Error(response_lines[0][1])

    def control(self) -> None:
        """Switch the instrument to remote control mode."""
        self._send_command(Command.CONTROL)  # Empty response is expected
        self._remote_mode = True

    def release(self) -> None:
        """Return the instrument to local control mode."""
        self._send_command(Command.RELEASE)  # Empty response is expected
        self._remote_mode = False

    def reset_error(self) -> None:
        """Reset all error flags."""
        response_lines = self._send_command(Command.RESET_ERROR)
        if response_lines == []:
            raise ValueError("No response received from device")

        error = Error(response_lines[0][1])

        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to reset errors")

    def get_status(self) -> DeviceStatus:
        """Request a report of operating status for all gauges.

        Returns
        -------
        dict
            Dictionary containing status information for each gauge
        """
        response_lines = self._send_command(Command.GET_STATUS)
        if response_lines == []:
            raise ValueError("No response received from device")

        return DeviceStatus(response_lines)

    def gauge_on(self, emission_current: EmissionCurrent = EmissionCurrent.mA0_5) -> None:
        """Switch on ion gauge emission.

        Parameters
        ----------
        emission_current : EmissionCurrent
            Emission current to set
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control gauge")

        if emission_current not in EmissionCurrent:
            raise ValueError("Emission current must be 'mA0_5' or 'mA5'")

        response_lines = self._send_command(Command.GAUGE_ON, param=emission_current.value,)
        if len(response_lines) > 1:
            error = Error(response_lines[0][1])
            if error.gauge_error or error.over_temp_trip or error.temp_warning:
                raise ValueError("Failed to switch on gauge")

    def gauge_off(self) -> None:
        """Switch off ion gauge."""
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control gauge")

        response_lines = self._send_command(Command.GAUGE_OFF)
        if len(response_lines) > 1:
            error = Error(response_lines[0][1])
            if error.gauge_error or error.over_temp_trip or error.temp_warning:
                raise ValueError("Failed to switch off gauge")

    def select_ion_gauge(self, gauge_num: IonGaugeSelection = IonGaugeSelection.IG1) -> None:
        """Select which ion gauge to use.

        Parameters
        ----------
        gauge_num : IonGaugeSelection
            'IG1' for Ion Gauge 1, 'IG2' for Ion Gauge 2
        """
        if not self.has_feature(OptionalFeature.DUAL_ION_GAUGE):
            raise NotImplementedError("This device doesn't support dual ion gauges")
        
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to select gauge")
        
        if gauge_num not in IonGaugeSelection:
            raise ValueError("Gauge number must be 'IG1' or 'IG2'")
        
        response_lines = self._send_command(Command.SELECT_ION_GAUGE, param=gauge_num.value)
        if response_lines == []:
            raise ValueError("No response received from device")

        error = Error(response_lines[1][1])
        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to select ion gauge")

    def override_relay(self, relay: Relay) -> None:
        """Permanently energize a relay.

        Parameters
        ----------
        relay : str
            Relay to energize ('A' to 'D')
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control relays")

        if relay not in Relay:
            raise ValueError("Relay must be 'A', 'B', 'C', or 'D'")

        response_lines = self._send_command(Command.OVERRIDE_RELAY, param=relay.value,)
        if response_lines == []:
            raise ValueError("No response received from device")

        error = Error(response_lines[0][1])
        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to override relay")

    def inhibit_relay(self, relay: Relay) -> None:
        """Permanently de-energize a relay.

        Parameters
        ----------
        relay : str
            Relay to de-energize ('A' to 'D')
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control relays")

        if relay not in Relay:
            raise ValueError("Relay must be 'A', 'B', 'C', or 'D'")

        response_lines = self._send_command(Command.INHIBIT_RELAY, param=relay.value)
        if response_lines == []:
            raise ValueError("No response received from device")

        error = Error(response_lines[0][1])
        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to inhibit relay")
        
    def bake(self, state: BakeState = BakeState.START) -> None:
        """Start or stop the bake cycle."""
        if not self.has_feature(OptionalFeature.BAKE):
            raise NotImplementedError("This device doesn't support bake")

        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control bake")

        self._send_command(Command.BAKE, param=state.value)


class NGC2(NGC):
    """NGC2 Pressure Gauge Controller driver.

    This class provides an interface to control and read from the NGC2 pressure
    gauge controller. The controller supports multiple gauge types and pressure
    measurement units.
    """
    _INST_CLASSES: List[str] = ["NGC2"]

    def _initialize(self) -> None:
        """Initialize the instrument connection"""
        super()._initialize()

    def _initialize_features(self) -> None:
        """NGC2 has no additional features"""
        pass


class NGC2D(NGC):
    """NGC2D Pressure Gauge Controller driver.

    This class provides an interface to control and read from the NGC2D pressure
    gauge controller. The controller supports multiple gauge types and pressure
    measurement units.
    """
    _INST_CLASSES: List[str] = ["NGC2D"]

    def _initialize(self) -> None:
        """Initialize the instrument connection"""
        super()._initialize()

    def _initialize_features(self) -> None:
        """NGC2D has dual ion gauge and bakeout features"""
        self._features.update({
            OptionalFeature.DUAL_ION_GAUGE: True,
            OptionalFeature.BAKE: True,
        })


class NGC2_D(NGC):
    """NGC2_D Pressure Gauge Controller driver.

    This class provides an interface to control and read from the NGC2D pressure
    gauge controller. The controller supports multiple gauge types and pressure
    measurement units.
    """
    _INST_CLASSES: List[str] = ["NGC2_D"]

    def _initialize(self) -> None:
        """Initialize the instrument connection"""
        super()._initialize()

    def _initialize_features(self) -> None:
        """NGC2D has dual ion gauge and bakeout features"""
        self._features.update({
            OptionalFeature.DUAL_ION_GAUGE: True,
        })

class NGC3(NGC):
    """NGC3 Pressure Gauge Controller driver.

    This class provides an interface to control and read from the NGC3 pressure
    gauge controller. The controller supports multiple gauge types and pressure
    measurement units.
    """
    _INST_CLASSES: List[str] = ["NGC3"]

    def _initialize(self) -> None:
        """Initialize the instrument connection"""
        super()._initialize()

    def _initialize_features(self) -> None:
        """NGC2D has dual ion gauge and bakeout features"""
        self._features.update({
            OptionalFeature.DUAL_ION_GAUGE: True,
            OptionalFeature.BAKE: True,
        })
