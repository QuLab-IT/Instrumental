# -*- coding: utf-8 -*-
"""
Driver for NGC2D Pressure Gauge Controller.

The controller supports communication via RS232 serial interface at 9600 baud,
8 data bits, 1 stop bit, no parity, and no handshaking.
"""
from enum import Enum, Flag, auto
import glob
import sys
from typing import Dict, List, Optional, Tuple, Union, Any
from serial import Serial, SerialException

from .. import Instrument, ParamSet
from ... import u

_INST_PRIORITY: int = 5
_INST_PARAMS: List[str] = ["port"]
_INST_CLASSES: List[str] = ["NGC2D"]


class GaugeSelection(Enum):
    """Types of gauges supported by the NGC2D controller"""

    ION_GAUGE_1: str = "1"
    PIRANI_1: str = "2"
    PIRANI_2: str = "3"
    CAPACITANCE_MANOMETER: str = "4"
    ION_GAUGE_2: str = "5"


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


class StateFlags(Flag):
    """Flags representing the state byte information"""

    IG1_SELECTED: int = 0  # Bit 6 = 0
    IG2_SELECTED: int = auto()  # Bit 6 = 1
    LOCAL_MODE: int = 0  # Bit 4 = 0
    REMOTE_MODE: int = auto()  # Bit 4 = 1
    IG_CONNECTED: int = 0  # Bit 7 = 0
    IG_DISCONNECTED: int = auto()  # Bit 7 = 1


class ErrorFlags(Flag):
    """Flags representing the error byte information"""

    GAUGE_ERROR: int = auto()  # Bit 0
    OVER_TEMP_TRIP: int = auto()  # Bit 1
    TEMP_WARNING: int = auto()  # Bit 3


class DeviceMode(Enum):
    """Modes of the NGC2D controller"""

    LOCAL: str = "local"
    REMOTE: str = "remote"

class SelectedGauge(Enum):
    """Gauges selected by the NGC2D controller"""

    IG1: str = "IG1"
    IG2: str = "IG2"


class GaugeStatus:
    """Class representing the status of a gauge in the NGC2D controller."""

    in_emission: bool
    controlling_bakeout: bool
    in_degas: bool
    filament_2: bool
    bit_6: bool
    operating: bool
    pirani_interlock: bool
    filament_leads: bool

    def __init__(self, status_byte: int, gauge_type: str):
        """Initialize the gauge status from a status byte.

        Parameters
        ----------
        status_byte : int
            The status byte from the device
        gauge_type : str
            The type of gauge ('I' for Ion, 'P' for Pirani, 'M' for Manometer)
        """
        self.gauge_type = gauge_type

        if gauge_type == "I":
            # Ion Gauge Status
            self.in_emission = bool(status_byte & 0x01)  # Bit 0
            self.controlling_bakeout = bool(status_byte & 0x04)  # Bit 2
            self.in_degas = bool(status_byte & 0x08)  # Bit 3
            self.filament_2 = bool(status_byte & 0x20)  # Bit 5
            self.bit_6 = bool(status_byte & 0x40)  # Bit 6 (always 1)
        elif gauge_type == "P":
            # Pirani Gauge Status
            self.operating = bool(status_byte & 0x01)  # Bit 0
            self.pirani_interlock = bool(status_byte & 0x10)  # Bit 4
            self.bit_6 = bool(status_byte & 0x40)  # Bit 6 (always 1)
            self.filament_leads = bool(status_byte & 0x80)  # Bit 7
        elif gauge_type == "M":
            # Manometer Status
            self.operating = bool(status_byte & 0x01)  # Bit 0
            self.bit_6 = bool(status_byte & 0x40)  # Bit 6 (always 1)

    def __str__(self) -> str:
        if self.gauge_type == "I":
            return (
                f"GaugeStatus(type=Ion, in_emission={self.in_emission}, "
                f"controlling_bakeout={self.controlling_bakeout}, "
                f"in_degas={self.in_degas}, filament_2={self.filament_2})"
            )
        elif self.gauge_type == "P":
            return (
                f"GaugeStatus(type=Pirani, operating={self.operating}, "
                f"pirani_interlock={self.pirani_interlock}, "
                f"filament_leads={self.filament_leads})"
            )
        else:  # M
            return f"GaugeStatus(type=Manometer, operating={self.operating})"

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the status to a dictionary."""
        if self.gauge_type == "I":
            return {
                "in_emission": self.in_emission,
                "controlling_bakeout": self.controlling_bakeout,
                "in_degas": self.in_degas,
                "filament_2": self.filament_2,
            }
        elif self.gauge_type == "P":
            return {
                "operating": self.operating,
                "pirani_interlock": self.pirani_interlock,
                "filament_leads": self.filament_leads,
            }
        else:  # M
            return {"operating": self.operating}


class GaugeError:
    """Class representing the error state of a gauge in the NGC2D controller."""

    filament_failure: bool
    emission_failure: bool
    over_pressure: bool
    over_temp: bool
    bit_4: bool
    bit_5: bool
    bit_6: bool
    bit_7: bool

    def __init__(self, error_byte: int, gauge_type: str):
        """Initialize the gauge error from an error byte.

        Parameters
        ----------
        error_byte : int
            The error byte from the device
        gauge_type : str
            The type of gauge ('I' for Ion, 'P' for Pirani, 'M' for Manometer)
        """
        self.gauge_type = gauge_type

        if gauge_type == "I":
            # Ion Gauge Error
            self.filament_failure = bool(error_byte & 0x01)  # Bit 0
            self.emission_failure = bool(error_byte & 0x02)  # Bit 1
            self.over_pressure = bool(error_byte & 0x04)  # Bit 2
            self.over_temp = bool(error_byte & 0x08)  # Bit 3
            self.bit_4 = bool(error_byte & 0x10)  # Bit 4 (always 0)
            self.bit_5 = bool(error_byte & 0x20)  # Bit 5 (always 0)
            self.bit_6 = bool(error_byte & 0x40)  # Bit 6 (always 0)
            self.bit_7 = bool(error_byte & 0x80)  # Bit 7 (always 0)
        elif gauge_type == "P":
            # Pirani Gauge Error
            self.over_pressure = bool(error_byte & 0x04)  # Bit 2
            self.over_temp = bool(error_byte & 0x08)  # Bit 3
            self.bit_4 = bool(error_byte & 0x10)  # Bit 4 (always 0)
            self.bit_5 = bool(error_byte & 0x20)  # Bit 5 (always 0)
            self.bit_6 = bool(error_byte & 0x40)  # Bit 6 (always 0)
            self.bit_7 = bool(error_byte & 0x80)  # Bit 7 (always 0)
        elif gauge_type == "M":
            # Manometer Error
            self.over_pressure = bool(error_byte & 0x04)  # Bit 2
            self.over_temp = bool(error_byte & 0x08)  # Bit 3
            self.bit_4 = bool(error_byte & 0x10)  # Bit 4 (always 0)
            self.bit_5 = bool(error_byte & 0x20)  # Bit 5 (always 0)
            self.bit_6 = bool(error_byte & 0x40)  # Bit 6 (always 0)
            self.bit_7 = bool(error_byte & 0x80)  # Bit 7 (always 0)

    def __str__(self) -> str:
        if self.gauge_type == "I":
            return (
                f"GaugeError(type=Ion, filament_failure={self.filament_failure}, "
                f"emission_failure={self.emission_failure}, "
                f"over_pressure={self.over_pressure}, "
                f"over_temp={self.over_temp})"
            )
        elif self.gauge_type == "P":
            return (
                f"GaugeError(type=Pirani, over_pressure={self.over_pressure}, "
                f"over_temp={self.over_temp})"
            )
        else:  # M
            return (
                f"GaugeError(type=Manometer, over_pressure={self.over_pressure}, "
                f"over_temp={self.over_temp})"
            )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the error to a dictionary."""
        if self.gauge_type == "I":
            return {
                "filament_failure": self.filament_failure,
                "emission_failure": self.emission_failure,
                "over_pressure": self.over_pressure,
                "over_temp": self.over_temp,
            }
        elif self.gauge_type == "P":
            return {"over_pressure": self.over_pressure, "over_temp": self.over_temp}
        else:  # M
            return {"over_pressure": self.over_pressure, "over_temp": self.over_temp}



class Gauge:
    """Class representing a gauge in the NGC2D controller."""

    type: str
    number: str
    status: GaugeStatus
    error: GaugeError
    pressure: Optional[float]

    def __init__(self, line: str):
        """Initialize the gauge from a status line.

        Parameters
        ----------
        line : str
            The gauge status line in format G<type><num><status><error><pressure>,<unit>
            Example: 'GP2A@  2E-02,M0'
        """
        self.type = line[1]  # P for Pirani, I for Ion, etc.
        self.number = line[2]  # Gauge number
        self.status = GaugeStatus(ord(line[3]), self.type)
        self.error = GaugeError(ord(line[4]), self.type)
        pressure_str = line[5:].split(",")[0].strip()
        self.pressure = float(pressure_str) if pressure_str.strip() else None

    def __str__(self) -> str:
        return (
            f"Gauge(type={self.type}, number={self.number}, "
            f"status={self.status}, error={self.error}, "
            f"pressure={self.pressure})"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Any]:
        """Convert the gauge to a dictionary."""
        return {
            "type": self.type,
            "status": self.status.to_dict(),
            "error": self.error.to_dict(),
            "pressure": self.pressure,
        }


class State:
    """Class representing the state of the NGC2D controller."""

    instrument_type: int
    mode: DeviceMode
    selected_gauge: SelectedGauge
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
        self.mode = DeviceMode(state_byte & 0x10)  # Bit 4
        self.selected_gauge = SelectedGauge(state_byte & 0x40)  # Bit 6
        self.ig_connected = not bool(state_byte & 0x80)  # Bit 7

    def __str__(self) -> str:
        return (
            f"State(instrument_type={self.instrument_type}, "
            f"mode={self.mode}, selected_gauge={self.selected_gauge}, "
            f"ig_connected={self.ig_connected})"
        )

    def __repr__(self) -> str:
        return self.__str__()

    def to_dict(self) -> Dict[str, Union[int, str, bool]]:
        return {
            "instrument_type": self.instrument_type,
            "mode": self.mode,
            "selected_gauge": self.selected_gauge,
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

class DeviceStatus:
    """Class representing the status of the NGC2D controller."""

    state: State
    error: Error
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
        
        lines = response_lines[0][2:] + response_lines[1:]
        self.gauges = []
        if len(lines) > 0:
            self.gauges = [Gauge(line) for line in lines]


    def __str__(self) -> str:
        return (
            f"DeviceStatus(instrument_type={self.instrument_type}, "
            f"mode={self.mode}, selected_gauge={self.selected_gauge}, "
            f"ig_connected={self.ig_connected})"
        )  
    
    def to_dict(self) -> Dict[str, Union[int, str, bool]]:
        return {
            "instrument_type": self.instrument_type,
            "mode": self.mode,
            "selected_gauge": self.selected_gauge,
            "ig_connected": self.ig_connected,
        }

def parse_state_byte(state_byte: int) -> Dict[str, Union[int, str, bool]]:
    """Parse the state byte into a dictionary of states.

    Parameters
    ----------
    state_byte : int
        The state byte from the device

    Returns
    -------
    dict
        Dictionary containing the parsed states
    """
    states: Dict[str, Union[int, str, bool]] = {}
    states["instrument_type"] = state_byte & 0x0F  # Bits 3-0
    states["mode"] = "remote" if state_byte & 0x10 else "local"  # Bit 4
    states["selected_gauge"] = "IG2" if state_byte & 0x40 else "IG1"  # Bit 6
    states["ig_connected"] = not bool(state_byte & 0x80)  # Bit 7
    return states


def parse_error_byte(error_byte: int) -> Dict[str, bool]:
    """Parse the error byte into a dictionary of errors.

    Parameters
    ----------
    error_byte : int
        The error byte from the device

    Returns
    -------
    dict
        Dictionary containing the parsed errors
    """
    errors: Dict[str, bool] = {}
    errors["gauge_error"] = bool(error_byte & 0x01)  # Bit 0
    errors["over_temp_trip"] = bool(error_byte & 0x02)  # Bit 1
    errors["temp_warning"] = bool(error_byte & 0x08)  # Bit 3
    return errors



class NGC2D(Instrument):
    """NGC2D Pressure Gauge Controller driver.

    This class provides an interface to control and read from the NGC2D pressure
    gauge controller. The controller supports multiple gauge types and pressure
    measurement units.

    Parameters
    ----------
    port : str
        The serial port to connect to (e.g., 'COM1' or '/dev/ttyUSB0')
    """

    def _initialize(self) -> None:
        """Initialize the instrument connection"""
        self._ser = Serial(
            self._paramset["port"],
            baudrate=9600,
            bytesize=8,
            stopbits=1,
            parity="N",
            timeout=1.0,
        )
        # Start in local mode
        self._remote_mode: bool = False

    def close(self) -> None:
        """Close the serial connection"""
        if self._remote_mode:
            self.release()
        self._ser.close()

    def _send_command(
        self,
        command_char: str,
        ignored_byte: str = "0",
        param: Optional[str] = None,
    ) -> Optional[Tuple[State, Error, List[str]]]:
        """Send a command to the controller and read the response.

        Parameters
        ----------
        command_char : str
            Single character command
        ignored_byte : str
            Ignored byte (for compatibility with PGC1)
        param : str, optional
            Additional command parameter

        Returns
        -------
        tuple
            (State, Error, [response_lines]) or None if no response
        """
        cmd = f"*{command_char}{ignored_byte}"
        if param is not None:
            cmd += param
        cmd += "\r\n"

        self._ser.write(cmd.encode())

        response_lines: List[str] = []
        while True:
            line = self._ser.readline().decode().strip()
            if not line:
                break
            response_lines.append(line)

        return response_lines

    @property
    def state(self) -> Optional[Dict[str, Union[int, str, bool]]]:
        """Get the current state of the device.

        Returns
        -------
        dict
            Dictionary containing the current state information
        """
        return self._state.copy() if hasattr(self, "_state") else None

    @property
    def error(self) -> Optional[Dict[str, bool]]:
        """Get the current error status.

        Returns
        -------
        dict
            Dictionary containing the current error information
        """
        return self._error.copy() if hasattr(self, "_error") else None

    def poll(self) -> Tuple[State, Error]:
        """Poll the instrument for state and error information.

        Returns
        -------
        tuple
            (State, Error)
        """
        response = self._send_command("P")
        if response == []:
            raise ValueError("No response received from device")
        return State(response[0]), Error(response[1])

    def control(self) -> None:
        """Switch the instrument to remote control mode."""
        self._send_command("C")  # Empty response is expected
        self._remote_mode = True

    def release(self) -> None:
        """Return the instrument to local control mode."""
        self._send_command("R")  # Empty response is expected
        self._remote_mode = False

    def reset_error(self) -> None:
        """Reset all error flags."""
        response_lines = self._send_command("E")
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
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to get status")

        response_lines = self._send_command("S")
        if response_lines == []:
            raise ValueError("No response received from device")

        return DeviceStatus(response_lines)


    def select_ion_gauge(self, gauge_num: str) -> None:
        """Select which ion gauge to use.

        Parameters
        ----------
        gauge_num : str
            '1' for Ion Gauge 1, '2' for Ion Gauge 2
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to select gauge")

        response_lines = self._send_command("j", param=gauge_num)
        if response_lines == []:
            raise ValueError("No response received from device")
        
        error = Error(response_lines[1][1])
        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to select ion gauge")

    def gauge_on(self, emission_current: str = "0") -> None:
        """Switch on ion gauge emission.

        Parameters
        ----------
        emission_current : str
            '0' for 0.5mA, '1' for 5mA
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control gauge")

        response_lines = self._send_command("i", param=emission_current)
        if response_lines == []:
            raise ValueError("No response received from device")
        
        error = Error(response_lines[1][1])
        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to switch on gauge")

    def gauge_off(self) -> None:
        """Switch off ion gauge."""
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control gauge")

        response_lines = self._send_command("o")
        if response_lines == []:
            raise ValueError("No response received from device")
        
        error = Error(response_lines[1][1])
        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to switch off gauge")

    def override_relay(self, relay: str) -> None:
        """Permanently energize a relay.

        Parameters
        ----------
        relay : str
            Relay to energize ('A' to 'D')
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control relays")

        if relay not in "ABCD":
            raise ValueError("Relay must be 'A', 'B', 'C', or 'D'")

        response_lines = self._send_command("O", param=relay)
        if response_lines == []:
            raise ValueError("No response received from device")
        
        error = Error(response_lines[0][1])
        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to override relay")

    def inhibit_relay(self, relay: str) -> None:
        """Permanently de-energize a relay.

        Parameters
        ----------
        relay : str
            Relay to de-energize ('A' to 'D')
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control relays")

        if relay not in "ABCD":
            raise ValueError("Relay must be 'A', 'B', 'C', or 'D'")

        response_lines = self._send_command("I", param=relay)
        if response_lines == []:
            raise ValueError("No response received from device")
        
        error = Error(response_lines[0][1])
        if error.gauge_error or error.over_temp_trip or error.temp_warning:
            raise ValueError("Failed to inhibit relay")


def list_serial_ports() -> List[str]:
    """Lists all available serial ports.

    Returns
    -------
    list of str
        List of available serial port names
    """
    if sys.platform.startswith("win"):
        ports = ["COM%s" % (i + 1) for i in range(256)]
    elif sys.platform.startswith("linux") or sys.platform.startswith("cygwin"):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob("/dev/tty[A-Za-z]*")
    elif sys.platform.startswith("darwin"):
        ports = glob.glob("/dev/tty.*")
    else:
        raise EnvironmentError("Unsupported platform")
    result: List[str] = []
    for port in ports:
        try:
            s = Serial(port)
            s.close()
            result.append(port)
        except (OSError, SerialException):
            pass
    return result


def list_instruments() -> List[ParamSet]:
    """List all available NGC2D instruments.

    Returns
    -------
    list of ParamSet
        A list of parameter sets for each available instrument
    """
    ports = list_serial_ports()
    return [ParamSet(NGC2D, port=port) for port in ports]
