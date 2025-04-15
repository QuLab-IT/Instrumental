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
_INST_PARAMS: List[str] = ['port']
_INST_CLASSES: List[str] = ['NGC2D']

class GaugeSelection(Enum):
    """Types of gauges supported by the NGC2D controller"""
    ION_GAUGE_1: str = '1'
    PIRANI_1: str = '2'
    PIRANI_2: str = '3'
    CAPACITANCE_MANOMETER: str = '4'
    ION_GAUGE_2: str = '5'

class GaugeType(Enum):
    """Types of gauges supported by the NGC2D controller"""
    ION_GAUGE: str = 'I'
    PIRANI: str = 'P'
    CAPACITANCE_MANOMETER: str = 'M'

class PressureUnit(Enum):
    """Supported pressure units"""
    TORR: str = 'T'
    PASCAL: str = 'P'
    MBAR: str = 'M'

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
    states['instrument_type'] = state_byte & 0x0F  # Bits 3-0
    states['mode'] = 'remote' if state_byte & 0x10 else 'local'  # Bit 4
    states['selected_gauge'] = 'IG2' if state_byte & 0x40 else 'IG1'  # Bit 6
    states['ig_connected'] = not bool(state_byte & 0x80)  # Bit 7
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
    errors['gauge_error'] = bool(error_byte & 0x01)  # Bit 0
    errors['over_temp_trip'] = bool(error_byte & 0x02)  # Bit 1
    errors['temp_warning'] = bool(error_byte & 0x08)  # Bit 3
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
            self._paramset['port'],
            baudrate=9600,
            bytesize=8,
            stopbits=1,
            parity='N',
            timeout=1.0
        )
        # Start in local mode
        self._remote_mode: bool = False

    def close(self) -> None:
        """Close the serial connection"""
        if self._remote_mode:
            self.release()
        self._ser.close()

    def _send_command(self, command_char: str, ignored_byte: str = '0', 
                     param: Optional[str] = None) -> Optional[Tuple[str, str, List[str]]]:
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
            (state_byte, error_byte, [response_lines]) or None if no response
        """
        cmd = f"*{command_char}{ignored_byte}"
        if param is not None:
            cmd += param
        cmd += "\r\n"
        
        self._ser.write(cmd.encode())
        
        # Read first line
        first_line = self._ser.readline().decode().strip()
        print(f"first_line: {first_line}")

        # Handle empty responses (like from control and release commands)
        if not first_line:
            return None, None, None
        
        # For responses with state and error bytes
        state_byte = first_line[0]
        error_byte = first_line[1]
        
        # For status command, read additional lines until empty line
        response_lines: List[str] = []
        if command_char == 'S':
            response_lines.append(first_line[2:])  # Add rest of first line
            while True:
                line = self._ser.readline().decode().strip()
                if not line:
                    break
                response_lines.append(line)
        print(f"state_byte: {state_byte}")
        print(f"error_byte: {error_byte}")
        print(f"response_lines: {response_lines}")
        return state_byte, error_byte, response_lines

    @property
    def state(self) -> Optional[Dict[str, Union[int, str, bool]]]:
        """Get the current state of the device.
        
        Returns
        -------
        dict
            Dictionary containing the current state information
        """
        return self._state.copy() if hasattr(self, '_state') else None

    @property
    def error(self) -> Optional[Dict[str, bool]]:
        """Get the current error status.
        
        Returns
        -------
        dict
            Dictionary containing the current error information
        """
        return self._error.copy() if hasattr(self, '_error') else None

    def poll(self) -> Tuple[str, str]:
        """Poll the instrument for state and error information.
        
        Returns
        -------
        tuple
            (state_byte, error_byte)
        """
        state, error, _ = self._send_command('P')
        return state, error

    def control(self) -> None:
        """Switch the instrument to remote control mode."""
        self._send_command('C')
        self._remote_mode = True

    def release(self) -> None:
        """Return the instrument to local control mode."""
        self._send_command('R')
        self._remote_mode = False

    def reset_error(self) -> None:
        """Reset all error flags."""
        state, error, _ = self._send_command('E')
        if error != '0':
            raise ValueError(f"Failed to reset errors: error {error}")

    def get_status(self) -> Dict[str, Any]:
        """Request a report of operating status for all gauges.
        
        Returns
        -------
        dict
            Dictionary containing status information for each gauge
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to get status")
            
        response = self._send_command('S')
        if response is None:
            raise ValueError("No response received from device")
            
        state, error, lines = response
        if not lines:
            raise ValueError("No status report received")
            
        # Parse status report from multiple lines
        gauges: Dict[str, Dict[str, Any]] = {}
        for line in lines:
            if not line.startswith('G'):
                continue
            
            # Each line format: G<type><num><status><error><pressure>,<unit>
            # Example: 'GP2A@  2E-02,M0'
            gauge_type = line[1]  # P for Pirani, I for Ion, etc.
            gauge_num = line[2]   # Gauge number
            gauge_status = line[3]
            gauge_error = line[4]
            pressure_str = line[5:].split(',')[0].strip()
            
            gauge_id = f"{gauge_type}_{gauge_num}"
            gauges[gauge_id] = {
                'type': gauge_type,
                'status': gauge_status,
                'error': gauge_error,
                'pressure': float(pressure_str) if pressure_str.strip() else None
            }
        
        return {
            'state': state,
            'error': error,
            'gauges': gauges
        }

    def gauge_on(self, emission_current: str = '0') -> None:
        """Switch on ion gauge emission.
        
        Parameters
        ----------
        emission_current : str
            '0' for 0.5mA, '1' for 5mA
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control gauge")
            
        state, error, _ = self._send_command('i', param=emission_current)
        if error != '0':
            raise ValueError(f"Failed to switch on gauge: error {error}")

    def select_ion_gauge(self, gauge_num: str) -> None:
        """Select which ion gauge to use.
        
        Parameters
        ----------
        gauge_num : str
            '1' for Ion Gauge 1, '2' for Ion Gauge 2
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to select gauge")
            
        state, error, _ = self._send_command('j', param=gauge_num)
        if error != '0':
            raise ValueError(f"Failed to select ion gauge: error {error}")

    def gauge_off(self) -> None:
        """Switch off ion gauge."""
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control gauge")
            
        state, error, _ = self._send_command('o')
        if error != '0':
            raise ValueError(f"Failed to switch off gauge: error {error}")

    def override_relay(self, relay: str) -> None:
        """Permanently energize a relay.
        
        Parameters
        ----------
        relay : str
            Relay to energize ('A' to 'D')
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control relays")
            
        if relay not in 'ABCD':
            raise ValueError("Relay must be 'A', 'B', 'C', or 'D'")
            
        state, error, _ = self._send_command('O', param=relay)
        if error != '0':
            raise ValueError(f"Failed to override relay: error {error}")

    def inhibit_relay(self, relay: str) -> None:
        """Permanently de-energize a relay.
        
        Parameters
        ----------
        relay : str
            Relay to de-energize ('A' to 'D')
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control relays")
            
        if relay not in 'ABCD':
            raise ValueError("Relay must be 'A', 'B', 'C', or 'D'")
            
        state, error, _ = self._send_command('I', param=relay)
        if error != '0':
            raise ValueError(f"Failed to inhibit relay: error {error}")

def list_serial_ports() -> List[str]:
    """Lists all available serial ports.
    
    Returns
    -------
    list of str
        List of available serial port names
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')
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