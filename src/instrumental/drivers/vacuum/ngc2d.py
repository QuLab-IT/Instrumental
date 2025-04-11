# -*- coding: utf-8 -*-
"""
Driver for NGC2D Pressure Gauge Controller.

The controller supports communication via RS232 serial interface at 9600 baud,
8 data bits, 1 stop bit, no parity, and no handshaking.
"""
from enum import Enum, Flag, auto
import sys
import glob
from serial import Serial, SerialException

from .. import Instrument, ParamSet
from ... import u

_INST_PRIORITY = 5
_INST_PARAMS = ['port']
_INST_CLASSES = ['NGC2D']

def list_serial_ports():
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
    result = []
    for port in ports:
        try:
            s = Serial(port)
            s.close()
            result.append(port)
        except (OSError, SerialException):
            pass
    return result

class GaugeSelection(Enum):
    """Types of gauges supported by the NGC2D controller"""
    ION_GAUGE_1 = '1'
    PIRANI_1 = '2'
    PIRANI_2 = '3'
    CAPACITANCE_MANOMETER = '4'
    ION_GAUGE_2 = '5'

class GaugeType(Enum):
    """Types of gauges supported by the NGC2D controller"""
    ION_GAUGE = 'I'
    PIRANI = 'P'
    CAPACITANCE_MANOMETER = 'M'

class PressureUnit(Enum):
    """Supported pressure units"""
    TORR = 'T'
    PASCAL = 'P'
    MBAR = 'M'

class StateFlags(Flag):
    """Flags representing the state byte information"""
    IG1_SELECTED = 0  # Bit 6 = 0
    IG2_SELECTED = auto()  # Bit 6 = 1
    LOCAL_MODE = 0  # Bit 4 = 0
    REMOTE_MODE = auto()  # Bit 4 = 1
    IG_CONNECTED = 0  # Bit 7 = 0
    IG_DISCONNECTED = auto()  # Bit 7 = 1

class ErrorFlags(Flag):
    """Flags representing the error byte information"""
    GAUGE_ERROR = auto()  # Bit 0
    OVER_TEMP_TRIP = auto()  # Bit 1
    TEMP_WARNING = auto()  # Bit 3

def parse_state_byte(state_byte: int) -> dict:
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
    states = {}
    states['instrument_type'] = state_byte & 0x0F  # Bits 3-0
    states['mode'] = 'remote' if state_byte & 0x10 else 'local'  # Bit 4
    states['selected_gauge'] = 'IG2' if state_byte & 0x40 else 'IG1'  # Bit 6
    states['ig_connected'] = not bool(state_byte & 0x80)  # Bit 7
    return states

def parse_error_byte(error_byte: int) -> dict:
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
    errors = {}
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
    def _initialize(self):
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
        self._remote_mode = False

    def close(self):
        """Close the serial connection"""
        if self._remote_mode:
            self.release()
        self._ser.close()

    def _send_command(self, command_char, ignored_byte='0', param=None):
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
            (state_byte, error_byte, status_report)
        """
        cmd = f"*{command_char}{ignored_byte}"
        if param is not None:
            cmd += param
        cmd += "\r\n"
        
        self._ser.write(cmd.encode())
        response = self._ser.readline().decode().strip()
        
        if len(response) < 2:
            print(f"Invalid response from device: {response}")
            return None, None, None
            
        # Convert string bytes to integers for parsing
        state_byte = int.from_bytes(response[0].encode(), 'big')
        error_byte = int.from_bytes(response[1].encode(), 'big')
        
        # Parse state and error information
        self._state = parse_state_byte(state_byte)
        self._error = parse_error_byte(error_byte)
        
        # Store the raw bytes for debugging
        self._raw_state = state_byte
        self._raw_error = error_byte
        
        # Raise exception if there are errors
        if any(self._error.values()):
            error_msg = ', '.join(f"{k}" for k, v in self._error.items() if v)
            raise ValueError(f"Device errors detected: {error_msg}")
        
        return self._state, self._error, response[2:] if len(response) > 2 else None

    @property
    def state(self) -> dict:
        """Get the current state of the device.
        
        Returns
        -------
        dict
            Dictionary containing the current state information
        """
        return self._state.copy() if hasattr(self, '_state') else None

    @property
    def error(self) -> dict:
        """Get the current error status.
        
        Returns
        -------
        dict
            Dictionary containing the current error information
        """
        return self._error.copy() if hasattr(self, '_error') else None

    def poll(self):
        """Poll the instrument for state and error information.
        
        Returns
        -------
        tuple
            (state_byte, error_byte)
        """
        state, error, _ = self._send_command('P')
        return state, error

    def control(self):
        """Switch the instrument to remote control mode."""
        state, error, _ = self._send_command('C')
        if error != '0':
            raise ValueError(f"Failed to switch to remote control: error {error}")
        self._remote_mode = True

    def release(self):
        """Return the instrument to local control mode."""
        state, error, _ = self._send_command('R')
        if error != '0':
            raise ValueError(f"Failed to switch to local control: error {error}")
        self._remote_mode = False

    def reset_error(self):
        """Reset all error flags."""
        state, error, _ = self._send_command('E')
        if error != '0':
            raise ValueError(f"Failed to reset errors: error {error}")

    def get_status(self):
        """Request a report of operating status for all gauges.
        
        Returns
        -------
        dict
            Dictionary containing status information for each gauge
        """
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to get status")
            
        state, error, status = self._send_command('S')
        if not status:
            raise ValueError("No status report received")
            
        # Parse status report
        # Format: State byte, Error byte, Relay status byte, Unused byte,
        #         Gauge records (each with header, type, number, status, error, pressure)
        gauges = {}
        pos = 0
        while pos < len(status):
            if status[pos] == 'G':  # Gauge record header
                gauge_type = status[pos+1]
                gauge_num = status[pos+2]
                gauge_status = status[pos+3]
                gauge_error = status[pos+4]
                pressure = status[pos+5:pos+13]
                
                gauge_id = f"{gauge_type}_{gauge_num}"
                print(pressure)
                gauges[gauge_id] = {
                    'type': GaugeType(gauge_type),
                    'num': GaugeSelection(gauge_num),
                    'status': gauge_status,
                    'error': gauge_error,
                    'pressure': float(pressure.strip(',')) if pressure.strip() else None
                }
                pos += 13
            else:
                pos += 1
                
        # Add state and error information to the response
        result = {
            'state': state,
            'error': error,
            'gauges': gauges
        }
        
        return result

    def gauge_on(self, emission_current='0'):
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

    def select_ion_gauge(self, gauge_num):
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

    def gauge_off(self):
        """Switch off ion gauge."""
        if not self._remote_mode:
            raise RuntimeError("Must be in remote control mode to control gauge")
            
        state, error, _ = self._send_command('o')
        if error != '0':
            raise ValueError(f"Failed to switch off gauge: error {error}")

    def override_relay(self, relay):
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

    def inhibit_relay(self, relay):
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

def list_instruments():
    """List all available NGC2D instruments.
    
    Returns
    -------
    list of ParamSet
        A list of parameter sets for each available instrument
    """
    ports = list_serial_ports()
    return [ParamSet(NGC2D, port=port) for port in ports] 