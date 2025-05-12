import functools
import inspect
import numpy as np

from enum import Enum
from instrumental.drivers import VisaMixin
from instrumental.drivers.funcgenerators import FunctionGenerator # Assuming this is the correct base class
from numpy.typing import NDArray # Included if any type hints might resolve to NDArray
from typing import (
    Any,
    Callable,
    Dict,
    List,
    overload,
    Union
) # Added for type hints


_BASIC_TYPE_MAP = {
    'int': int,
    'float': float,
    'str': str,
    'bool': bool,
    'Boolean': bool, # Handle a common alias
}

def validate_parameters(rules_list: List[Dict[str, Any]] | None = None):
    if rules_list is None:
        rules_list = []
    
    param_rules: Dict[str, Dict[str, Any]] = {rule['name']: rule for rule in rules_list}

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(self: Any, *args: Any, **kwargs: Any) -> Any:
            sig = inspect.signature(func)
            try:
                bound_args = sig.bind(self, *args, **kwargs)
            except TypeError as e:
                raise TypeError(
                    f"Error binding arguments for {func.__name__}{sig}: {e}. "
                    f"Provided args: {args}, kwargs: {kwargs}"
                ) from e
            
            bound_args.apply_defaults()
            
            # --- 1. Validation Phase ---
            for param_name, arg_value in bound_args.arguments.items():
                if param_name == 'self':
                    continue

                rule = param_rules.get(param_name)
                if not rule:
                    continue

                type_options = rule.get('type_options', [])
                if not type_options or 'Any' in type_options: # Allow 'Any' to bypass type checks
                    pass
                else:
                    type_match_found = False
                    for type_str_opt in type_options:
                        expected_py_type = _BASIC_TYPE_MAP.get(type_str_opt)
                        if expected_py_type:
                            # Handle basic Python types (int, float, str, bool)
                            # Allow int to be passed for a float parameter
                            if (expected_py_type is float and isinstance(arg_value, int)) or \
                               isinstance(arg_value, expected_py_type):
                                type_match_found = True
                                break
                        else:
                            # Assume type_str_opt is an Enum class name string
                            enum_class = globals().get(type_str_opt)
                            if enum_class and isinstance(enum_class, type) and issubclass(enum_class, Enum):
                                if isinstance(arg_value, enum_class):
                                    type_match_found = True
                                    break
                                # else:
                                    # Coercion logic for enums from raw values was here, removed for stricter typing based on user request focus.
                                    # If needed, it could be: 
                                    # try: enum_class(arg_value); type_match_found = True; break
                                    # except (ValueError, TypeError): pass
                            # else:
                                # print(f"Warning: Unrecognized type '{type_str_opt}' in validation rule for '{param_name}' of {func.__name__}")

                    if not type_match_found:
                        expected_types_str = ", ".join(type_options)
                        raise TypeError(
                            f"Parameter '{param_name}' for {func.__name__} expected one of types "
                            f"[{expected_types_str}], but got {type(arg_value).__name__} with value {arg_value!r}."
                        )

                # --- Min/Max Value Validation ---
                current_value_for_range_check = arg_value

                if not isinstance(current_value_for_range_check, Enum):
                    min_val = rule.get('min_val')
                    if min_val is not None:
                        try:
                            if float(current_value_for_range_check) < float(min_val):
                                raise ValueError(
                                    f"Parameter '{param_name}' for {func.__name__} is {current_value_for_range_check}, "
                                    f"which is less than minimum value {min_val}."
                                )
                        except (TypeError, ValueError):
                            pass 

                    max_val = rule.get('max_val')
                    if max_val is not None:
                        try:
                            if float(current_value_for_range_check) > float(max_val):
                                raise ValueError(
                                    f"Parameter '{param_name}' for {func.__name__} is {current_value_for_range_check}, "
                                    f"which is greater than maximum value {max_val}."
                                )
                        except (TypeError, ValueError):
                            pass

            # --- 2. Transformation Phase (Enum to .value for mixed Unions) ---
            for param_name, arg_value in bound_args.arguments.items():
                if param_name == 'self':
                    continue

                if isinstance(arg_value, Enum):
                    bound_args.arguments[param_name] = arg_value.name
            
            return func(*bound_args.args, **bound_args.kwargs)
        return wrapper
    return decorator


# --- Global Enums ---
class Boolean(Enum):
    """
    Enum for Boolean
    """

    ON = '1'
    OFF = '0'


class Enumminmaxdefinf(Enum):
    """
    Enum for enumMinMaxDefInf
    """

    MINIMUM = '1'
    MAXIMUM = '2'
    DEFAULT = '5'
    INFINITY = '7'


class FormBorder(Enum):
    """
    Enum for form_border
    """

    NORMAL = '0'
    SWAPPED = '1'


class Minmax(Enum):
    """
    Enum for MinMax
    """

    MINIMUM = '1'
    MAXIMUM = '2'


class Minmaxdef(Enum):
    """
    Enum for MinMaxDef
    """

    MINIMUM = '1'
    MAXIMUM = '2'
    DEFAULT = '5'


class OutpPolarity(Enum):
    """
    Enum for outp_polarity
    """

    NORMAL = '0'
    INVERTED = '1'


class OutpTrigSlope(Enum):
    """
    Enum for outp_trig_slope
    """

    POSITIVE = '1'
    NEGATIVE = '2'


class SourAmIntFuncShape(Enum):
    """
    Enum for sour_am_int_func_shape
    """

    SINUSOID = '0'
    SQUARE = '1'
    TRIANGLE = '2'
    RAMP = '3'
    NRAMP = '4'
    NOISE = '5'
    USER = '6'


class SourAmSource(Enum):
    """
    Enum for sour_am_source
    """

    INTERNAL = '0'
    EXTERNAL = '1'


class SourBursGatePolarity(Enum):
    """
    Enum for sour_burs_gate_polarity
    """

    NORMAL = '0'
    INVERTED = '1'


class SourBursMode(Enum):
    """
    Enum for sour_burs_mode
    """

    TRIGGERED = '0'
    GATED = '1'


class SourFmIntFuncShape(Enum):
    """
    Enum for sour_fm_int_func_shape
    """

    SINUSOID = '0'
    SQUARE = '1'
    TRIANGLE = '2'
    RAMP = '3'
    NRAMP = '4'
    NOISE = '5'
    USER = '6'


class SourFmSource(Enum):
    """
    Enum for sour_fm_source
    """

    INTERNAL = '0'
    EXTERNAL = '1'


class SourFskSource(Enum):
    """
    Enum for sour_fsk_source
    """

    INTERNAL = '0'
    EXTERNAL = '1'


class SourFuncShape(Enum):
    """
    Enum for sour_func_shape
    """

    SINUSOID = '0'
    SQUARE = '1'
    RAMP = '2'
    PULSE = '3'
    NOISE = '4'
    USER = '5'
    DC = '6'


class SourSweSpacing(Enum):
    """
    Enum for sour_swe_spacing
    """

    LINEAR = '0'
    LOGARITHMIC = '1'


class SourVoltLevImmUnitVoltage(Enum):
    """
    Enum for sour_volt_lev_imm_unit_voltage
    """

    VPP = '0'
    VRMS = '1'
    DBM = '2'


class SourVoltRangAuto(Enum):
    """
    Enum for sour_volt_rang_auto
    """

    OFF = '0'
    ON = '1'
    ONCE = '2'


class TracData(Enum):
    """
    Enum for trac_data
    """

    VOLATILE = '0'


class TracDataDac(Enum):
    """
    Enum for trac_data_dac
    """

    VOLATILE = '0'


class TrigSeqSlope(Enum):
    """
    Enum for trig_seq_slope
    """

    POSITIVE = '0'
    NEGATIVE = '1'


class TrigSeqSource(Enum):
    """
    Enum for trig_seq_source
    """

    IMMEDIATE = '0'
    EXTERNAL = '1'
    BUS = '2'


class UnitAngle(Enum):
    """
    Enum for unit_angle
    """

    DEGREE = '0'
    RADIAN = '1'


# --- Command Syntax Enums ---
class DataDataDacSyntax(Enum):
    """
    Enum for command syntaxes of DATA:DATA:DAC
    """
    VALUELIST = "ValueList"
    BINARYBLOCK = "BinaryBlock"



# --- Validator Decorator Definition ---


# --- Main Instrument Class ---
class Keysight33250A(FunctionGenerator, VisaMixin):
    """Main class for controlling the Keysight 33250A function generators.
    
    This class is auto-generated from an SDL file.
    """
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = (
        'Agilent Technologies', [
            '33250A',
        ]
    )

    def _initialize(self):
        super()._initialize() # Call parent _initialize if it exists
        self._rsrc.timeout = 2000  # ms
        self._rsrc.write_termination = '\n'
        self._rsrc.read_termination = '\n'

    # --- Binary Format Handling Methods ---
    
    def _set_binary_format(self, format_name: str) -> None:
        """Set the binary data format for subsequent commands.
        
        Args:
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
        """
        format_commands = {
            'BlockInt16': 'FORMat:BORDer SWAPped',
            'BlockReal32': 'FORMat:BORDer SWAPped',
            'BlockInt16xxx': 'FORMat:BORDer SWAPped',
            'BlockReal32xxx': 'FORMat:BORder SWAPped'
        }
        if format_name not in format_commands:
            raise ValueError(f"Unsupported binary format: {format_name}")
        self._rsrc.write(format_commands[format_name])

    def _prepare_binary_data(self, data: Any, format_name: str) -> bytes:
        """Prepare binary data according to the specified format.
        
        Args:
            data: The data to convert
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
            
        Returns:
            bytes: The prepared binary data
        """
        if format_name.startswith('BlockInt16'):
            if isinstance(data, (list, tuple, np.ndarray)):
                data = np.array(data, dtype=np.int16)
            else:
                data = np.array([data], dtype=np.int16)
            return data.tobytes()
            
        elif format_name.startswith('BlockReal32'):
            if isinstance(data, (list, tuple, np.ndarray)):
                data = np.array(data, dtype=np.float32)
            else:
                data = np.array([data], dtype=np.float32)
            return data.tobytes()
            
        else:
            raise ValueError(f"Unsupported binary format: {format_name}")

    def _write_binary_data(self, cmd: str, data: Any, format_name: str) -> None:
        """Write a command with binary data.
        
        Args:
            cmd: The SCPI command string
            data: The binary data to write
            format_name: The format name (e.g., 'BlockInt16', 'BlockReal32')
        """
        # Set the binary format
        self._set_binary_format(format_name)
        
        # Prepare the binary data
        binary_data = self._prepare_binary_data(data, format_name)
        
        # Write the command and data
        self._rsrc.write_binary_values(cmd, binary_data)




    # --- Direct Commands (defined at the root of the SDL) ---
    def cls(self) -> None:
        """
        Clear the event register in all register groups. This command also clears the error queue and cancels a *OPC operation. 

        Args:
        """
        cmd = f"*CLS"
        self._rsrc.write(cmd)

    def get_ese(self) -> int:
        """
        Enable bits in the Standard Event Status Register to be reported in the Status Byte. The selected bits are summarized in the "Standard Event" bit (bit 5) of the Status Byte Register. 


        Returns:
            int: The selected bits enabled in the Standard Event Status Register to be reported in the Status Byte.
        """
        cmd = f"*ESE?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'enableValue', 'type_options': ['int']}]
    )
    def set_ese(self, enableValue: int) -> None:
        """
        Enable bits in the Standard Event Status Register to be reported in the Status Byte. The selected bits are summarized in the "Standard Event" bit (bit 5) of the Status Byte Register. 

        Args:
            enableValue (int): The selected bits to be enabled in the Standard Event Status Register to be reported in the Status Byte.
        """
        cmd = f"*ESE {enableValue}"
        self._rsrc.write(cmd)

    def get_esr(self) -> int:
        """
        Query the Standard Event Status Register. Once a bit is set, it remains set until cleared by a *CLS (clear status) command or queried by this command. 


        Returns:
            int: A decimal value which corresponds to the binary-weighted sum of all bits set in the Standard Event Status register.
        """
        cmd = f"*ESR?"
        response = self._rsrc.query(cmd)
        return int(response)

    def get_idn(self) -> str:
        """
        Read the function generator's identification string which contains four fields separated by commas. The first field is the manufacturer's name, the second field is the model number, the third field is the serial number, and the fourth field is a revision code which contains four numbers separated by dashes. 


        Returns:
            str: The function generator's identification string.  The first field is the manufacturer's name, the second field is the model number, the third field is the serial number, and the fourth field is a revision code which contains four numbers separated by dashes. 
        """
        cmd = f"*IDN?"
        response = self._rsrc.query(cmd)
        return response

    def get_lrn(self) -> str:
        """
        Query the function generator and return a string of SCPI commands containing the current settings (learn string). You can then send the string back to the instrument to restore this state at a later time. 


        Returns:
            str: A string of SCPI commands containing the current settings (learn string).
        """
        cmd = f"*LRN?"
        response = self._rsrc.query(cmd)
        return response

    def get_opc(self) -> bool:
        """
        Set the "Operation Complete" bit (bit 0) in the Standard Event register after the previous commands have completed. When used with a bus-triggered sweep or burst, you may have the opportunity to execute commands after the *OPC command and before the "Operation Complete" bit is set in the register. 


        Returns:
            bool: The "Operation Complete" bit (bit 0) in the Standard Event register.
        """
        cmd = f"*OPC?"
        response = self._rsrc.query(cmd)
        return bool(response)

    def opc(self) -> None:
        """
        Set the "Operation Complete" bit (bit 0) in the Standard Event register after the previous commands have completed. When used with a bus-triggered sweep or burst, you may have the opportunity to execute commands after the *OPC command and before the "Operation Complete" bit is set in the register. 

        Args:
        """
        cmd = f"*OPC"
        self._rsrc.write(cmd)

    def get_psc(self) -> bool:
        """
        Power-On Status Clear. Clear the Standard Event enable register and Status Byte condition register at power on (*PSC 1). When *PSC 0 is in effect, these two registers are not cleared at power on. 


        Returns:
            bool: The present setting of the power-on status clear. Returns "0" (do not clear at power on) or "1" (clear at power on). 
        """
        cmd = f"*PSC?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'psc', 'type_options': ['int']}]
    )
    def set_psc(self, psc: int) -> None:
        """
        Power-On Status Clear. Clear the Standard Event enable register and Status Byte condition register at power on (*PSC 1). When *PSC 0 is in effect, these two registers are not cleared at power on. 

        Args:
            psc (int): 0|1
        """
        cmd = f"*PSC {psc}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'location', 'type_options': ['int']}]
    )
    def set_rcl(self, location: int) -> None:
        """
        Recall the instrument state stored in the specified non-volatile storage location. You cannot recall the instrument state from a storage location that is empty. 

        Args:
            location (int): 0|1|2|3|4
        """
        cmd = f"*RCL {location}"
        self._rsrc.write(cmd)

    def rst(self) -> None:
        """
        Reset the function generator to its factory default state.

        Args:
        """
        cmd = f"*RST"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'location', 'type_options': ['int']}]
    )
    def set_sav(self, location: int) -> None:
        """
        Store (save) the current instrument state in the specified non-volatile storage location. Any state previously stored in the same location will be overwritten (and no error will be generated). 

        Args:
            location (int): 0|1|2|3|4
        """
        cmd = f"*SAV {location}"
        self._rsrc.write(cmd)

    def get_sre(self) -> int:
        """
        Enable bits in the Status Byte to generate a Service Request. The selected bits are summarized in the "Master Summary" bit (bit 6) of the Status Byte Register. If any of the selected bits change from "0" to "1", a Service Request signal is generated. 


        Returns:
            int: A decimal value which corresponds to the binary-weighted sum of all bits enabled by the *SRE command.
        """
        cmd = f"*SRE?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'enableValue', 'type_options': ['int']}]
    )
    def set_sre(self, enableValue: int) -> None:
        """
        Enable bits in the Status Byte to generate a Service Request. The selected bits are summarized in the "Master Summary" bit (bit 6) of the Status Byte Register. If any of the selected bits change from "0" to "1", a Service Request signal is generated. 

        Args:
            enableValue (int): The selected bits to be enabled in the Status Byte to generate a Service Request.
        """
        cmd = f"*SRE {enableValue}"
        self._rsrc.write(cmd)

    def get_stb(self) -> int:
        """
        Query the summary (condition) register in this register group. This command is similar to a Serial Poll but it is processed like any other instrument command. This command returns the same result as a Serial Poll but the "Master Summary" bit (bit 6) is not cleared by the *STB? command. 


        Returns:
            int: The summary (condition) register in this register group.
        """
        cmd = f"*STB?"
        response = self._rsrc.query(cmd)
        return int(response)

    def trg(self) -> None:
        """
        Trigger a sweep or burst from the remote interface only if the bus (software) trigger source is currently selected (TRIG:SOUR BUS command). 

        Args:
        """
        cmd = f"*TRG"
        self._rsrc.write(cmd)

    def get_tst(self) -> int:
        """
        Perform a complete self-test of the function generator. Returns "+0" (PASS) or "+1" (FAIL). If the test fails, one or more error messages will be generated to provide additional information on the failure. 


        Returns:
            int: "+0" (PASS) or "+1" (FAIL) indicating the result of the complete self-test.
        """
        cmd = f"*TST?"
        response = self._rsrc.query(cmd)
        return int(response)

    def wai(self) -> None:
        """
        Wait for all pending operations to complete before executing any additional commands over the interface. 

        Args:
        """
        cmd = f"*WAI"
        self._rsrc.write(cmd)

    # --- Subsystem Commands ---
    def get_apply(self) -> str:
        """
        Query the function generator's current configuration and return a quoted string.


        Returns:
            str: The function generator's current function, frequency, amplitude, and offset.
        """
        cmd = f":APPLy?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}, {'name': 'amplitude', 'type_options': ['float', 'Minmaxdef']}, {'name': 'offset', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_apply_dc(self, frequency: Union[float, Minmaxdef], amplitude: Union[float, Minmaxdef], offset: Union[float, Minmaxdef]) -> None:
        """
        Output a dc voltage with the level specified by the offset parameter. The dc voltage is output as soon as the command is executed. 

        Args:
            frequency (float): DEFault
            amplitude (float): DEFault
            offset (float): Any value between ±5 Vdc into 50 ohms or ±10 Vdc.
        """
        cmd = f":APPLy:DC {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}, {'name': 'amplitude', 'type_options': ['float', 'Minmaxdef']}, {'name': 'offset', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_apply_noise(self, frequency: Union[float, Minmaxdef], amplitude: Union[float, Minmaxdef], offset: Union[float, Minmaxdef]) -> None:
        """
        Output Gaussian noise with the specified amplitude and dc offset. The waveform is output as soon as the command is executed. 

        Args:
            frequency (float): The specified frequency of the output Gaussian noise.
            amplitude (float): The specified amplitude of the output Gaussian noise.
            offset (float): The specified dc offset of the output Gaussian noise.
        """
        cmd = f":APPLy:NOISe {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}, {'name': 'amplitude', 'type_options': ['float', 'Minmaxdef']}, {'name': 'offset', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_apply_pulse(self, frequency: Union[float, Minmaxdef], amplitude: Union[float, Minmaxdef], offset: Union[float, Minmaxdef]) -> None:
        """
        Output a pulse wave with the specified frequency, amplitude, and dc offset. The waveform is output as soon as the command is executed. 

        Args:
            frequency (float): The specified frequency of the output pulse wave.
            amplitude (float): The specified amplitude of the output pulse wave.
            offset (float): The specified offset of the output pulse wave.
        """
        cmd = f":APPLy:PULSe {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}, {'name': 'amplitude', 'type_options': ['float', 'Minmaxdef']}, {'name': 'offset', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_apply_ramp(self, frequency: Union[float, Minmaxdef], amplitude: Union[float, Minmaxdef], offset: Union[float, Minmaxdef]) -> None:
        """
        Output a ramp wave with the specified frequency, amplitude, and dc offset. This command overrides the current symmetry setting and automatically selects 100%. The waveform is output as soon as the command is executed. 

        Args:
            frequency (float): The specified frequency of the output ramp wave.
            amplitude (float): The specified amplitude of the output ramp wave.
            offset (float): The specified offset of the output ramp wave.
        """
        cmd = f":APPLy:RAMP {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}, {'name': 'amplitude', 'type_options': ['float', 'Minmaxdef']}, {'name': 'offset', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_apply_sinusoid(self, frequency: Union[float, Minmaxdef], amplitude: Union[float, Minmaxdef], offset: Union[float, Minmaxdef]) -> None:
        """
        Output a sine wave with the specified frequency, amplitude, and dc offset. The waveform is output as soon as the command is executed. 

        Args:
            frequency (float): The specified frequency of the output sine wave.
            amplitude (float): The specified amplitude of the output ramp wave.
            offset (float): The specified offset of the output ramp wave.
        """
        cmd = f":APPLy:SINusoid {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}, {'name': 'amplitude', 'type_options': ['float', 'Minmaxdef']}, {'name': 'offset', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_apply_square(self, frequency: Union[float, Minmaxdef], amplitude: Union[float, Minmaxdef], offset: Union[float, Minmaxdef]) -> None:
        """
        Output a square wave with the specified frequency, amplitude, and dc offset. This command overrides the current duty cycle setting and automatically selects 50%. The waveform is output as soon as the command is executed. 

        Args:
            frequency (float): The specified frequency of the output square wave.
            amplitude (float): The specified amplitude of the output square wave.
            offset (float): The specified offset of the output square wave.
        """
        cmd = f":APPLy:SQUare {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}, {'name': 'amplitude', 'type_options': ['float', 'Minmaxdef']}, {'name': 'offset', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_apply_user(self, frequency: Union[float, Minmaxdef], amplitude: Union[float, Minmaxdef], offset: Union[float, Minmaxdef]) -> None:
        """
        Output the arbitrary waveform currently selected by the FUNC:USER command. The waveform is output using the specified frequency, amplitude, and dc offset. The waveform is output as soon as the command is executed. 

        Args:
            frequency (float): The specified frequency of the output arbitrary waveform.
            amplitude (float): The specified amplitude of the output arbitrary waveform.
            offset (float): The specified offset of the output arbitrary waveform.
        """
        cmd = f":APPLy:USER {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)



    def get_calibrate_all(self) -> int:
        """
        Perform a calibration of the instrument using the specified calibration value (CAL:VAL command). Before you can calibrate the function generator, you must unsecure it by entering the correct security code. 


        Returns:
            int: Returns "0" (PASS) or "1" (FAIL).
        """
        cmd = f":CALibrate:ALL?"
        response = self._rsrc.query(cmd)
        return int(response)


    def get_calibrate_count(self) -> int:
        """
        Query the instrument to determine the number of times it has been calibrated. 


        Returns:
            int: The number of times the instrument has been calibrated.
        """
        cmd = f":CALibrate:COUNt?"
        response = self._rsrc.query(cmd)
        return int(response)


    @validate_parameters(
        rules_list=[{'name': 'newCode', 'type_options': ['str']}]
    )
    def set_calibrate_secure_code(self, newCode: str) -> None:
        """
        Enter a new security code. To change the security code, you must first unsecure the function generator using the old security code, and then enter a new code. The security code is stored in non-volatile memory. 

        Args:
            newCode (str): The calibration code may contain up to 12 characters. The first character must be a letter (A-Z), but the remaining characters can be letters, numbers (0-9), or the underscore character (" _ "). You do not have to use all 12 characters, but the first character must always be a letter. 
        """
        cmd = f":CALibrate:SECure:CODE {newCode}"
        self._rsrc.write(cmd)


    def get_calibrate_secure_state(self) -> Boolean:
        """
        Unsecure or secure the instrument for calibration. 


        Returns:
            bool: The secure state of the instrument.
        """
        cmd = f":CALibrate:SECure:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'code', 'type_options': ['str']}]
    )
    def set_calibrate_secure_state(self, state: Boolean, code: str) -> None:
        """
        Unsecure or secure the instrument for calibration. 

        Args:
            state (bool): The secure state of the instrument.
            code (str): Calibration code may contain up to 12 characters.
        """
        cmd = f":CALibrate:SECure:STATe {state}, {code}"
        self._rsrc.write(cmd)



    def get_calibrate_setup(self) -> int:
        """
        Configure the function generator's internal state for each of the calibration steps to be performed. 


        Returns:
            int: The function generator's internal state for each of the calibration steps to be performed.
        """
        cmd = f":CALibrate:SETup?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'setup', 'type_options': ['int']}]
    )
    def set_calibrate_setup(self, setup: int) -> None:
        """
        Configure the function generator's internal state for each of the calibration steps to be performed. 

        Args:
            setup (int): 0|1|2|3| . . . |115
        """
        cmd = f":CALibrate:SETup {setup}"
        self._rsrc.write(cmd)


    def get_calibrate_string(self) -> str:
        """
        Store a message in non-volatile calibration memory. Storing a message will overwrite any message previously stored in memory. 


        Returns:
            str: The present calibration message.
        """
        cmd = f":CALibrate:STRing?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'quotedString', 'type_options': ['str']}]
    )
    def set_calibrate_string(self, quotedString: str) -> None:
        """
        Store a message in non-volatile calibration memory. Storing a message will overwrite any message previously stored in memory. 

        Args:
            quotedString (str): The calibration message may contain up to 40 characters (additional characters are truncated).
        """
        cmd = f":CALibrate:STRing {quotedString}"
        self._rsrc.write(cmd)


    def get_calibrate_value(self) -> float:
        """
        Specify the value of the known calibration signal as outlined in the calibration procedures in the Agilent 33250A Service Guide. 


        Returns:
            float: The value of the known calibration signal as outlined in the calibration procedures in the Agilent 33250A Service Guide.
        """
        cmd = f":CALibrate:VALue?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'value', 'type_options': ['float']}]
    )
    def set_calibrate_value(self, value: float) -> None:
        """
        Specify the value of the known calibration signal as outlined in the calibration procedures in the Agilent 33250A Service Guide. 

        Args:
            value (float): The value of the known calibration signal as outlined in the calibration procedures in the Agilent 33250A Service Guide.
        """
        cmd = f":CALibrate:VALue {value}"
        self._rsrc.write(cmd)



    def get_display_window_state(self) -> Boolean:
        """
        Disable or enable the function generator front-panel display. When it is disabled, the front-panel display is blanked (however, the bulb used to backlight the display remains enabled). 


        Returns:
            bool: The state of the function generator front-panel display.
        """
        cmd = f":DISPlay:WINDow:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_display_window_state(self, state: Boolean) -> None:
        """
        Disable or enable the function generator front-panel display. When it is disabled, the front-panel display is blanked (however, the bulb used to backlight the display remains enabled). 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":DISPlay:WINDow:STATe {state}"
        self._rsrc.write(cmd)


    def display_window_text_clear(self) -> None:
        """
        Clear the text message currently shown on the function generator's front-panel display. 

        Args:
        """
        cmd = f":DISPlay:WINDow:TEXT:CLEar"
        self._rsrc.write(cmd)


    def get_display_window_text_data(self) -> str:
        """
        Display a text message on the function generator's front-panel display. Sending a text message to the display overrides the display state as set by the DISP command. 


        Returns:
            str: The text message shown on the function generator's front-panel display.
        """
        cmd = f":DISPlay:WINDow:TEXT:DATA?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'quotedString', 'type_options': ['str']}]
    )
    def set_display_window_text_data(self, quotedString: str) -> None:
        """
        Display a text message on the function generator's front-panel display. Sending a text message to the display overrides the display state as set by the DISP command. 

        Args:
            quotedString (str): You can use upper- or lower-case letters (A-Z), numbers (0-9), and any other character on a standard computer keyboard. Depending on the number of characters you specify in the string, the function generator will choose one of two font sizes to display the message. You can display approximately 12 characters in a large font and approximately 40 characters in a small font. 
        """
        cmd = f":DISPlay:WINDow:TEXT:DATA {quotedString}"
        self._rsrc.write(cmd)





    def get_format_border(self) -> FormBorder:
        """
        Used for binary block transfers only. Select the byte order for binary transfers in the block mode using the DATA:DAC command. 


        Returns:
            str: The byte order for binary transfers in the block mode using the DATA:DAC command.
        """
        cmd = f":FORMat:BORDer?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'bOrder', 'type_options': ['FormBorder']}]
    )
    def set_format_border(self, bOrder: FormBorder) -> None:
        """
        Used for binary block transfers only. Select the byte order for binary transfers in the block mode using the DATA:DAC command. 

        Args:
            bOrder (str): NORMal|SWAPped
        """
        cmd = f":FORMat:BORDer {bOrder}"
        self._rsrc.write(cmd)



    def get_memory_nstates(self) -> int:
        """
        Query the total number of memory locations available for state storage. 


        Returns:
            int: The total number of memory locations available for state storage. Always returns "5" (memory location "0" is included).
        """
        cmd = f":MEMory:NSTates?"
        response = self._rsrc.query(cmd)
        return int(response)


    @validate_parameters(
        rules_list=[{'name': 'location', 'type_options': ['int']}]
    )
    def set_memory_state_delete(self, location: int) -> None:
        """
        Delete the contents of the specified storage location. If you have assigned a user-defined name to a location (MEM:STAT:NAME command), this command also removes the name that you assigned and restores the default name ("AUTO_RECALL", "STATE_1", "STATE_2", etc.). 

        Args:
            location (int): 0|1|2|3|4
        """
        cmd = f":MEMory:STATe:DELete {location}"
        self._rsrc.write(cmd)


    def get_memory_state_name(self) -> str:
        """
        Assign a custom name to the specified storage location.


        Returns:
            str: The custom name of the specified storage location.
        """
        cmd = f":MEMory:STATe:NAME?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'location', 'type_options': ['int']}, {'name': 'name', 'type_options': ['str']}]
    )
    def set_memory_state_name(self, location: int, name: str) -> None:
        """
        Assign a custom name to the specified storage location.

        Args:
            location (int): 0|1|2|3|4
            name (str): The name can contain up to 12 characters. The first character must be a letter (A-Z), but the remaining characters can be letters, numbers (0-9), or the underscore character (" _ "). Blank spaces are not allowed. An error is generated if you specify a name with more than 12 characters.
        """
        cmd = f":MEMory:STATe:NAME {location}, {name}"
        self._rsrc.write(cmd)


    def get_memory_state_recall_auto(self) -> Boolean:
        """
        Disable or enable the automatic recall of the power-down state from storage location "0" when power is turned on. 


        Returns:
            bool: The present automatic recall state of the power-down state from storage location "0" when power is turned on.
        """
        cmd = f":MEMory:STATe:RECall:AUTO?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'auto', 'type_options': ['Boolean']}]
    )
    def set_memory_state_recall_auto(self, auto: Boolean) -> None:
        """
        Disable or enable the automatic recall of the power-down state from storage location "0" when power is turned on. 

        Args:
            auto (bool): OFF|ON
        """
        cmd = f":MEMory:STATe:RECall:AUTO {auto}"
        self._rsrc.write(cmd)



    def get_memory_state_valid(self) -> Boolean:
        """
        Query the specified storage location to determine if a valid state is currently stored in that location. 


        Returns:
            bool: Whether a valid state is stored in the specified storage location. "0" if no state has been stored or if it has been deleted, "1" if a valid state is stored in the specified location. 
        """
        cmd = f":MEMory:STATe:VALid?"
        response = self._rsrc.query(cmd)
        return bool(response)




    def get_output_load(self) -> float:
        """
        Select the desired output termination (i.e., the impedance of the load attached to the output of the Agilent 33250A). The specified value is used for amplitude, offset, and high/low level settings. 


        Returns:
            float: The desired output termination (i.e., the impedance of the load attached to the output of the Agilent 33250A). 
        """
        cmd = f":OUTPut:LOAD?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'ohms', 'type_options': ['float', 'Enumminmaxdefinf']}]
    )
    def set_output_load(self, ohms: Union[float, Enumminmaxdefinf]) -> None:
        """
        Select the desired output termination (i.e., the impedance of the load attached to the output of the Agilent 33250A). The specified value is used for amplitude, offset, and high/low level settings. 

        Args:
            ohms (float): MINimum | MAXimum | DEFault | INFinity
        """
        cmd = f":OUTPut:LOAD {ohms}"
        self._rsrc.write(cmd)


    def get_output_polarity(self) -> OutpPolarity:
        """
        Invert the waveform relative to the offset voltage. In the normal mode (default), the waveform goes positive during the first part of the cycle. In the inverted mode, the waveform goes negative during the first part of the cycle. 


        Returns:
            str: The polarity setting of the waveform.
        """
        cmd = f":OUTPut:POLarity?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'polarity', 'type_options': ['OutpPolarity']}]
    )
    def set_output_polarity(self, polarity: OutpPolarity) -> None:
        """
        Invert the waveform relative to the offset voltage. In the normal mode (default), the waveform goes positive during the first part of the cycle. In the inverted mode, the waveform goes negative during the first part of the cycle. 

        Args:
            polarity (str): NORMal|INVerted
        """
        cmd = f":OUTPut:POLarity {polarity}"
        self._rsrc.write(cmd)


    def get_output_state(self) -> Boolean:
        """
        Disable or enable the front-panel Output connector. The default is "OFF". 


        Returns:
            bool: The present output setting.
        """
        cmd = f":OUTPut:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_output_state(self, state: Boolean) -> None:
        """
        Disable or enable the front-panel Output connector. The default is "OFF". 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":OUTPut:STATe {state}"
        self._rsrc.write(cmd)


    def get_output_sync_state(self) -> Boolean:
        """
        Disable or enable the front-panel Sync connector. At lower amplitudes, you can reduce output distortion by disabling the Sync signal. 


        Returns:
            bool: The present setting of the Sync signal.
        """
        cmd = f":OUTPut:SYNC:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_output_sync_state(self, state: Boolean) -> None:
        """
        Disable or enable the front-panel Sync connector. At lower amplitudes, you can reduce output distortion by disabling the Sync signal. 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":OUTPut:SYNC:STATe {state}"
        self._rsrc.write(cmd)



    def get_output_trigger_slope(self) -> OutpTrigSlope:
        """
        Select a rising or falling edge for the "trigger out" signal. When enabled using the OUTP:TRIG command (see below), a TTL-compatible square waveform with the specified edge is output from the rear-panel Trig Out connector at the beginning of the sweep or burst. 


        Returns:
            str: The current selection between the rising or falling edge for the "trigger out" signal.
        """
        cmd = f":OUTPut:TRIGger:SLOPe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'slope', 'type_options': ['OutpTrigSlope']}]
    )
    def set_output_trigger_slope(self, slope: OutpTrigSlope) -> None:
        """
        Select a rising or falling edge for the "trigger out" signal. When enabled using the OUTP:TRIG command (see below), a TTL-compatible square waveform with the specified edge is output from the rear-panel Trig Out connector at the beginning of the sweep or burst. 

        Args:
            slope (str): POSitive|NEGative
        """
        cmd = f":OUTPut:TRIGger:SLOPe {slope}"
        self._rsrc.write(cmd)


    def get_output_trigger_state(self) -> Boolean:
        """
        Disable or enable the "trigger out" signal (used for sweep and burst only). When enabled, a TTL-compatible square waveform with the specified edge (OUTP:TRIG:SLOP command) is output from the rear-panel Trig Out connector at the beginning of the sweep or burst. 


        Returns:
            bool: The present setting of the "trigger out" signal.
        """
        cmd = f":OUTPut:TRIGger:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_output_trigger_state(self, state: Boolean) -> None:
        """
        Disable or enable the "trigger out" signal (used for sweep and burst only). When enabled, a TTL-compatible square waveform with the specified edge (OUTP:TRIG:SLOP command) is output from the rear-panel Trig Out connector at the beginning of the sweep or burst. 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":OUTPut:TRIGger:STATe {state}"
        self._rsrc.write(cmd)




    def get_source_am_depth(self) -> float:
        """
        Set the internal modulation depth (or "percent modulation") in percent. 


        Returns:
            float: The present internal modulation depth (or "percent modulation") in percent. 
        """
        cmd = f":SOURce:AM:DEPTh?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'depthInPercent', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_am_depth(self, depthInPercent: Union[float, Minmaxdef]) -> None:
        """
        Set the internal modulation depth (or "percent modulation") in percent. 

        Args:
            depthInPercent (float): 0% to 120%. The default is 100%. MIN = 0%. MAX = 120%. 
        """
        cmd = f":SOURce:AM:DEPTh {depthInPercent}"
        self._rsrc.write(cmd)


    def get_source_am_internal_frequency(self) -> float:
        """
        Set the frequency of the modulating waveform. Used only when the Internal modulation source is selected (AM:SOUR INT command). 


        Returns:
            float: The frequency of the modulating waveform.
        """
        cmd = f":SOURce:AM:INTernal:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_am_internal_frequency(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the frequency of the modulating waveform. Used only when the Internal modulation source is selected (AM:SOUR INT command). 

        Args:
            frequency (float): 2 mHz to 20 kHz. The default is 100 Hz. MIN = 2 mHz. MAX = 20 kHz.
        """
        cmd = f":SOURce:AM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)


    def get_source_am_internal_function_shape(self) -> SourAmIntFuncShape:
        """
        Select the shape of the modulating waveform. Used only when the Internal modulation source is selected (AM:SOUR INT command). 


        Returns:
            str: The shape of the modulating waveform.
        """
        cmd = f":SOURce:AM:INTernal:FUNCtion:SHAPe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'shape', 'type_options': ['SourAmIntFuncShape']}]
    )
    def set_source_am_internal_function_shape(self, shape: SourAmIntFuncShape) -> None:
        """
        Select the shape of the modulating waveform. Used only when the Internal modulation source is selected (AM:SOUR INT command). 

        Args:
            shape (str): SINusoid|SQUare|RAMP|NRAMp|TRIangle|NOISe|USER
        """
        cmd = f":SOURce:AM:INTernal:FUNCtion:SHAPe {shape}"
        self._rsrc.write(cmd)




    def get_source_am_source(self) -> SourAmSource:
        """
        Select the source of the modulating signal. The function generator will accept an internal or external modulation source. 


        Returns:
            str: The source of the modulating signal.
        """
        cmd = f":SOURce:AM:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourAmSource']}]
    )
    def set_source_am_source(self, source: SourAmSource) -> None:
        """
        Select the source of the modulating signal. The function generator will accept an internal or external modulation source. 

        Args:
            source (str): INTernal|EXTernal
        """
        cmd = f":SOURce:AM:SOURce {source}"
        self._rsrc.write(cmd)


    def get_source_am_state(self) -> Boolean:
        """
        Disable or enable AM. To avoid multiple waveform changes, you can enable AM after you have set up the other modulation parameters. 


        Returns:
            bool: The present AM state.
        """
        cmd = f":SOURce:AM:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_source_am_state(self, state: Boolean) -> None:
        """
        Disable or enable AM. To avoid multiple waveform changes, you can enable AM after you have set up the other modulation parameters. 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":SOURce:AM:STATe {state}"
        self._rsrc.write(cmd)



    def get_source_burst_gate_polarity(self) -> SourBursGatePolarity:
        """
        Select whether the function generator uses true-high or true-low logic levels on the rear-panel Trig In connector for an externally-gated burst. 


        Returns:
            str: Returns the current value of whether the function generator uses true-high or true-low logic levels on the rear-panel Trig In connector for an externally-gated burst.
        """
        cmd = f":SOURce:BURSt:GATE:POLarity?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'polarity', 'type_options': ['SourBursGatePolarity']}]
    )
    def set_source_burst_gate_polarity(self, polarity: SourBursGatePolarity) -> None:
        """
        Select whether the function generator uses true-high or true-low logic levels on the rear-panel Trig In connector for an externally-gated burst. 

        Args:
            polarity (str): Whether the function generator uses true-high or true-low logic levels on the rear-panel Trig In connector for an externally-gated burst.
        """
        cmd = f":SOURce:BURSt:GATE:POLarity {polarity}"
        self._rsrc.write(cmd)



    def get_source_burst_internal_period(self) -> float:
        """
        Set the burst period for internally-triggered bursts. 


        Returns:
            float: Returns the current value of the burst period for internally-triggered bursts.
        """
        cmd = f":SOURce:BURSt:INTernal:PERiod?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'period', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_burst_internal_period(self, period: Union[float, Minmaxdef]) -> None:
        """
        Set the burst period for internally-triggered bursts. 

        Args:
            period (float): The burst period for internally-triggered bursts.
        """
        cmd = f":SOURce:BURSt:INTernal:PERiod {period}"
        self._rsrc.write(cmd)



    def get_source_burst_mode(self) -> SourBursMode:
        """
        Select the burst mode.


        Returns:
            str: Returns the current value of the burst mode.
        """
        cmd = f":SOURce:BURSt:MODE?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mode', 'type_options': ['SourBursMode']}]
    )
    def set_source_burst_mode(self, mode: SourBursMode) -> None:
        """
        Select the burst mode.

        Args:
            mode (str): The burst mode.
        """
        cmd = f":SOURce:BURSt:MODE {mode}"
        self._rsrc.write(cmd)


    def get_source_burst_ncycles(self) -> float:
        """
        Set the number of cycles to be output per burst (triggered burst mode only).


        Returns:
            float: Returns the current value of the number of cycles to be output per burst
        """
        cmd = f":SOURce:BURSt:NCYCles?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'cycles', 'type_options': ['float', 'Enumminmaxdefinf']}]
    )
    def set_source_burst_ncycles(self, cycles: Union[float, Enumminmaxdefinf]) -> None:
        """
        Set the number of cycles to be output per burst (triggered burst mode only).

        Args:
            cycles (float): The number of cycles to be output per burst
        """
        cmd = f":SOURce:BURSt:NCYCles {cycles}"
        self._rsrc.write(cmd)


    def get_source_burst_phase(self) -> float:
        """
        Set the starting phase for the burst in degrees or radians as specified by the previous UNIT:ANGL command. 


        Returns:
            float: Returns the current value of the starting phase for the burst in degrees or radians as specified by the previous UNIT:ANGL command.
        """
        cmd = f":SOURce:BURSt:PHASe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'angle', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_burst_phase(self, angle: Union[float, Minmaxdef]) -> None:
        """
        Set the starting phase for the burst in degrees or radians as specified by the previous UNIT:ANGL command. 

        Args:
            angle (float): The starting phase for the burst in degrees or radians as specified by the previous UNIT:ANGL command.
        """
        cmd = f":SOURce:BURSt:PHASe {angle}"
        self._rsrc.write(cmd)


    def get_source_burst_state(self) -> Boolean:
        """
        Disable or enable the burst mode. 


        Returns:
            bool: Returns the current value of the burst mode.
        """
        cmd = f":SOURce:BURSt:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_source_burst_state(self, state: Boolean) -> None:
        """
        Disable or enable the burst mode. 

        Args:
            state (bool): Disable or enable the burst mode.
        """
        cmd = f":SOURce:BURSt:STATe {state}"
        self._rsrc.write(cmd)



    def get_source_fm_deviation(self) -> float:
        """
        Set the peak frequency deviation in hertz. This value represents the peak variation in frequency of the modulated waveform from the carrier frequency. 


        Returns:
            float: The peak frequency deviation in hertz.
        """
        cmd = f":SOURce:FM:DEViation?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'peakDeviationInHz', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_fm_deviation(self, peakDeviationInHz: Union[float, Minmaxdef]) -> None:
        """
        Set the peak frequency deviation in hertz. This value represents the peak variation in frequency of the modulated waveform from the carrier frequency. 

        Args:
            peakDeviationInHz (float): 5 Hz to 40.05 MHz (limited to 550 kHz for ramps and 12.55 MHz for arbitrary waveforms). The default is 100 Hz. MIN = 5 Hz. MAX = based on the frequency of the carrier waveform.
        """
        cmd = f":SOURce:FM:DEViation {peakDeviationInHz}"
        self._rsrc.write(cmd)


    def get_source_fm_internal_frequency(self) -> float:
        """
        Set the frequency of the modulating waveform. Used only when the Internal modulation source is selected (FM:SOUR INT command). 


        Returns:
            float: The frequency of the modulating waveform.
        """
        cmd = f":SOURce:FM:INTernal:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_fm_internal_frequency(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the frequency of the modulating waveform. Used only when the Internal modulation source is selected (FM:SOUR INT command). 

        Args:
            frequency (float): 2 mHz to 20 kHz. The default is 10 Hz. MIN = 2 mHz. MAX = 20 kHz.
        """
        cmd = f":SOURce:FM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)


    def get_source_fm_internal_function_shape(self) -> SourFmIntFuncShape:
        """
        Select the shape of the modulating waveform. Used only when the Internal modulation source is selected (FM:SOUR INT command). 


        Returns:
            str: The shape of the modulating waveform.
        """
        cmd = f":SOURce:FM:INTernal:FUNCtion:SHAPe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'shape', 'type_options': ['SourFmIntFuncShape']}]
    )
    def set_source_fm_internal_function_shape(self, shape: SourFmIntFuncShape) -> None:
        """
        Select the shape of the modulating waveform. Used only when the Internal modulation source is selected (FM:SOUR INT command). 

        Args:
            shape (str): SINusoid|SQUare|RAMP|NRAMp|TRIangle|NOISe|USER
        """
        cmd = f":SOURce:FM:INTernal:FUNCtion:SHAPe {shape}"
        self._rsrc.write(cmd)




    def get_source_fm_source(self) -> SourFmSource:
        """
        Select the source of the modulating signal. The function generator will accept an internal or external modulation source. 


        Returns:
            str: The source of the modulating signal.
        """
        cmd = f":SOURce:FM:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourFmSource']}]
    )
    def set_source_fm_source(self, source: SourFmSource) -> None:
        """
        Select the source of the modulating signal. The function generator will accept an internal or external modulation source. 

        Args:
            source (str): INTernal|EXTernal
        """
        cmd = f":SOURce:FM:SOURce {source}"
        self._rsrc.write(cmd)


    def get_source_fm_state(self) -> Boolean:
        """
        Disable or enable FM. To avoid multiple waveform changes, you can enable FM after you have set up the other modulation parameters. 


        Returns:
            bool: The present FM state.
        """
        cmd = f":SOURce:FM:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_source_fm_state(self, state: Boolean) -> None:
        """
        Disable or enable FM. To avoid multiple waveform changes, you can enable FM after you have set up the other modulation parameters. 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":SOURce:FM:STATe {state}"
        self._rsrc.write(cmd)



    def get_source_frequency_center(self) -> float:
        """
        Set the center frequency (used in conjunction with the frequency span). 


        Returns:
            float: The center frequency (used in conjunction with the frequency span).
        """
        cmd = f":SOURce:FREQuency:CENTer?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_frequency_center(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the center frequency (used in conjunction with the frequency span). 

        Args:
            frequency (float): 1 uHz to 80 MHz (limited to 1 MHz for ramps and 25 MHz for arbitrary waveforms). The default is 550 Hz. MIN = 1 uHz. MAX = based on the frequency span and maximum frequency for the selected function.
        """
        cmd = f":SOURce:FREQuency:CENTer {frequency}"
        self._rsrc.write(cmd)


    def get_source_frequency_cw(self) -> float:
        """
        Set the output frequency. 


        Returns:
            float: The output frequency.
        """
        cmd = f":SOURce:FREQuency:CW?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_frequency_cw(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the output frequency. 

        Args:
            frequency (float): See table for the maximum and minimum frequencies allowed.
        """
        cmd = f":SOURce:FREQuency:CW {frequency}"
        self._rsrc.write(cmd)


    def get_source_frequency_span(self) -> float:
        """
        Set the frequency span (used in conjunction with the center frequency). 


        Returns:
            float: The frequency span (used in conjunction with the center frequency).
        """
        cmd = f":SOURce:FREQuency:SPAN?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_frequency_span(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the frequency span (used in conjunction with the center frequency). 

        Args:
            frequency (float): 0 Hz to 80 MHz (limited to 1 MHz for ramps and 25 MHz for arbitrary waveforms). The default is 900 Hz. MIN = 0 Hz. MAX = based on the center frequency and maximum frequency for the selected function. 
        """
        cmd = f":SOURce:FREQuency:SPAN {frequency}"
        self._rsrc.write(cmd)


    def get_source_frequency_start(self) -> float:
        """
        Set the start frequency (used in conjunction with the stop frequency). 


        Returns:
            float: The start frequency (used in conjunction with the stop frequency).
        """
        cmd = f":SOURce:FREQuency:STARt?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_frequency_start(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the start frequency (used in conjunction with the stop frequency). 

        Args:
            frequency (float): 1 uHz to 80 MHz (limited to 1 MHz for ramps and 25 MHz 
    for arbitrary waveforms). The default is 100 Hz. MIN = 1 uHz. MAX = 80 MHz.
        """
        cmd = f":SOURce:FREQuency:STARt {frequency}"
        self._rsrc.write(cmd)


    def get_source_frequency_stop(self) -> float:
        """
        Set the stop frequency (used in conjunction with the start frequency).


        Returns:
            float: The stop frequency (used in conjunction with the start frequency).
        """
        cmd = f":SOURce:FREQuency:STOP?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_frequency_stop(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the stop frequency (used in conjunction with the start frequency).

        Args:
            frequency (float): 1 uHz to 80 MHz (limited to 1 MHz for ramps and 25 MHz for arbitrary waveforms). The default is 1 kHz. MIN = 1 uHz. MAX = 80 MHz. 
        """
        cmd = f":SOURce:FREQuency:STOP {frequency}"
        self._rsrc.write(cmd)



    def get_source_fskey_frequency(self) -> float:
        """
        Set the FSK alternate (or "hop") frequency. 


        Returns:
            float: The FSK alternate (or "hop") frequency. 
        """
        cmd = f":SOURce:FSKey:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_fskey_frequency(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the FSK alternate (or "hop") frequency. 

        Args:
            frequency (float): 1 uHz to 80 MHz (limited to 1 MHz for ramps and 25 MHz for arbitrary waveforms). The default is 100 Hz. MIN = 1 uHz. MAX = 80 MHz. 
        """
        cmd = f":SOURce:FSKey:FREQuency {frequency}"
        self._rsrc.write(cmd)


    def get_source_fskey_internal_rate(self) -> float:
        """
        Set the rate at which the output frequency "shifts" between the carrier and hop frequency. 


        Returns:
            float: The rate at which the output frequency "shifts" between the carrier and hop frequency.
        """
        cmd = f":SOURce:FSKey:INTernal:RATE?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'rate', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_fskey_internal_rate(self, rate: Union[float, Minmaxdef]) -> None:
        """
        Set the rate at which the output frequency "shifts" between the carrier and hop frequency. 

        Args:
            rate (float): 2 mHz to 100 kHz. The default is 10 Hz. MIN = 2 mHz. MAX = 100 kHz.
        """
        cmd = f":SOURce:FSKey:INTernal:RATE {rate}"
        self._rsrc.write(cmd)



    def get_source_fskey_source(self) -> SourFskSource:
        """
        Select an internal or external FSK source. 


        Returns:
            str: The present selection of the internal or external FSK source.
        """
        cmd = f":SOURce:FSKey:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourFskSource']}]
    )
    def set_source_fskey_source(self, source: SourFskSource) -> None:
        """
        Select an internal or external FSK source. 

        Args:
            source (str): INTernal|EXTernal
        """
        cmd = f":SOURce:FSKey:SOURce {source}"
        self._rsrc.write(cmd)


    def get_source_fskey_state(self) -> Boolean:
        """
        Disable or enable FSK modulation. To avoid multiple waveform changes, you can enable FSK after you have set up the other modulation parameters. 


        Returns:
            bool: The present state of the FSK modulation.
        """
        cmd = f":SOURce:FSKey:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_source_fskey_state(self, state: Boolean) -> None:
        """
        Disable or enable FSK modulation. To avoid multiple waveform changes, you can enable FSK after you have set up the other modulation parameters. 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":SOURce:FSKey:STATe {state}"
        self._rsrc.write(cmd)



    def get_source_function_shape(self) -> SourFuncShape:
        """
        Select the output function. The selected waveform is output using the previously selected frequency, amplitude, and offset voltage settings. 


        Returns:
            str: The output function.
        """
        cmd = f":SOURce:FUNCtion:SHAPe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'function', 'type_options': ['SourFuncShape']}]
    )
    def set_source_function_shape(self, function: SourFuncShape) -> None:
        """
        Select the output function. The selected waveform is output using the previously selected frequency, amplitude, and offset voltage settings. 

        Args:
            function (str): SINusoid|SQUare|RAMP|PULSe|NOISe|DC|USER
        """
        cmd = f":SOURce:FUNCtion:SHAPe {function}"
        self._rsrc.write(cmd)

    def get_source_function_shape_ramp_symmetry(self) -> float:
        """
        Set the symmetry percentage for ramp waves. Symmetry represents the amount of time per cycle that the ramp wave is rising (assuming that the waveform polarity is not inverted). 


        Returns:
            float: The symmetry percentage for ramp waves.
        """
        cmd = f":SOURce:FUNCtion:SHAPe:RAMP:SYMMetry?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'percent', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_function_shape_ramp_symmetry(self, percent: Union[float, Minmaxdef]) -> None:
        """
        Set the symmetry percentage for ramp waves. Symmetry represents the amount of time per cycle that the ramp wave is rising (assuming that the waveform polarity is not inverted). 

        Args:
            percent (float): 0% to 100%. The default is 100%. MIN = 0%. MAX = 100%.
        """
        cmd = f":SOURce:FUNCtion:SHAPe:RAMP:SYMMetry {percent}"
        self._rsrc.write(cmd)



    def get_source_function_shape_square_dcycle(self) -> float:
        """
        Set the duty cycle percentage for square waves. Duty cycle represents the amount of time per cycle that the square wave is at a high level (assuming that the waveform polarity is not inverted). 


        Returns:
            float: The duty cycle percentage for square waves.
        """
        cmd = f":SOURce:FUNCtion:SHAPe:SQUare:DCYCle?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'percent', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_function_shape_square_dcycle(self, percent: Union[float, Minmaxdef]) -> None:
        """
        Set the duty cycle percentage for square waves. Duty cycle represents the amount of time per cycle that the square wave is at a high level (assuming that the waveform polarity is not inverted). 

        Args:
            percent (float): 20% to 80% (frequency < 25 MHz)
    40% to 60% (25 MHz < frequency < 50 MHz)
    50% (frequency > 50 MHz) 
        """
        cmd = f":SOURce:FUNCtion:SHAPe:SQUare:DCYCle {percent}"
        self._rsrc.write(cmd)



    def get_source_function_shape_user(self) -> str:
        """
        Select one of the five built-in arbitrary waveforms, one of four user-defined waveforms, or the waveform currently downloaded to volatile memory. 


        Returns:
            str: "EXP_RISE", "EXP_FALL", "NEG_RAMP", "SINC", "CARDIAC", "VOLATILE", or the name of any user-defined waveforms in non-volatile memory.
        """
        cmd = f":SOURce:FUNCtion:SHAPe:USER?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'arbName', 'type_options': ['str']}]
    )
    def set_source_function_shape_user(self, arbName: str) -> None:
        """
        Select one of the five built-in arbitrary waveforms, one of four user-defined waveforms, or the waveform currently downloaded to volatile memory. 

        Args:
            arbName (str): Select one of the five built-in arbitrary waveforms, one of four user-defined waveforms, or the waveform currently downloaded to volatile memory. 
        """
        cmd = f":SOURce:FUNCtion:SHAPe:USER {arbName}"
        self._rsrc.write(cmd)




    def get_source_marker_frequency(self) -> float:
        """
        Set the marker frequency. This is the frequency at which the signal on the front-panel Sync connector goes to a logic low during the sweep. The Sync signal always goes from low to high at the beginning of the sweep. 


        Returns:
            float: The marker frequency.
        """
        cmd = f":SOURce:MARKer:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_marker_frequency(self, frequency: Union[float, Minmaxdef]) -> None:
        """
        Set the marker frequency. This is the frequency at which the signal on the front-panel Sync connector goes to a logic low during the sweep. The Sync signal always goes from low to high at the beginning of the sweep. 

        Args:
            frequency (float): 1 uHz to 80 MHz (limited to 1 MHz for ramps and 25 MHz for arbitrary waveforms). The default is 500 Hz. MIN = 1 uHz. MAX = the start frequency or stop frequency (whichever is higher).
        """
        cmd = f":SOURce:MARKer:FREQuency {frequency}"
        self._rsrc.write(cmd)


    def get_source_marker_state(self) -> Boolean:
        """
        Disable or enable the frequency marker. When the frequency marker is disabled, the signal output from the Sync connector is the normal Sync signal for the carrier waveform.


        Returns:
            bool: The present state of the frequency marker.
        """
        cmd = f":SOURce:MARKer:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'marker', 'type_options': ['Boolean']}]
    )
    def set_source_marker_state(self, marker: Boolean) -> None:
        """
        Disable or enable the frequency marker. When the frequency marker is disabled, the signal output from the Sync connector is the normal Sync signal for the carrier waveform.

        Args:
            marker (bool): ON | OFF
        """
        cmd = f":SOURce:MARKer:STATe {marker}"
        self._rsrc.write(cmd)



    def get_source_phase_adjust(self) -> float:
        """
        Adjust the phase offset of the output waveform in degrees or radians as specified by the previous UNIT:ANGL command 


        Returns:
            float: The query returns the phase offset in degrees or radians.
        """
        cmd = f":SOURce:PHASe:ADJust?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'angle', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_phase_adjust(self, angle: Union[float, Minmaxdef]) -> None:
        """
        Adjust the phase offset of the output waveform in degrees or radians as specified by the previous UNIT:ANGL command 

        Args:
            angle (float): The phase offset of the output waveform in degrees or radians as specified by the previous UNIT:ANGL command.
        """
        cmd = f":SOURce:PHASe:ADJust {angle}"
        self._rsrc.write(cmd)


    def source_phase_reference(self) -> None:
        """
        Immediately sets a new zero-phase reference point without changing the output of the function generator. That is, this command resets the phase value returned by the PHAS? command but does not affect the output waveform.

        Args:
        """
        cmd = f":SOURce:PHASe:REFerence"
        self._rsrc.write(cmd)


    def get_source_phase_unlock_error_state(self) -> Boolean:
        """
        Disable or enable the function generator from generating an error if the phase-lock is ever lost. 


        Returns:
            bool: The present state of the error generating on the function generator if the phase-lock is ever lost.
        """
        cmd = f":SOURce:PHASe:UNLock:ERRor:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_source_phase_unlock_error_state(self, state: Boolean) -> None:
        """
        Disable or enable the function generator from generating an error if the phase-lock is ever lost. 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":SOURce:PHASe:UNLock:ERRor:STATe {state}"
        self._rsrc.write(cmd)





    def get_source_pulse_period(self) -> float:
        """
        Set the period for pulses. 


        Returns:
            float: The period for pulses.
        """
        cmd = f":SOURce:PULSe:PERiod?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_pulse_period(self, seconds: Union[float, Minmaxdef]) -> None:
        """
        Set the period for pulses. 

        Args:
            seconds (float): 200 ns to 2000 seconds. The default is 1 ms. MIN = 200 ns. MAX = 2000 seconds.
        """
        cmd = f":SOURce:PULSe:PERiod {seconds}"
        self._rsrc.write(cmd)


    def get_source_pulse_width(self) -> float:
        """
        Set the pulse width in seconds. 


        Returns:
            float: Returns the current value of set the pulse width in seconds.
        """
        cmd = f":SOURce:PULSe:WIDTh?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_pulse_width(self, seconds: Union[float, Minmaxdef]) -> None:
        """
        Set the pulse width in seconds. 

        Args:
            seconds (float): Set the pulse width in seconds.
        """
        cmd = f":SOURce:PULSe:WIDTh {seconds}"
        self._rsrc.write(cmd)



    def get_source_sweep_spacing(self) -> SourSweSpacing:
        """
        Select linear or logarithmic spacing for the sweep. 


        Returns:
            str: The present selection of the sweep spacing.
        """
        cmd = f":SOURce:SWEep:SPACing?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'spacing', 'type_options': ['SourSweSpacing']}]
    )
    def set_source_sweep_spacing(self, spacing: SourSweSpacing) -> None:
        """
        Select linear or logarithmic spacing for the sweep. 

        Args:
            spacing (str): LINear|LOGarithmic
        """
        cmd = f":SOURce:SWEep:SPACing {spacing}"
        self._rsrc.write(cmd)


    def get_source_sweep_state(self) -> Boolean:
        """
        Disable or enable the sweep mode. To avoid multiple waveform changes, you can enable the sweep mode after you have set up the other sweep parameters. 


        Returns:
            bool: The present state of the sweep mode.
        """
        cmd = f":SOURce:SWEep:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_source_sweep_state(self, state: Boolean) -> None:
        """
        Disable or enable the sweep mode. To avoid multiple waveform changes, you can enable the sweep mode after you have set up the other sweep parameters. 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":SOURce:SWEep:STATe {state}"
        self._rsrc.write(cmd)


    def get_source_sweep_time(self) -> float:
        """
        Set the number of seconds required to sweep from the start frequency to the stop frequency. 


        Returns:
            float: 1 ms to 500 seconds. The default is 1 second. MIN = 1 ms. MAX = 500 seconds.
        """
        cmd = f":SOURce:SWEep:TIME?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_sweep_time(self, seconds: Union[float, Minmaxdef]) -> None:
        """
        Set the number of seconds required to sweep from the start frequency to the stop frequency. 

        Args:
            seconds (float): The number of seconds required to sweep from the start frequency to the stop frequency.
        """
        cmd = f":SOURce:SWEep:TIME {seconds}"
        self._rsrc.write(cmd)



    def get_source_voltage_level_immediate_amplitude(self) -> float:
        """
        Set the output amplitude. The default amplitude is 100 mVpp (into 50W) for all functions.


        Returns:
            float: The output amplitude.
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:AMPLitude?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'amplitude', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_voltage_level_immediate_amplitude(self, amplitude: Union[float, Minmaxdef]) -> None:
        """
        Set the output amplitude. The default amplitude is 100 mVpp (into 50W) for all functions.

        Args:
            amplitude (float): The default amplitude is 100 mVpp (into 50 Ohms) for all functions. MIN selects the smallest amplitude (1 mVpp into 50 Ohms). MAX selects the largest amplitude for the selected function (at most 10 Vpp into 50 Ohms depending on the selected function and offset voltage). 
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:AMPLitude {amplitude}"
        self._rsrc.write(cmd)


    def get_source_voltage_level_immediate_high(self) -> float:
        """
        Set the high voltage level. 


        Returns:
            float: The high voltage level.
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:HIGH?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'highVoltage', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_voltage_level_immediate_high(self, highVoltage: Union[float, Minmaxdef]) -> None:
        """
        Set the high voltage level. 

        Args:
            highVoltage (float): The default high level is +50 mV. MIN selects the most negative voltage level for the selected function and MAX selects the largest voltage level.
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:HIGH {highVoltage}"
        self._rsrc.write(cmd)


    def get_source_voltage_level_immediate_low(self) -> float:
        """
        Set the low voltage level.


        Returns:
            float: The low voltage level.
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:LOW?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'lowVoltage', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_voltage_level_immediate_low(self, lowVoltage: Union[float, Minmaxdef]) -> None:
        """
        Set the low voltage level.

        Args:
            lowVoltage (float): The default low level is -50 mV. MIN selects the most negative voltage level for the selected function and MAX selects the largest voltage level. 
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:LOW {lowVoltage}"
        self._rsrc.write(cmd)


    def get_source_voltage_level_immediate_offset(self) -> float:
        """
        Set the dc offset voltage. 


        Returns:
            float: The dc offset voltage.
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:OFFSet?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'offset', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_source_voltage_level_immediate_offset(self, offset: Union[float, Minmaxdef]) -> None:
        """
        Set the dc offset voltage. 

        Args:
            offset (float): The default offset is 0 volts for all functions. MIN selects the most negative dc offset voltage for the selected function and amplitude. MAX selects the largest dc offset for the selected function and amplitude.
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:OFFSet {offset}"
        self._rsrc.write(cmd)


    def get_source_voltage_level_immediate_unit_voltage(self) -> SourVoltLevImmUnitVoltage:
        """
        Select the units for output amplitude (does not affect offset voltage or high/low levels).


        Returns:
            str: The units for output amplitude (does not affect offset voltage or high/low levels).
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:UNIT:VOLTage?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'unit', 'type_options': ['SourVoltLevImmUnitVoltage']}]
    )
    def set_source_voltage_level_immediate_unit_voltage(self, unit: SourVoltLevImmUnitVoltage) -> None:
        """
        Select the units for output amplitude (does not affect offset voltage or high/low levels).

        Args:
            unit (str): VPP|VRMS|DBM
        """
        cmd = f":SOURce:VOLTage:LEVel:IMMediate:UNIT:VOLTage {unit}"
        self._rsrc.write(cmd)





    def get_source_voltage_range_auto(self) -> Boolean:
        """
        Disable or enable voltage autoranging for all functions. In the default mode, autoranging is enabled ("ON") and the function generator automatically selects the optimal settings for the output amplifier and attenuators. 


        Returns:
            bool: The present state of the voltage autoranging for all functions.
        """
        cmd = f":SOURce:VOLTage:RANGe:AUTO?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'auto', 'type_options': ['int', 'SourVoltRangAuto']}]
    )
    def set_source_voltage_range_auto(self, auto: Union[int, SourVoltRangAuto]) -> None:
        """
        Disable or enable voltage autoranging for all functions. In the default mode, autoranging is enabled ("ON") and the function generator automatically selects the optimal settings for the output amplifier and attenuators. 

        Args:
            auto (int): OFF|ON|ONCE
        """
        cmd = f":SOURce:VOLTage:RANGe:AUTO {auto}"
        self._rsrc.write(cmd)





    def get_status_questionable_condition(self) -> int:
        """
        Query the condition register in this group. This is a read-only register and bits are not cleared when you read the register. 


        Returns:
            int: A query of this register returns a decimal value which corresponds to the binary-weighted sum of all bits set in the register.
        """
        cmd = f":STATus:QUEStionable:CONDition?"
        response = self._rsrc.query(cmd)
        return int(response)


    def get_status_questionable_enable(self) -> int:
        """
        Enable bits in the enable register in this register group. 


        Returns:
            int: The query returns a decimal value which corresponds to the binary-weighted sum of all bits enabled by the STAT:QUES:ENAB command. 
        """
        cmd = f":STATus:QUEStionable:ENABle?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'enableValue', 'type_options': ['int']}]
    )
    def set_status_questionable_enable(self, enableValue: int) -> None:
        """
        Enable bits in the enable register in this register group. 

        Args:
            enableValue (int): The binary-weighted sum of all bits to be enabled.
        """
        cmd = f":STATus:QUEStionable:ENABle {enableValue}"
        self._rsrc.write(cmd)


    def get_status_questionable_event(self) -> int:
        """
        Query the event register in this register group. 


        Returns:
            int: A query of this register returns a decimal value which corresponds to the binary-weighted sum of all bits set in the register.
        """
        cmd = f":STATus:QUEStionable:EVENt?"
        response = self._rsrc.query(cmd)
        return int(response)



    def status_preset(self) -> None:
        """
        Clear all bits in the Questionable Data enable register and the Standard Operation enable register. 

        Args:
        """
        cmd = f":STATus:PRESet"
        self._rsrc.write(cmd)



    def system_beeper_immediate(self) -> None:
        """
        Issue a single beep immediately. 

        Args:
        """
        cmd = f":SYSTem:BEEPer:IMMediate"
        self._rsrc.write(cmd)


    def get_system_beeper_state(self) -> Boolean:
        """
        Disable or enable the tone heard when an error is generated from the front-panel or over the remote interface. The current selection is stored in non-volatile memory. 


        Returns:
            bool: The present state of the beeper, the tone heard when an error is generated from the front-panel or over the remote interface.
        """
        cmd = f":SYSTem:BEEPer:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_system_beeper_state(self, state: Boolean) -> None:
        """
        Disable or enable the tone heard when an error is generated from the front-panel or over the remote interface. The current selection is stored in non-volatile memory. 

        Args:
            state (bool): ON | OFF
        """
        cmd = f":SYSTem:BEEPer:STATe {state}"
        self._rsrc.write(cmd)



    def get_system_error_next(self) -> int:
        """
        Read and clear one error from the function generator's error queue. A record of up to 20 command syntax or hardware errors can be stored in the error queue.


        Returns:
            int: The number of the error cleared from the error queue.
            str: The text of the error cleared from the error queue.
        """
        cmd = f":SYSTem:ERRor:NEXT?"
        response = self._rsrc.query(cmd)
        return int(response)



    def system_local(self) -> None:
        """
        Sets the instrument state to local (the normal power-on default state). Removes any annunciator and unlocks the front panel keyboard. 

        Args:
        """
        cmd = f":SYSTem:LOCal"
        self._rsrc.write(cmd)


    def system_rwlock(self) -> None:
        """
        Sets the instrument state to remote with lock. Displays the rwl annunciator and locks the keyboard.

        Args:
        """
        cmd = f":SYSTem:RWLock"
        self._rsrc.write(cmd)


    def get_system_version(self) -> str:
        """
        Query the function generator to determine the present SCPI version. 


        Returns:
            str: A string in the form "YYYY.V", where "YYYY" represents the year of the version, and "V" represents a version number for that year (e.g., 1999.0).
        """
        cmd = f":SYSTem:VERSion?"
        response = self._rsrc.query(cmd)
        return response



    def get_data_attribute_average(self) -> float:
        """
        Query the arithmetic average of all data points for the specified arbitrary waveform. 


        Returns:
            float: The arithmetic average of all data points for the specified arbitrary waveform.
        """
        cmd = f":DATA:ATTRibute:AVERage?"
        response = self._rsrc.query(cmd)
        return float(response)


    def get_data_attribute_cfactor(self) -> float:
        """
        Query the crest factor of all data points for the specified arbitrary waveform. Crest factor is the ratio of the peak value to the RMS value of the waveform. 


        Returns:
            float: The crest factor of all data points for the specified arbitrary waveform. Crest factor is the ratio of the peak value to the RMS value of the waveform.
        """
        cmd = f":DATA:ATTRibute:CFACtor?"
        response = self._rsrc.query(cmd)
        return float(response)


    def get_data_attribute_points(self) -> int:
        """
        Query the number of points in the specified arbitrary waveform. 


        Returns:
            int: The number of points in the specified arbitrary waveform.
        """
        cmd = f":DATA:ATTRibute:POINts?"
        response = self._rsrc.query(cmd)
        return int(response)


    def get_data_attribute_ptpeak(self) -> float:
        """
        Query the peak-to-peak value of all data points for the specified arbitrary waveform. 


        Returns:
            float: The peak-to-peak value of all data points for the specified arbitrary waveform.
        """
        cmd = f":DATA:ATTRibute:PTPeak?"
        response = self._rsrc.query(cmd)
        return float(response)



    def get_data_catalog(self) -> str:
        """
        List the names of all waveforms currently available for selection. 


        Returns:
            str: The names of all waveforms currently available for selection.
        """
        cmd = f":DATA:CATalog?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'destinationArbName', 'type_options': ['str']}, {'name': 'volatile', 'type_options': ['TracData']}]
    )
    def set_data_copy(self, destinationArbName: str, volatile: TracData) -> None:
        """
        Copy the waveform from volatile memory to the specified name in 
    non-volatile memory. 

        Args:
            destinationArbName (str): The arb name may contain up to 12 characters. The first character must be a letter (A-Z), but the remaining characters can be numbers (0-9) or the underscore character (" _ "). Blank spaces are not allowed. If you specify a name with more than 12 characters, a "Program mnemonic too long" error is generated.
            volatile (str): VOLATILE
        """
        cmd = f":DATA:COPY {destinationArbName}, {volatile}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'volatile', 'type_options': ['TracData']}, {'name': 'value', 'type_options': ['float']}]
    )
    def set_data_data(self, volatile: TracData, value: float) -> None:
        """
        Download floating-point values from -1 to +1 into volatile memory. You can download from 1 to 65,536 (64K) points per waveform. The function generator takes the specified number of points and expands them to fill waveform memory. 

        Args:
            volatile (str): VOLATILE
            value (float): The values -1 and +1 correspond to the peak values of the waveform (if the offset is 0 volts). For example, if you set the amplitude to 10 Vpp (0V offset), "+1" corresponds to +5V and "-1" corresponds to -5V. (Repeatable: *)
        """
        cmd = f":DATA:DATA {volatile}, {value}"
        self._rsrc.write(cmd)

    @overload
    def set_data_data_dac(self, syntax: DataDataDacSyntax.VALUELIST, volatile: TracDataDac, value: int) -> None:
        ...

    @overload
    def set_data_data_dac(self, syntax: DataDataDacSyntax.BINARYBLOCK, volatile: TracDataDac, value: Union[bytes] | None) -> None:
        ...

    @validate_parameters(
        rules_list=[{'name': 'syntax', 'type_options': ['DataDataDacSyntax']}, {'name': 'volatile', 'type_options': ['TracDataDac']}, {'name': 'value', 'type_options': ['int']}, {'name': 'data', 'type_options': ['Any']}]
    )
    def set_data_data_dac(self, syntax: DataDataDacSyntax, volatile: TracDataDac, value: int, data: Any) -> None:
        """
        Download binary or decimal integer values from -8191 to +8191 into volatile memory. 

        Args:
            syntax (DataDataDacSyntax): The syntax variant to use for this command

            For syntax ValueList:
                volatile (str): VOLATILE
                value (int): The values -2047 and +2047 correspond to the peak values of the waveform (if the offset is 0 volts). For example, if you set the output amplitude to 10 Vpp, "+2047" corresponds to +5V and "-2047" corresponds to -5V.  (Repeatable: *)

            For syntax BinaryBlock:
                volatile (str): VOLATILE
                value (Union[bytes] | None): The values -2047 and +2047 correspond to the peak values of the waveform (if the offset is 0 volts). For example, if you set the output amplitude to 10 Vpp, "+2047" corresponds to +5V and "-2047" corresponds to -5V. 
        """
        match syntax:
            case DataDataDacSyntax.VALUELIST:
                cmd = f":DATA:DATA:DAC {volatile}, {value}, {data}"

                self._rsrc.write(cmd)
            case DataDataDacSyntax.BINARYBLOCK:
                cmd = f":DATA:DATA:DAC {volatile}, {value}, {data}"

                self._rsrc.write(cmd)
            case _:
                raise ValueError(f"Unsupported syntax '{syntax}' for command set_data_data_dac.")



    def data_delete_all(self) -> None:
        """
        Delete all user-defined arbitrary waveforms from memory. This command deletes the waveform in volatile memory and all user-defined waveforms in non-volatile memory. The five built-in waveforms in non-volatile memory are not deleted. 

        Args:
        """
        cmd = f":DATA:DELete:ALL"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'arbName', 'type_options': ['str']}]
    )
    def set_data_delete_name(self, arbName: str) -> None:
        """
        Delete the specified arbitrary waveform from memory. You can delete the waveform in volatile memory or any of the four user-defined waveforms in non-volatile memory. 

        Args:
            arbName (str): The name of the arbitrary waveform to be deleted from memory. You can delete the waveform in volatile memory or any of the four user-defined waveforms in non-volatile memory. 
        """
        cmd = f":DATA:DELete:NAME {arbName}"
        self._rsrc.write(cmd)



    def get_data_nvolatile_catalog(self) -> str:
        """
        List the names of all user-defined arbitrary waveforms downloaded to non-volatile memory. Returns the names of up to four waveforms. 


        Returns:
            str: The names of all user-defined arbitrary waveforms downloaded to non-volatile memory. 
        """
        cmd = f":DATA:NVOLatile:CATalog?"
        response = self._rsrc.query(cmd)
        return response


    def get_data_nvolatile_free(self) -> int:
        """
        Query the number of non-volatile memory slots available to store user-defined waveforms. Returns the number of memory slots available to store user-defined waveforms.


        Returns:
            int: The number of non-volatile memory slots available to store user-defined waveforms.
        """
        cmd = f":DATA:NVOLatile:FREE?"
        response = self._rsrc.query(cmd)
        return int(response)




    def get_trigger_sequence_delay(self) -> float:
        """
        Insert a time delay between the receipt of the trigger and the start of the burst waveform 


        Returns:
            float: Returns the current value of the time delay between the receipt of the trigger and the start of the burst waveform.
        """
        cmd = f":TRIGger:SEQuence:DELay?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'Minmaxdef']}]
    )
    def set_trigger_sequence_delay(self, seconds: Union[float, Minmaxdef]) -> None:
        """
        Insert a time delay between the receipt of the trigger and the start of the burst waveform 

        Args:
            seconds (float): The time delay between the receipt of the trigger and the start of the burst waveform.
        """
        cmd = f":TRIGger:SEQuence:DELay {seconds}"
        self._rsrc.write(cmd)


    def trigger_sequence_immediate(self) -> None:
        """
        Trigger a sweep or burst from the remote interface. This command can be used with any of the available trigger sources (TRIG:SOUR command). 

        Args:
        """
        cmd = f":TRIGger:SEQuence:IMMediate"
        self._rsrc.write(cmd)


    def get_trigger_sequence_slope(self) -> TrigSeqSlope:
        """
        Select whether the function generator uses the rising edge or falling edge of the trigger signal on the rear-panel Trig In connector. 


        Returns:
            str: Whether the function generator uses the rising edge or falling edge of the trigger signal on the rear-panel Trig In connector for an externally-triggered sweep.
        """
        cmd = f":TRIGger:SEQuence:SLOPe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'slope', 'type_options': ['TrigSeqSlope']}]
    )
    def set_trigger_sequence_slope(self, slope: TrigSeqSlope) -> None:
        """
        Select whether the function generator uses the rising edge or falling edge of the trigger signal on the rear-panel Trig In connector. 

        Args:
            slope (str): POSitive|NEGative
        """
        cmd = f":TRIGger:SEQuence:SLOPe {slope}"
        self._rsrc.write(cmd)


    def get_trigger_sequence_source(self) -> TrigSeqSource:
        """
        Select the source from which the function generator will accept a trigger. 


        Returns:
            str: The source from which the function generator will accept a trigger.
        """
        cmd = f":TRIGger:SEQuence:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['TrigSeqSource']}]
    )
    def set_trigger_sequence_source(self, source: TrigSeqSource) -> None:
        """
        Select the source from which the function generator will accept a trigger. 

        Args:
            source (str): IMMediate|EXTernal|BUS
        """
        cmd = f":TRIGger:SEQuence:SOURce {source}"
        self._rsrc.write(cmd)




    def get_unit_angle(self) -> UnitAngle:
        """
        Select degrees or radians to set the phase offset value using the PHAS command (remote interface only). 


        Returns:
            str: Degrees or radians to set the starting phase for the burst with the BURS:PHAS command (remote interface only).
        """
        cmd = f":UNIT:ANGLe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'angle', 'type_options': ['UnitAngle']}]
    )
    def set_unit_angle(self, angle: UnitAngle) -> None:
        """
        Select degrees or radians to set the phase offset value using the PHAS command (remote interface only). 

        Args:
            angle (str): DEGree|RADian
        """
        cmd = f":UNIT:ANGLe {angle}"
        self._rsrc.write(cmd)




# For basic testing or example usage:
if __name__ == '__main__':
    # This section is for demonstration and won't run in a typical import scenario.
    # To use the driver:
    # 1. Ensure you have a VISA backend installed (e.g., NI-VISA, pyvisa-py).
    # 2. Connect your instrument.
    # 3. Instantiate the class:
    #    instrument = Keysight33250A(visa_address='YOUR_INSTRUMENT_VISA_ADDRESS')
    #    # Example: instrument = Keysight33250A(visa_address='GPIB0::10::INSTR')
    #
    # 4. Call methods:
    #    # idn = instrument.get_idn() # If *IDN? is defined and generates get_idn()
    #    # print(idn)
    #    # instrument.set_output1_function(Output1Function.SIN) # Example assuming such methods
    
    print(f"Class 'Keysight33250A' is defined in this file.")
    print(f"To use it, import it into your script and instantiate with a VISA address.")