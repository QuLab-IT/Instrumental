from enum import Enum
from typing import Any, Union, overload, List, Dict, Optional, Tuple
import numpy as np
from numpy.typing import NDArray # Included if any type hints might resolve to NDArray
import pyvisa # Generally not directly used if VisaMixin handles all rsrc interactions

from instrumental.drivers import VisaMixin
from instrumental.drivers.funcgenerators import FunctionGenerator # Assuming this is the correct base class
import functools
import inspect
from enum import Enum
from typing import Any, Callable, Dict, List, Union # Added for type hints

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
                print(f"param_name: {param_name}, arg_value: {arg_value}")
                if param_name == 'self':
                    continue

                if isinstance(arg_value, Enum):
                    # print("Is Enum")
                    # bound_args.arguments[param_name] = arg_value.name
                    rule = param_rules.get(param_name)
                    if rule:
                        type_options = rule.get('type_options', [])
                        enum_type_name = type(arg_value).__name__
                        
                        is_enum_in_options = enum_type_name in type_options
                        is_mixed_union = len(type_options) > 1 

                        if is_enum_in_options and is_mixed_union and hasattr(arg_value, 'value'):
                            non_enum_type_in_options = False
                            for opt_str in type_options:
                                if _BASIC_TYPE_MAP.get(opt_str):
                                    non_enum_type_in_options = True
                                    break
                            
                            if non_enum_type_in_options:
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


class DispWindFocus(Enum):
    """
    Enum for disp_wind_focus
    """

    CH1 = '0'
    CH2 = '1'


class DispWindUnitArbrate(Enum):
    """
    Enum for disp_wind_unit_arbrate
    """

    SRATE = '0'
    FREQUENCY = '1'
    PERIOD = '2'


class DispWindUnitPulse(Enum):
    """
    Enum for disp_wind_unit_pulse
    """

    WIDTH = '0'
    DUTY = '1'


class DispWindUnitRate(Enum):
    """
    Enum for disp_wind_unit_rate
    """

    FREQUENCY = '0'
    PERIOD = '1'


class DispWindUnitSweep(Enum):
    """
    Enum for disp_wind_unit_sweep
    """

    STARTSTOP = '0'
    CENTERSPAN = '1'


class DispWindUnitVoltage(Enum):
    """
    Enum for disp_wind_unit_voltage
    """

    AMPLITUDEOFF = '0'
    HIGHLOW = '1'


class DispWindView(Enum):
    """
    Enum for disp_wind_view
    """

    STANDARD = '0'
    TEXT = '1'
    GRAPH = '2'
    DUAL = '3'


class Enumminmaxdef(Enum):
    """
    Enum for enumMinMaxDef
    """

    MINIMUM = '1'
    MAXIMUM = '2'


class Enumminmaxdefinf(Enum):
    """
    Enum for enumMinMaxDefInf
    """

    MINIMUM = '1'
    MAXIMUM = '2'
    INFINITY = '7'


class Enumstaticcurrent(Enum):
    """
    Enum for enumStaticCurrent
    """

    STATIC = '0'
    CURRENT = '1'


class FormBorder(Enum):
    """
    Enum for form_border
    """

    NORMAL = '0'
    SWAPPED = '1'


class HcopSdumDataFormat(Enum):
    """
    Enum for hcop_sdum_data_format
    """

    BMP = '0'
    PNG = '1'


class OutpMode(Enum):
    """
    Enum for outp_mode
    """

    NORMAL = '0'
    GATED = '1'


class OutpPolarity(Enum):
    """
    Enum for outp_polarity
    """

    NORMAL = '0'
    INVERTED = '1'


class OutpSyncMode(Enum):
    """
    Enum for outp_sync_mode
    """

    NORMAL = '0'
    CARRIER = '1'
    MARKER = '2'


class OutpSyncPolarity(Enum):
    """
    Enum for outp_sync_polarity
    """

    NORMAL = '0'
    INVERTED = '1'


class OutpSyncSource(Enum):
    """
    Enum for outp_sync_source
    """

    CH1 = '0'
    CH2 = '1'


class OutpTrigSlope(Enum):
    """
    Enum for outp_trig_slope
    """

    POSITIVE = '1'
    NEGATIVE = '2'


class OutpTrigSource(Enum):
    """
    Enum for outp_trig_source
    """

    CH1 = '0'
    CH2 = '1'


class SourAmIntFuncShapeclone(Enum):
    """
    Enum for sour_am_int_func_shapeClone
    """

    SINUSOID = '0'
    SQUARE = '1'
    TRIANGLE = '2'
    RAMP = '3'
    NRAMP = '4'
    NOISE = '5'
    PRBS = '6'
    ARB = '7'


class SourAmSource(Enum):
    """
    Enum for sour_am_source
    """

    INTERNAL = '0'
    EXTERNAL = '1'
    CH1 = '2'
    CH2 = '3'


class SourAmSourceclone(Enum):
    """
    Enum for sour_am_sourceClone
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


class SourCombFeed(Enum):
    """
    Enum for sour_comb_feed
    """

    CH1 = '0'
    CH2 = '1'
    NONE = '2'


class SourFmSource(Enum):
    """
    Enum for sour_fm_source
    """

    INTERNAL = '0'
    EXTERNAL = '1'
    CH1 = '2'
    CH2 = '3'


class SourFreqCoupMode(Enum):
    """
    Enum for sour_freq_coup_mode
    """

    OFFSET = '0'
    RATIO = '1'


class SourFreqMode(Enum):
    """
    Enum for sour_freq_mode
    """

    FIXED = '0'
    SWEEP = '2'
    CW = '3'
    LIST = '4'


class SourFuncShapArbAdvance(Enum):
    """
    Enum for sour_func_shap_arb_advance
    """

    TRIGGER = '0'
    SRATE = '1'


class SourFuncShapArbFilter(Enum):
    """
    Enum for sour_func_shap_arb_filter
    """

    OFF = '0'
    NORMAL = '1'
    STEP = '2'


class SourFuncShapPrbsData(Enum):
    """
    Enum for sour_func_shap_prbs_data
    """

    PN7 = '0'
    PN9 = '1'
    PN11 = '2'
    PN15 = '3'
    PN20 = '4'
    PN23 = '5'


class SourFuncShapPulsHold(Enum):
    """
    Enum for sour_func_shap_puls_hold
    """

    WIDTH = '0'
    DCYCLE = '1'


class SourFuncShapeclone(Enum):
    """
    Enum for sour_func_shapeClone
    """

    SINUSOID = '0'
    SQUARE = '1'
    RAMP = '2'
    PULSE = '3'
    ARB = '4'
    TRIANGLE = '5'
    NOISE = '6'
    PRBS = '7'
    DC = '8'


class SourPmSource(Enum):
    """
    Enum for sour_pm_source
    """

    INTERNAL = '0'
    EXTERNAL = '1'
    CH1 = '2'
    CH2 = '3'


class SourPwmSource(Enum):
    """
    Enum for sour_pwm_source
    """

    INTERNAL = '0'
    EXTERNAL = '1'
    CH1 = '2'
    CH2 = '3'


class SourRateCoupMode(Enum):
    """
    Enum for sour_rate_coup_mode
    """

    OFFSET = '0'
    RATIO = '1'


class SourRoscSourAuto(Enum):
    """
    Enum for sour_rosc_sour_auto
    """

    OFF = '0'
    ON = '1'


class SourRoscSourCurrent(Enum):
    """
    Enum for sour_rosc_sour_current
    """

    INTERNAL = '0'
    EXTERNAL = '1'


class SourRoscSource(Enum):
    """
    Enum for sour_rosc_source
    """

    INTERNAL = '0'
    EXTERNAL = '1'


class SourSumIntFunctionclone(Enum):
    """
    Enum for sour_sum_int_functionClone
    """

    SINUSOID = '0'
    SQUARE = '1'
    TRIANGLE = '2'
    RAMP = '3'
    NRAMP = '4'
    NOISE = '5'
    PRBS = '6'
    ARB = '7'


class SourSweSpacing(Enum):
    """
    Enum for sour_swe_spacing
    """

    LINEAR = '0'
    LOGARITHMIC = '1'


class SourTrack(Enum):
    """
    Enum for sour_track
    """

    OFF = '0'
    ON = '1'
    INVERTED = '2'


class SourVoltLevUnit(Enum):
    """
    Enum for sour_volt_lev_unit
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


class SourceDataArb2Format(Enum):
    """
    Enum for source_data_arb2_format
    """

    AABB = '0'
    ABAB = '1'


class StdNumEnums(Enum):
    """
    Enum for std_num_enums
    """

    MINIMUM = '1'
    MAXIMUM = '2'


class StdNumEnums1(Enum):
    """
    Enum for std_num_enums1
    """

    MINIMUM = '1'
    MAXIMUM = '2'
    DEFAULT = '3'


class StdNumEnumsDef(Enum):
    """
    Enum for std_num_enums_DEF
    """

    DEFAULT = '3'


class SystCommEnableCommandParameter2clone(Enum):
    """
    Enum for syst_comm_enable_command_parameter_2Clone
    """

    GPIB = '0'
    USB = '1'
    LAN = '2'
    SOCKETS = '3'
    TELNET = '4'
    VXI11 = '5'
    WEB = '6'


class SystLicsDel(Enum):
    """
    Enum for syst_lics_del
    """

    SEC = '0'
    IQP = '1'
    MEM = '2'
    BW30 = '3'


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
    TIMER = '3'


class UnitAngleclone(Enum):
    """
    Enum for unit_angleClone
    """

    DEGREE = '0'
    RADIAN = '1'
    SECOND = '2'
    DEFAULT = '3'


# --- Command Syntax Enums ---
class SourceDataArbitrary2DacSyntax(Enum):
    """
    Enum for command syntaxes of SOURce:DATA:ARBitrary2:DAC
    """
    ASCII = "Ascii"
    BLOCKINT16 = "BlockInt16"


class SourceDataArbitrary2Syntax(Enum):
    """
    Enum for command syntaxes of SOURce:DATA:ARBitrary2
    """
    BLOCKREAL32 = "BlockReal32"
    ASCII = "Ascii"


class SourceDataArbitraryDacSyntax(Enum):
    """
    Enum for command syntaxes of SOURce:DATA:ARBitrary:DAC
    """
    ASCII = "Ascii"
    BLOCKINT16 = "BlockInt16"


class SourceDataArbitrarySyntax(Enum):
    """
    Enum for command syntaxes of SOURce:DATA:ARBitrary
    """
    BLOCKREAL32 = "BlockReal32"
    ASCII = "Ascii"



# --- Validator Decorator Definition ---


# --- Main Instrument Class ---
class Keysight33500B(FunctionGenerator, VisaMixin):
    """Main class for controlling the Keysight 33500B function generators.
    
    This class is auto-generated from an SDL file.
    """
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('Agilent Technologies', ('33521B', '33522B', '33519B', '33520B', '33511B', '33512B', '33510B', '33611A', '33612A', '33621A', '33622A', '33509B'))

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
        Clears the event registers in all register groups. Also clears the error queue.

        Args:
        """
        cmd = f"*CLS"
        self._rsrc.write(cmd)

    def get_ese(self) -> int:
        """
        Enables bits in the enable register for the Standard Event Register group.


        Returns:
            int: Returns the current value of enables bits in the enable register for the Standard Event Register group.
        """
        cmd = f"*ESE?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'enable_value', 'type_options': ['int']}]
    )
    def set_ese(self, enable_value: int) -> None:
        """
        Enables bits in the enable register for the Standard Event Register group.

        Args:
            enable_value (int): Enables bits in the enable register for the Standard Event Register group.
        """
        cmd = f"*ESE {enable_value}"
        self._rsrc.write(cmd)

    def get_esr(self) -> int:
        """
        Standard Event Status Register Query. Queries the event register for the Standard Event Register group. 


        Returns:
            int: the event register for the Standard Event Register group.
        """
        cmd = f"*ESR?"
        response = self._rsrc.query(cmd)
        return int(response)

    def get_idn(self) -> str:
        """
        instrument’s identification string.


        Returns:
            str: Instrument’s identification string.
        """
        cmd = f"*IDN?"
        response = self._rsrc.query(cmd)
        return response

    def get_opc(self) -> int:
        """
        Sets "Operation Complete" (bit 0) in the Standard Event register at the completion of the current operation. Returns 1 to the output buffer after all pending commands complete.


        Returns:
            int: Returns returns "1" to the output buffer when the current operation completes.
        """
        cmd = f"*OPC?"
        response = self._rsrc.query(cmd)
        return int(response)

    def opc(self) -> None:
        """
        Sets "Operation Complete" (bit 0) in the Standard Event register at the completion of the current operation. Returns 1 to the output buffer after all pending commands complete.

        Args:
        """
        cmd = f"*OPC"
        self._rsrc.write(cmd)

    def get_opt(self) -> str:
        """
        Returns a quoted string identifying any installed options.


        Returns:
            str: Returns a quoted string identifying any installed options.
        """
        cmd = f"*OPT?"
        response = self._rsrc.query(cmd)
        return response

    def get_psc(self) -> Boolean:
        """
        Power-On Status Clear. Enables (1) or disables (0) clearing of two specific registers at power on.


        Returns:
            int: Returns the current state of the Power-On Status Clear.
        """
        cmd = f"*PSC?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'psc', 'type_options': ['int']}]
    )
    def set_psc(self, psc: int) -> None:
        """
        Power-On Status Clear. Enables (1) or disables (0) clearing of two specific registers at power on.

        Args:
            psc (int): 0|1.
        """
        cmd = f"*PSC {psc}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'rcl', 'type_options': ['int']}]
    )
    def set_rcl(self, rcl: int) -> None:
        """
        Recalls (*RCL) instrument state in specified non-volatile location.

        Args:
            rcl (int): 0|1|2|3|4.
        """
        cmd = f"*RCL {rcl}"
        self._rsrc.write(cmd)

    def rst(self) -> None:
        """
        Resets instrument to factory default state.

        Args:
        """
        cmd = f"*RST"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'sav', 'type_options': ['int']}]
    )
    def set_sav(self, sav: int) -> None:
        """
        saves (*SAV) instrument state in specified non-volatile location. 

        Args:
            sav (int): 0|1|2|3|4.
        """
        cmd = f"*SAV {sav}"
        self._rsrc.write(cmd)

    def get_sre(self) -> int:
        """
        Service Request Enable. This command enables bits in the enable register for the Status Byte Register group.


        Returns:
            int: Returns the current value of enable bits in the enable register for the Status Byte Register group.
        """
        cmd = f"*SRE?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'enable_value', 'type_options': ['int']}]
    )
    def set_sre(self, enable_value: int) -> None:
        """
        Service Request Enable. This command enables bits in the enable register for the Status Byte Register group.

        Args:
            enable_value (int): Enable bits in the enable register for the Status Byte Register group.
        """
        cmd = f"*SRE {enable_value}"
        self._rsrc.write(cmd)

    def get_stb(self) -> int:
        """
        Read Status Byte Query. This command queries the condition register for the Status Byte Register group.


        Returns:
            int: Returns the condition register for the Status Byte Register group.
        """
        cmd = f"*STB?"
        response = self._rsrc.query(cmd)
        return int(response)

    def trg(self) -> None:
        """
        Trigger Command. Triggers a sweep, burst, arbitrary waveform advance, or LIST advance from the remote interface if the bus (software) trigger source is currently selected.

        Args:
        """
        cmd = f"*TRG"
        self._rsrc.write(cmd)

    def get_tst(self) -> int:
        """
        Self-Test Query. Performs a complete instrument self-test.


        Returns:
            int: Returns the results of the self-test.
        """
        cmd = f"*TST?"
        response = self._rsrc.query(cmd)
        return int(response)

    def wai(self) -> None:
        """
        Configures the instrument to wait for all pending operations to complete before executing any additional commands over the interface.

        Args:
        """
        cmd = f"*WAI"
        self._rsrc.write(cmd)

    # --- Subsystem Commands ---
    def abort(self) -> None:
        """
        Halts a sequence, list, sweep, or burst, even an infinite burst. 

        Args:
        """
        cmd = f":ABORt"
        self._rsrc.write(cmd)


    def get_calibration_all(self) -> int:
        """
        Performs a calibration using the calibration value (CALibration:VALue). 


        Returns:
            int: Returns the result of the calibration test.
        """
        cmd = f":CALibration:ALL?"
        response = self._rsrc.query(cmd)
        return int(response)


    def get_calibration_count(self) -> int:
        """
        Returns the number of calibrations performed.


        Returns:
            int: Return the calibration count
        """
        cmd = f":CALibration:COUNt?"
        response = self._rsrc.query(cmd)
        return int(response)


    @validate_parameters(
        rules_list=[{'name': 'new_code', 'type_options': ['str']}]
    )
    def set_calibration_secure_code(self, new_code: str) -> None:
        """
        Sets the security code to prevent unauthorized calibrations.

        Args:
            new_code (str): The new security code.
        """
        cmd = f":CALibration:SECure:CODE {new_code}"
        self._rsrc.write(cmd)


    def get_calibration_secure_state(self) -> Boolean:
        """
        Unsecures or secures the instrument for calibration. 


        Returns:
            bool: Returns the current state of the instrument for calibration.
        """
        cmd = f":CALibration:SECure:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'code', 'type_options': ['str']}]
    )
    def set_calibration_secure_state(self, state: Boolean, code: str) -> None:
        """
        Unsecures or secures the instrument for calibration. 

        Args:
            state (bool): ON|1|OFF|0.
            code (str): Security Code
        """
        cmd = f":CALibration:SECure:STATe {state}, {code}"
        self._rsrc.write(cmd)



    def get_calibration_setup(self) -> int:
        """
        Configures the calibration step (default 1) to be performed. 


        Returns:
            int: Returns the current calibration step number.
        """
        cmd = f":CALibration:SETup?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'step', 'type_options': ['int']}]
    )
    def set_calibration_setup(self, step: int) -> None:
        """
        Configures the calibration step (default 1) to be performed. 

        Args:
            step (int): The calibration step number.
        """
        cmd = f":CALibration:SETup {step}"
        self._rsrc.write(cmd)


    def get_calibration_string(self) -> str:
        """
        Stores a message of up to 40 characters in calibration memory.


        Returns:
            str: Returns the current message to be stored in the calibration memory.
        """
        cmd = f":CALibration:STRing?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'string', 'type_options': ['str']}]
    )
    def set_calibration_string(self, string: str) -> None:
        """
        Stores a message of up to 40 characters in calibration memory.

        Args:
            string (str): Message to be stored in the calibration memory.
        """
        cmd = f":CALibration:STRing {string}"
        self._rsrc.write(cmd)


    def get_calibration_value(self) -> float:
        """
        Specifies the value of the known calibration signal.


        Returns:
            float: Returns the calibration value.
        """
        cmd = f":CALibration:VALue?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'value', 'type_options': ['float']}]
    )
    def set_calibration_value(self, value: float) -> None:
        """
        Specifies the value of the known calibration signal.

        Args:
            value (float): The calibration value.
        """
        cmd = f":CALibration:VALue {value}"
        self._rsrc.write(cmd)



    def get_display(self) -> Boolean:
        """
        Disables or enables the front-panel display.


        Returns:
            bool: Returns the current state of the front-panel display.
        """
        cmd = f":DISPlay?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_display(self, state: Boolean) -> None:
        """
        Disables or enables the front-panel display.

        Args:
            state (bool): ON|1|OFF|0.
        """
        cmd = f":DISPlay {state}"
        self._rsrc.write(cmd)

    def get_display_focus(self) -> DispWindFocus:
        """
        selects the channel displayed "in front" on a two-channel instrument 


        Returns:
            str: Returns the current selected the channel that is displayed "in front" on a two-channel instrument.
        """
        cmd = f":DISPlay:FOCus?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'focus', 'type_options': ['DispWindFocus']}]
    )
    def set_display_focus(self, focus: DispWindFocus) -> None:
        """
        selects the channel displayed "in front" on a two-channel instrument 

        Args:
            focus (str): Selects the channel that is displayed "in front" on a two-channel instrument.
        """
        cmd = f":DISPlay:FOCus {focus}"
        self._rsrc.write(cmd)


    def get_display_text(self) -> str:
        """
        Displays a text message on the front-panel display.   


        Returns:
            str: Returns the current text message on the front-panel display.
        """
        cmd = f":DISPlay:TEXT?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'string', 'type_options': ['str']}]
    )
    def set_display_text(self, string: str) -> None:
        """
        Displays a text message on the front-panel display.   

        Args:
            string (str): Displays a text message on the front-panel display.
        """
        cmd = f":DISPlay:TEXT {string}"
        self._rsrc.write(cmd)

    def display_text_clear(self) -> None:
        """
        Clears the text message from the front-panel display.

        Args:
        """
        cmd = f":DISPlay:TEXT:CLEar"
        self._rsrc.write(cmd)



    def get_display_unit_arbrate(self) -> DispWindUnitArbrate:
        """
        Specifies whether the rate units for arbitrary waveforms are samples per second, (SRATe), Hz (FREQ) or seconds (PER).


        Returns:
            str: Returns the current units for arbitrary waveforms.
        """
        cmd = f":DISPlay:UNIT:ARBRate?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'arbrate', 'type_options': ['DispWindUnitArbrate']}]
    )
    def set_display_unit_arbrate(self, arbrate: DispWindUnitArbrate) -> None:
        """
        Specifies whether the rate units for arbitrary waveforms are samples per second, (SRATe), Hz (FREQ) or seconds (PER).

        Args:
            arbrate (str): SRATe|FREQuency|PERiod
        """
        cmd = f":DISPlay:UNIT:ARBRate {arbrate}"
        self._rsrc.write(cmd)


    def get_display_unit_pulse(self) -> DispWindUnitPulse:
        """
        Selects the method for specifying pulse duration.


        Returns:
            str: Returns the current method for specifying pulse duration.
        """
        cmd = f":DISPlay:UNIT:PULSe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'pulse', 'type_options': ['DispWindUnitPulse']}]
    )
    def set_display_unit_pulse(self, pulse: DispWindUnitPulse) -> None:
        """
        Selects the method for specifying pulse duration.

        Args:
            pulse (str): WIDTh|DUTY.
        """
        cmd = f":DISPlay:UNIT:PULSe {pulse}"
        self._rsrc.write(cmd)


    def get_display_unit_rate(self) -> DispWindUnitRate:
        """
        Specifies whether the rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).


        Returns:
            str: Returns the current rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).
        """
        cmd = f":DISPlay:UNIT:RATE?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'rate', 'type_options': ['DispWindUnitRate']}]
    )
    def set_display_unit_rate(self, rate: DispWindUnitRate) -> None:
        """
        Specifies whether the rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).

        Args:
            rate (str): FREQuency|PERiod.
        """
        cmd = f":DISPlay:UNIT:RATE {rate}"
        self._rsrc.write(cmd)


    def get_display_unit_sweep(self) -> DispWindUnitSweep:
        """
        Selects the method for specifying sweep frequency range.


        Returns:
            str: Returns the current method for specifying sweep frequency range.
        """
        cmd = f":DISPlay:UNIT:SWEep?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'sweep', 'type_options': ['DispWindUnitSweep']}]
    )
    def set_display_unit_sweep(self, sweep: DispWindUnitSweep) -> None:
        """
        Selects the method for specifying sweep frequency range.

        Args:
            sweep (str): STARtstop|CENTerspan.
        """
        cmd = f":DISPlay:UNIT:SWEep {sweep}"
        self._rsrc.write(cmd)


    def get_display_unit_voltage(self) -> DispWindUnitVoltage:
        """
        Selects the method for specifying voltage ranges.


        Returns:
            str: Returns the current method for specifying voltage ranges.
        """
        cmd = f":DISPlay:UNIT:VOLTage?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'voltage', 'type_options': ['DispWindUnitVoltage']}]
    )
    def set_display_unit_voltage(self, voltage: DispWindUnitVoltage) -> None:
        """
        Selects the method for specifying voltage ranges.

        Args:
            voltage (str): AMPLitudeoffset|HIGHlow.
        """
        cmd = f":DISPlay:UNIT:VOLTage {voltage}"
        self._rsrc.write(cmd)



    def get_display_view(self) -> DispWindView:
        """
        Selects the screen layout.


        Returns:
            str: Returns the current screen layout.
        """
        cmd = f":DISPlay:VIEW?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'view', 'type_options': ['DispWindView']}]
    )
    def set_display_view(self, view: DispWindView) -> None:
        """
        Selects the screen layout.

        Args:
            view (str): STANdard|TEXT|GRAPh|DUAL.
        """
        cmd = f":DISPlay:VIEW {view}"
        self._rsrc.write(cmd)



    def get_format_border(self) -> FormBorder:
        """
        Sets the byte order used in binary data point transfers in the block mode.


        Returns:
            str: Returns the current byte order.
        """
        cmd = f":FORMat:BORDer?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'border', 'type_options': ['FormBorder']}]
    )
    def set_format_border(self, border: FormBorder) -> None:
        """
        Sets the byte order used in binary data point transfers in the block mode.

        Args:
            border (str): NORMal|SWAPped.
        """
        cmd = f":FORMat:BORDer {border}"
        self._rsrc.write(cmd)



    def get_hcopy_sdump_data(self) -> NDArray[Any]:
        """
        Returns the front panel display image ("screen shot")


        Returns:
            NDArray[Any]: Returns the front panel display image ("screen shot")
        """
        cmd = f":HCOPy:SDUMp:DATA?"
        response = self._rsrc.query(cmd)
        return np.array(response)

    def get_hcopy_sdump_data_format(self) -> str:
        """
        Specifies the image format for images returned by HCOPy:SDUMp:DATA?.


        Returns:
            str: Returns the display image format.
        """
        cmd = f":HCOPy:SDUMp:DATA:FORMat?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'format', 'type_options': ['HcopSdumDataFormat']}]
    )
    def set_hcopy_sdump_data_format(self, format: HcopSdumDataFormat) -> None:
        """
        Specifies the image format for images returned by HCOPy:SDUMp:DATA?.

        Args:
            format (str): PNG|BMP.
        """
        cmd = f":HCOPy:SDUMp:DATA:FORMat {format}"
        self._rsrc.write(cmd)





    @validate_parameters(
        rules_list=[{'name': 'initiate_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_initiate_continuous(self, initiate_num: int = 1) -> Boolean:
        """
        Specifies whether the trigger system for one channel always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current state of the continuous trigger function.
        """
        cmd = f":INITiate{initiate_num}:CONTinuous?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'initiate_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_initiate_continuous(self, state: Boolean, initiate_num: int = 1) -> None:
        """
        Specifies whether the trigger system for one channel always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0
        """
        cmd = f":INITiate{initiate_num}:CONTinuous {state}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'initiate_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_initiate_continuous_all(self, state: Boolean, initiate_num: int = 1) -> None:
        """
        Specifies whether the trigger system for both channels (ALL) always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)
            state (bool): The current state of the function.
        """
        cmd = f":INITiate{initiate_num}:CONTinuous:ALL {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'initiate_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def initiate_immediate(self, initiate_num: int = 1) -> None:
        """
        Change state of triggering system for both channels (ALL) from "idle" to "wait-for-trigger" for the number of triggers specified by TRIGger[1|2]:COUNt.

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":INITiate{initiate_num}:IMMediate"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'initiate_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def initiate_immediate_all(self, initiate_num: int = 1) -> None:
        """
        Change state of triggering system for both channels (ALL) from "idle" to "wait-for-trigger" for the number of triggers specified by TRIGger[1|2]:COUNt

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":INITiate{initiate_num}:IMMediate:ALL"
        self._rsrc.write(cmd)




    def get_lxi_identify_state(self) -> Boolean:
        """
        Turns the LXI Identify Indicator on the display on or off.


        Returns:
            bool: Returns the current state of the LXI Identify Indicator display.
        """
        cmd = f":LXI:IDENtify:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_lxi_identify_state(self, state: Boolean) -> None:
        """
        Turns the LXI Identify Indicator on the display on or off.

        Args:
            state (bool): ON|1|OFF|0.
        """
        cmd = f":LXI:IDENtify:STATe {state}"
        self._rsrc.write(cmd)



    def get_lxi_mdns_enable(self) -> Boolean:
        """
        Disables or enables the Multicast Domain Name System (mDNS).


        Returns:
            bool: Returns the current state of the Multicast Domain Name System (mDNS).
        """
        cmd = f":LXI:MDNS:ENABle?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_lxi_mdns_enable(self, state: Boolean) -> None:
        """
        Disables or enables the Multicast Domain Name System (mDNS).

        Args:
            state (bool): ON|1|OFF|0.
        """
        cmd = f":LXI:MDNS:ENABle {state}"
        self._rsrc.write(cmd)


    def get_lxi_mdns_hname_resolved(self) -> str:
        """
        Returns the resolved (unique) mDNS hostname in the form <mDNS Hostname>-N. 


        Returns:
            str: Returns the resolved (unique) mDNS hostname.
        """
        cmd = f":LXI:MDNS:HNAMe:RESolved?"
        response = self._rsrc.query(cmd)
        return response



    def get_lxi_mdns_sname_desired(self) -> str:
        """
        Sets the desired mDNS service name.


        Returns:
            str: Returns the desired mDNS service name.
        """
        cmd = f":LXI:MDNS:SNAMe:DESired?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'name', 'type_options': ['str']}]
    )
    def set_lxi_mdns_sname_desired(self, name: str) -> None:
        """
        Sets the desired mDNS service name.

        Args:
            name (str): The desired mDNS service name.
        """
        cmd = f":LXI:MDNS:SNAMe:DESired {name}"
        self._rsrc.write(cmd)


    def get_lxi_mdns_sname_resolved(self) -> str:
        """
        Returns the resolved (unique) mDNS service name in the form <Desired mDNS Service Name>(N). 


        Returns:
            str: Return resolved mDNS service name.
        """
        cmd = f":LXI:MDNS:SNAMe:RESolved?"
        response = self._rsrc.query(cmd)
        return response




    def lxi_reset(self) -> None:
        """
        Resets LAN settings to a known operating state, beginning with DHCP. 

        Args:
        """
        cmd = f":LXI:RESet"
        self._rsrc.write(cmd)


    def lxi_restart(self) -> None:
        """
        Restarts the LAN with the current settings as specified by the SYSTem:COMM:LAN commands. 

        Args:
        """
        cmd = f":LXI:RESTart"
        self._rsrc.write(cmd)



    def get_memory_nstates(self) -> int:
        """
        Returns the total number of memory locations available for state storage 


        Returns:
            int: Return number of state storage locations.
        """
        cmd = f":MEMory:NSTates?"
        response = self._rsrc.query(cmd)
        return int(response)


    def get_memory_state_catalog(self) -> str:
        """
        Returns the names assigned to locations 0 through 4.


        Returns:
            str: Returns the names assigned to locations 0 through 4.
        """
        cmd = f":MEMory:STATe:CATalog?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'location', 'type_options': ['int']}]
    )
    def set_memory_state_delete(self, location: int) -> None:
        """
        Deletes a state storage location.

        Args:
            location (int): 0|1|2|3|4.
        """
        cmd = f":MEMory:STATe:DELete {location}"
        self._rsrc.write(cmd)


    def get_memory_state_name(self) -> str:
        """
        Names a storage location. 


        Returns:
            str: Returns the current storage location.
        """
        cmd = f":MEMory:STATe:NAME?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'sLocation', 'type_options': ['int']}, {'name': 'name', 'type_options': ['str']}]
    )
    def set_memory_state_name(self, sLocation: int, name: str) -> None:
        """
        Names a storage location. 

        Args:
            sLocation (int): 0|1|2|3|4.
            name (str): Names a storage location. 
        """
        cmd = f":MEMory:STATe:NAME {sLocation}, {name}"
        self._rsrc.write(cmd)


    def get_memory_state_recall_auto(self) -> Boolean:
        """
        Disables or enables automatic recall of instrument state in storage location "0" at power on.


        Returns:
            bool: Returns the current state of automatic recall of instrument state.
        """
        cmd = f":MEMory:STATe:RECall:AUTO?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}]
    )
    def set_memory_state_recall_auto(self, state: Boolean) -> None:
        """
        Disables or enables automatic recall of instrument state in storage location "0" at power on.

        Args:
            state (bool): ON|1|OFF|0.
        """
        cmd = f":MEMory:STATe:RECall:AUTO {state}"
        self._rsrc.write(cmd)



    def get_memory_state_valid(self) -> Boolean:
        """
        Indicates whether a valid state is currently stored in a storage location.


        Returns:
            bool: Return state of memory location.
        """
        cmd = f":MEMory:STATe:VALid?"
        response = self._rsrc.query(cmd)
        return bool(response)




    @validate_parameters(
        rules_list=[{'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_mmemory_catalog_all(self, mmemory_num: int = 1) -> int:
        """
        Returns a list of all files in the current mass storage directory, including internal storage and the USB drive.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            int: The number of bytes of storage used on the drive.
            int: The number of bytes of storage available.
            str: A string for each state file in the selected folder.
        """
        cmd = f":MMEMory{mmemory_num}:CATalog:ALL?"
        response = self._rsrc.query(cmd)
        return int(response)


    @validate_parameters(
        rules_list=[{'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_mmemory_catalog_data_arbitrary(self, mmemory_num: int = 1) -> int:
        """
        Returns a list of all the arbitrary sequence (.seq) files and folders, as well as arbitrary waveform (.arb/.barb) files in a folder.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            int: The number of bytes of storage used on the drive.
            int: The number of bytes of storage available.
            str: A string for each state file in the selected folder.
        """
        cmd = f":MMEMory{mmemory_num}:CATalog:DATA:ARBitrary?"
        response = self._rsrc.query(cmd)
        return int(response)



    @validate_parameters(
        rules_list=[{'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_mmemory_catalog_state(self, mmemory_num: int = 1) -> int:
        """
        Lists all state files (.sta file extension) in a folder. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            int: The number of bytes of storage used on the drive.
            int: The number of bytes of storage available.
            str: A string for each state file in the selected folder.
        """
        cmd = f":MMEMory{mmemory_num}:CATalog:STATe?"
        response = self._rsrc.query(cmd)
        return int(response)



    @validate_parameters(
        rules_list=[{'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_mmemory_cdirectory(self, mmemory_num: int = 1) -> str:
        """
        MMEMory:CDIRectory selects the default folder for the MMEMory subsystem commands. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current default folder for the MMEMory subsystem commands.
        """
        cmd = f":MMEMory{mmemory_num}:CDIRectory?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'folder', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_cdirectory(self, folder: str, mmemory_num: int = 1) -> None:
        """
        MMEMory:CDIRectory selects the default folder for the MMEMory subsystem commands. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            folder (str): The default folder for the MMEMory subsystem commands.
        """
        cmd = f":MMEMory{mmemory_num}:CDIRectory {folder}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'file1', 'type_options': ['str']}, {'name': 'file2', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_copy(self, file1: str, file2: str, mmemory_num: int = 1) -> None:
        """
        Copies <file1> to <file2>. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            file1 (str): The source file name.
            file2 (str): The destination file name.
        """
        cmd = f":MMEMory{mmemory_num}:COPY {file1}, {file2}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['str']}, {'name': 'destination', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_copy_sequence(self, source: str, destination: str, mmemory_num: int = 1) -> None:
        """
        Copies a sequence from <source> to <destination>. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source.
            destination (str): The destination.
        """
        cmd = f":MMEMory{mmemory_num}:COPY:SEQuence {source}, {destination}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'file', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_delete(self, file: str, mmemory_num: int = 1) -> None:
        """
        Deletes a file. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            file (str): The file to be deleted.
        """
        cmd = f":MMEMory{mmemory_num}:DELete {file}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'binary_block', 'type_options': ['Union[bytes] | None']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_download_data(self, binary_block: Union[bytes] | None, mmemory_num: int = 1) -> None:
        """
        Downloads data from the host computer to a file in the instrument.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            binary_block (Union[bytes] | None): Any IEEE-488 definite or indefinite block.
        """
        cmd = f":MMEMory{mmemory_num}:DOWNload:DATA {binary_block}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_mmemory_download_fname(self, mmemory_num: int = 1) -> str:
        """
        Creates or opens the specified filename prior to writing data to that file with MMEMory:DOWNload:DATA.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the specified filename
        """
        cmd = f":MMEMory{mmemory_num}:DOWNload:FNAMe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_download_fname(self, filename: str, mmemory_num: int = 1) -> None:
        """
        Creates or opens the specified filename prior to writing data to that file with MMEMory:DOWNload:DATA.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name.
        """
        cmd = f":MMEMory{mmemory_num}:DOWNload:FNAMe {filename}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_load_all(self, filename: str, mmemory_num: int = 1) -> None:
        """
        Loads a complete instrument setup, using a named file on the mass storage.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name on current mass storage directory.
        """
        cmd = f":MMEMory{mmemory_num}:LOAD:ALL {filename}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}, {'name': 'data_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_load_data(self, filename: str, mmemory_num: int = 1, data_num: int = 1) -> None:
        """
        Loads the specified arb segment(.arb/.barb) or arb sequence (.seq) file in INTERNAL or USB memory into volatile memory for the specified channel.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            data_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name.
        """
        cmd = f":MMEMory{mmemory_num}:LOAD:DATA{data_num} {filename}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}, {'name': 'list_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_load_list(self, filename: str, mmemory_num: int = 1, list_num: int = 1) -> None:
        """
        Loads a frequency list file (.lst).

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            list_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name on the mass memory device.
        """
        cmd = f":MMEMory{mmemory_num}:LOAD:LIST{list_num} {filename}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_load_state(self, filename: str, mmemory_num: int = 1) -> None:
        """
        Stores the current instrument state to a state file. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): The state file to load the instrument from.
        """
        cmd = f":MMEMory{mmemory_num}:LOAD:STATe {filename}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'folder', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_mdirectory(self, folder: str, mmemory_num: int = 1) -> None:
        """
        MMEMory:MDIRectory makes a new directory (folder) on the mass storage medium.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            folder (str): The new folder to be created.
        """
        cmd = f":MMEMory{mmemory_num}:MDIRectory {folder}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'file1', 'type_options': ['str']}, {'name': 'file2', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_move(self, file1: str, file2: str, mmemory_num: int = 1) -> None:
        """
        Moves and/or renames <file1> to <file2>. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            file1 (str): The source file.
            file2 (str): The destination file.
        """
        cmd = f":MMEMory{mmemory_num}:MOVE {file1}, {file2}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'folder', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_rdirectory(self, folder: str, mmemory_num: int = 1) -> None:
        """
        MMEMory:RDIRectory removes a directory (folder) on the mass storage medium.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            folder (str): The folder to be removed.
        """
        cmd = f":MMEMory{mmemory_num}:RDIRectory {folder}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_store_all(self, filename: str, mmemory_num: int = 1) -> None:
        """
        Loads or saves a complete instrument setup, using a named file on the mass storage.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name on current mass storage directory.
        """
        cmd = f":MMEMory{mmemory_num}:STORe:ALL {filename}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}, {'name': 'data_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_store_data(self, filename: str, mmemory_num: int = 1, data_num: int = 1) -> None:
        """
        Stores the specified arb segment(.arb/.barb) or arb sequence (.seq) data in the channel specified volatile memory (default, channel 1) in INTERNAL or USB memory.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            data_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name.
        """
        cmd = f":MMEMory{mmemory_num}:STORe:DATA{data_num} {filename}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}, {'name': 'list_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_store_list(self, filename: str, mmemory_num: int = 1, list_num: int = 1) -> None:
        """
        Loads or stores a frequency list file (.lst).

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            list_num (int): The channel number identifier. (Range: 1-2)
            filename (str): The file name to store the currently loaded frequency list in.
        """
        cmd = f":MMEMory{mmemory_num}:STORe:LIST{list_num} {filename}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_mmemory_store_state(self, filename: str, mmemory_num: int = 1) -> None:
        """
        Stores the current instrument state to a state file. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name on the current directory.
        """
        cmd = f":MMEMory{mmemory_num}:STORe:STATe {filename}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'mmemory_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_mmemory_upload(self, mmemory_num: int = 1) -> NDArray[Any]:
        """
        Uploads the contents of a file from the instrument to the host computer.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            NDArray[Any]: Returns the contents of the file to be uploaded.
        """
        cmd = f":MMEMory{mmemory_num}:UPLoad?"
        response = self._rsrc.query(cmd)
        return np.array(response)



    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output(self, output_num: int = 1) -> Boolean:
        """
        Enables or disables the front-panel output connector.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current state of the front-panel output connector.
        """
        cmd = f":OUTPut{output_num}?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output(self, state: Boolean, output_num: int = 1) -> None:
        """
        Enables or disables the front-panel output connector.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":OUTPut{output_num} {state}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_load(self, output_num: int = 1) -> float:
        """
        Sets expected output termination.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the load impedance.
        """
        cmd = f":OUTPut{output_num}:LOAD?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'ohms', 'type_options': ['float', 'Enumminmaxdefinf']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_load(self, ohms: Union[float, Enumminmaxdefinf], output_num: int = 1) -> None:
        """
        Sets expected output termination.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            ohms (float): The expected output termination.
        """
        cmd = f":OUTPut{output_num}:LOAD {ohms}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_mode(self, output_num: int = 1) -> OutpMode:
        """
        Enables (GATed) or disables (NORMal) gating of the output waveform signal on and off using the trigger input.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the mode.
        """
        cmd = f":OUTPut{output_num}:MODE?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mode', 'type_options': ['OutpMode']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_mode(self, mode: OutpMode, output_num: int = 1) -> None:
        """
        Enables (GATed) or disables (NORMal) gating of the output waveform signal on and off using the trigger input.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            mode (str): NORMal|GATed.
        """
        cmd = f":OUTPut{output_num}:MODE {mode}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_polarity(self, output_num: int = 1) -> OutpPolarity:
        """
        Inverts waveform relative to the offset voltage.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the polarity.
        """
        cmd = f":OUTPut{output_num}:POLarity?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'polarity', 'type_options': ['OutpPolarity']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_polarity(self, polarity: OutpPolarity, output_num: int = 1) -> None:
        """
        Inverts waveform relative to the offset voltage.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            polarity (str): NORMal|INVerted.
        """
        cmd = f":OUTPut{output_num}:POLarity {polarity}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_sync(self, output_num: int = 1) -> Boolean:
        """
        Disables or enables the front-panel Sync connector.  

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current state of the front-panel Sync connector.
        """
        cmd = f":OUTPut{output_num}:SYNC?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_sync(self, state: Boolean, output_num: int = 1) -> None:
        """
        Disables or enables the front-panel Sync connector.  

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":OUTPut{output_num}:SYNC {state}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_sync_mode(self, output_num: int = 1) -> OutpSyncMode:
        """
        Specifies normal Sync behavior (NORMal), forces Sync to follow the carrier waveform (CARRier), or indicates marker position (MARKer).

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the mode.
        """
        cmd = f":OUTPut{output_num}:SYNC:MODE?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mode', 'type_options': ['OutpSyncMode']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_sync_mode(self, mode: OutpSyncMode, output_num: int = 1) -> None:
        """
        Specifies normal Sync behavior (NORMal), forces Sync to follow the carrier waveform (CARRier), or indicates marker position (MARKer).

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            mode (str): NORMal|CARRier|MARKer
        """
        cmd = f":OUTPut{output_num}:SYNC:MODE {mode}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_sync_polarity(self, output_num: int = 1) -> OutpSyncPolarity:
        """
        Sets the desired output polarity of the Sync output to trigger external equipment that may require falling or rising edge triggers.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the desired output polarity of the Sync output.
        """
        cmd = f":OUTPut{output_num}:SYNC:POLarity?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'polarity', 'type_options': ['OutpSyncPolarity']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_sync_polarity(self, polarity: OutpSyncPolarity, output_num: int = 1) -> None:
        """
        Sets the desired output polarity of the Sync output to trigger external equipment that may require falling or rising edge triggers.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            polarity (str): NORMal|INVerted
        """
        cmd = f":OUTPut{output_num}:SYNC:POLarity {polarity}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_sync_source(self, output_num: int = 1) -> OutpSyncSource:
        """
        Sets the source for the Sync output connector.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the source for the Sync output connector.
        """
        cmd = f":OUTPut{output_num}:SYNC:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'channel', 'type_options': ['OutpSyncSource']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_sync_source(self, channel: OutpSyncSource, output_num: int = 1) -> None:
        """
        Sets the source for the Sync output connector.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            channel (str): CH1|CH2
        """
        cmd = f":OUTPut{output_num}:SYNC:SOURce {channel}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_trigger(self, output_num: int = 1) -> Boolean:
        """
        Disables or enables the "trigger out" signal for sweep and burst modes.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current state of the trigger out signal function.
        """
        cmd = f":OUTPut{output_num}:TRIGger?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_trigger(self, state: Boolean, output_num: int = 1) -> None:
        """
        Disables or enables the "trigger out" signal for sweep and burst modes.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":OUTPut{output_num}:TRIGger {state}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_trigger_slope(self, output_num: int = 1) -> OutpTrigSlope:
        """
        Selects whether the instrument uses the rising edge or falling edge for the "trigger out" signal.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns whether the instrument uses the rising edge or falling edge for the "trigger out" signal.
        """
        cmd = f":OUTPut{output_num}:TRIGger:SLOPe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'edge', 'type_options': ['OutpTrigSlope']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_trigger_slope(self, edge: OutpTrigSlope, output_num: int = 1) -> None:
        """
        Selects whether the instrument uses the rising edge or falling edge for the "trigger out" signal.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            edge (str): POSitive|NEGative
        """
        cmd = f":OUTPut{output_num}:TRIGger:SLOPe {edge}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_output_trigger_source(self, output_num: int = 1) -> OutpTrigSource:
        """
        Selects the source channel used by trigger output on a two-channel instrument. 

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source channel.
        """
        cmd = f":OUTPut{output_num}:TRIGger:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'channel', 'type_options': ['OutpTrigSource']}, {'name': 'output_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_output_trigger_source(self, channel: OutpTrigSource, output_num: int = 1) -> None:
        """
        Selects the source channel used by trigger output on a two-channel instrument. 

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            channel (str): Selects the source channel used by trigger output on a two-channel instrument.
        """
        cmd = f":OUTPut{output_num}:TRIGger:SOURce {channel}"
        self._rsrc.write(cmd)




    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_burst_gate_polarity(self, source_num: int = 1) -> SourBursGatePolarity:
        """
        Selects true-high (NORMal) or true-low (INVerted) logic levels on the rear-panel Trig In connector for an externally gated burst.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the logic levels on the rear-panel Trig In connector for an externally gated burst.
        """
        cmd = f":SOURce{source_num}:BURSt:GATE:POLarity?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'polarity', 'type_options': ['SourBursGatePolarity']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_burst_gate_polarity(self, polarity: SourBursGatePolarity, source_num: int = 1) -> None:
        """
        Selects true-high (NORMal) or true-low (INVerted) logic levels on the rear-panel Trig In connector for an externally gated burst.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            polarity (str): The logic levels on the rear-panel Trig In connector for an externally gated burst.

        """
        cmd = f":SOURce{source_num}:BURSt:GATE:POLarity {polarity}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_burst_internal_period(self, source_num: int = 1) -> float:
        """
        Sets the burst period for internally-triggered bursts.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the burst period for internally-triggered bursts.
        """
        cmd = f":SOURce{source_num}:BURSt:INTernal:PERiod?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'Enumminmaxdef']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_burst_internal_period(self, seconds: Union[float, Enumminmaxdef], source_num: int = 1) -> None:
        """
        Sets the burst period for internally-triggered bursts.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The burst period for internally-triggered bursts.
        """
        cmd = f":SOURce{source_num}:BURSt:INTernal:PERiod {seconds}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_burst_mode(self, source_num: int = 1) -> SourBursMode:
        """
        Selects the burst mode.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current burst mode.
        """
        cmd = f":SOURce{source_num}:BURSt:MODE?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mode', 'type_options': ['SourBursMode']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_burst_mode(self, mode: SourBursMode, source_num: int = 1) -> None:
        """
        Selects the burst mode.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The burst mode.
        """
        cmd = f":SOURce{source_num}:BURSt:MODE {mode}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_burst_ncycles(self, source_num: int = 1) -> float:
        """
        Sets the number of cycles to be output per burst (triggered burst mode only).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the number of cycles to be output per burst.
        """
        cmd = f":SOURce{source_num}:BURSt:NCYCles?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'num_cycles', 'type_options': ['float', 'Enumminmaxdefinf']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_burst_ncycles(self, num_cycles: Union[float, Enumminmaxdefinf], source_num: int = 1) -> None:
        """
        Sets the number of cycles to be output per burst (triggered burst mode only).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            num_cycles (float): The number of cycles to be output per burst.
        """
        cmd = f":SOURce{source_num}:BURSt:NCYCles {num_cycles}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_burst_phase(self, source_num: int = 1) -> float:
        """
        Sets the starting phase angle for the burst.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the starting phase angle for the burst.
        """
        cmd = f":SOURce{source_num}:BURSt:PHASe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'angle', 'type_options': ['float', 'Enumminmaxdef']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_burst_phase(self, angle: Union[float, Enumminmaxdef], source_num: int = 1) -> None:
        """
        Sets the starting phase angle for the burst.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            angle (float): The starting phase angle for the burst.
        """
        cmd = f":SOURce{source_num}:BURSt:PHASe {angle}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_burst_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables burst mode.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current state of the burst mode.
        """
        cmd = f":SOURce{source_num}:BURSt:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'boolean', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_burst_state(self, boolean: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables burst mode.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            boolean (bool): Enables or disables burst mode.
        """
        cmd = f":SOURce{source_num}:BURSt:STATe {boolean}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_am_depth(self, source_num: int = 1) -> float:
        """
        Sets internal modulation depth ("percent modulation") in percent.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the internal modulation depth ("percent modulation") in percent.
        """
        cmd = f":SOURce{source_num}:AM:DEPTh?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'depth_in_percent', 'type_options': ['float', 'Enumminmaxdef']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_am_depth(self, depth_in_percent: Union[float, Enumminmaxdef], source_num: int = 1) -> None:
        """
        Sets internal modulation depth ("percent modulation") in percent.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            depth_in_percent (float): Internal modulation depth ("percent modulation") in percent.
        """
        cmd = f":SOURce{source_num}:AM:DEPTh {depth_in_percent}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_am_dssc(self, source_num: int = 1) -> Boolean:
        """
        Selects Amplitude Modulation mode 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current state of the Amplitude Modulation mode.
        """
        cmd = f":SOURce{source_num}:AM:DSSC?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_am_dssc(self, state: Boolean, source_num: int = 1) -> None:
        """
        Selects Amplitude Modulation mode 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":SOURce{source_num}:AM:DSSC {state}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_am_internal_frequency(self, source_num: int = 1) -> float:
        """
        Sets frequency of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current frequency of modulating waveform.
        """
        cmd = f":SOURce{source_num}:AM:INTernal:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'Enumminmaxdef']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_am_internal_frequency(self, frequency: Union[float, Enumminmaxdef], source_num: int = 1) -> None:
        """
        Sets frequency of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency of modulating waveform.
        """
        cmd = f":SOURce{source_num}:AM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_am_internal_function(self, source_num: int = 1) -> SourAmIntFuncShapeclone:
        """
        Selects shape of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current shape of modulating waveform.
        """
        cmd = f":SOURce{source_num}:AM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'function', 'type_options': ['SourAmIntFuncShapeclone']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_am_internal_function(self, function: SourAmIntFuncShapeclone, source_num: int = 1) -> None:
        """
        Selects shape of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): Shape of modulating waveform.
        """
        cmd = f":SOURce{source_num}:AM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_am_source(self, source_num: int = 1) -> SourAmSource:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce:AM:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourAmSource']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_am_source(self, source: SourAmSource, source_num: int = 1) -> None:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): INTernal|EXTernal|CH1|CH2.
        """
        cmd = f":SOURce:AM:SOURce {source}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_am_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current state of the modulation.
        """
        cmd = f":SOURce{source_num}:AM:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_am_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0
        """
        cmd = f":SOURce{source_num}:AM:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_apply(self, source_num: int = 1) -> str:
        """
        Queries the output configuration.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the output configuration.
        """
        cmd = f":SOURce{source_num}:APPLy?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'sample_rate', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_arbitrary(self, sample_rate: Union[float, StdNumEnums1], amplitude: Union[float, StdNumEnums1], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs arbitrary waveform selected by FUNCtion: ARBitrary, using the specified sample rate, amplitude, and offset. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sample_rate (float): The specified sample rate.
            amplitude (float): The amplitude
            offset (float): The DC offset voltage
        """
        cmd = f":SOURce{source_num}:APPLy:ARBitrary {sample_rate}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnumsDef']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnumsDef']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_dc(self, frequency: Union[float, StdNumEnumsDef], amplitude: Union[float, StdNumEnumsDef], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs a DC voltage.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): Frequency
            amplitude (float): Amplitude
            offset (float): The DC offset voltage
        """
        cmd = f":SOURce{source_num}:APPLy:DC {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnumsDef']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_noise(self, frequency: Union[float, StdNumEnumsDef], amplitude: Union[float, StdNumEnums1], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs gaussian noise with the specified amplitude and DC offset.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): Frequency
            amplitude (float): Desired output amplitude
            offset (float): The DC offset voltage
        """
        cmd = f":SOURce{source_num}:APPLy:NOISe {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnumsDef']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_prbs(self, frequency: Union[float, StdNumEnumsDef], amplitude: Union[float, StdNumEnums1], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs a pseudo-random binary sequence with the specified bit rate, amplitude and DC offset.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): Frequency
            amplitude (float): Desired output amplitude
            offset (float): The DC offset voltage
        """
        cmd = f":SOURce{source_num}:APPLy:PRBS {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_pulse(self, frequency: Union[float, StdNumEnums1], amplitude: Union[float, StdNumEnums1], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs a pulse wave with the specified frequency, amplitude, and DC offset.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The specified frequency
            amplitude (float): Desired output amplitude
            offset (float):  the DC offset voltage
        """
        cmd = f":SOURce{source_num}:APPLy:PULSe {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_ramp(self, frequency: Union[float, StdNumEnums1], amplitude: Union[float, StdNumEnums1], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs a ramp wave with the specified frequency, amplitude, and DC offset.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The specified frequency.
            amplitude (float): Desired output amplitude.
            offset (float): The DC offset voltage.
        """
        cmd = f":SOURce{source_num}:APPLy:RAMP {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_sinusoid(self, frequency: Union[float, StdNumEnums1], amplitude: Union[float, StdNumEnums1], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs a sine wave with the specified frequency, amplitude, and DC offset.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The specified frequency.
            amplitude (float): Desired output amplitude
            offset (float): The DC offset voltage.
        """
        cmd = f":SOURce{source_num}:APPLy:SINusoid {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_square(self, frequency: Union[float, StdNumEnums1], amplitude: Union[float, StdNumEnums1], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs a square wave with the specified frequency, amplitude, and DC offset.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The specified frequency.
            amplitude (float): Desired output amplitude.
            offset (float): The DC offset voltage.
        """
        cmd = f":SOURce{source_num}:APPLy:SQUare {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'amplitude', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'offset', 'type_options': ['float', 'StdNumEnums1']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_apply_triangle(self, frequency: Union[float, StdNumEnums1], amplitude: Union[float, StdNumEnums1], offset: Union[float, StdNumEnums1], source_num: int = 1) -> None:
        """
        Outputs a triangle wave with the specified frequency, amplitude, and DC offset.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency.
            amplitude (float): The Desired output amplitude
            offset (float): The DC offset voltage
        """
        cmd = f":SOURce{source_num}:APPLy:TRIangle {frequency}, {amplitude}, {offset}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_bpsk_internal_rate(self, source_num: int = 1) -> float:
        """
        Sets the rate at which the output phase "shifts" between the carrier and offset phase.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current rate at which the output phase "shifts" between the carrier and offset phase.
        """
        cmd = f":SOURce{source_num}:BPSK:INTernal:RATE?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'modulating_frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_bpsk_internal_rate(self, modulating_frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the rate at which the output phase "shifts" between the carrier and offset phase.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            modulating_frequency (float): The rate at which the output phase "shifts" between the carrier and offset phase.
        """
        cmd = f":SOURce{source_num}:BPSK:INTernal:RATE {modulating_frequency}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_bpsk_phase(self, source_num: int = 1) -> float:
        """
        Sets the Binary Phase Shift Keying phase shift in degrees.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the Binary Phase Shift Keying.
        """
        cmd = f":SOURce{source_num}:BPSK:PHASe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'angle', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_bpsk_phase(self, angle: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the Binary Phase Shift Keying phase shift in degrees.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            angle (float): The Binary Phase Shift Keying.
        """
        cmd = f":SOURce{source_num}:BPSK:PHASe {angle}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_bpsk_source(self, source_num: int = 1) -> SourAmSourceclone:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce:BPSK:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourAmSourceclone']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_bpsk_source(self, source: SourAmSourceclone, source_num: int = 1) -> None:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): INTernal|EXTernal.
        """
        cmd = f":SOURce:BPSK:SOURce {source}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_bpsk_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current state of the modulation.
        """
        cmd = f":SOURce{source_num}:BPSK:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_bpsk_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":SOURce{source_num}:BPSK:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_combine_feed(self, source_num: int = 1) -> SourCombFeed:
        """
        Enables or disables the combining of both channels' outputs on a two-channel instrument into a single channel connector.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current  source channel.
        """
        cmd = f":SOURce{source_num}:COMBine:FEED?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourCombFeed']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_combine_feed(self, source: SourCombFeed, source_num: int = 1) -> None:
        """
        Enables or disables the combining of both channels' outputs on a two-channel instrument into a single channel connector.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): CH1|CH2|NONE.
        """
        cmd = f":SOURce{source_num}:COMBine:FEED {source}"
        self._rsrc.write(cmd)



    @overload
    def set_source_data_arbitrary(self, source_num: int, syntax: SourceDataArbitrarySyntax.BLOCKREAL32, arb_name: str, binary_block: Union[bytes] | None) -> None:
        ...

    @overload
    def set_source_data_arbitrary(self, source_num: int, syntax: SourceDataArbitrarySyntax.ASCII, arb_name: str, value: float) -> None:
        ...

    @validate_parameters(
        rules_list=[{'name': 'syntax', 'type_options': ['SourceDataArbitrarySyntax']}, {'name': 'arb_name', 'type_options': ['str']}, {'name': 'data', 'type_options': ['Any']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_data_arbitrary(self, syntax: SourceDataArbitrarySyntax, arb_name: str, data: Any, source_num: int = 1) -> None:
        """
        Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            syntax (SourceDataArbitrarySyntax): The syntax variant to use for this command

            For syntax BlockReal32:
                arb_name (str): The arbitrary sequence to be downloaded to.
                binary_block (Union[bytes] | None): List of values to be downloaded into waveform memory.

            For syntax Ascii:
                arb_name (str): The arbitrary sequence to be downloaded to.
                value (float): List of values to be downloaded into waveform memory. (Repeatable: *)
        """
        match syntax:
            case SourceDataArbitrarySyntax.BLOCKREAL32:
                cmd = f":SOURce{source_num}:DATA:ARBitrary {arb_name}, {data}"

                self._write_binary_data(cmd, data, "BlockReal32")
            case SourceDataArbitrarySyntax.ASCII:
                cmd = f":SOURce{source_num}:DATA:ARBitrary {arb_name}, {data}"

                self._rsrc.write(cmd)
            case _:
                raise ValueError(f"Unsupported syntax '{syntax}' for command set_source_data_arbitrary.")

    @overload
    def set_source_data_arbitrary_dac(self, source_num: int, syntax: SourceDataArbitraryDacSyntax.ASCII, arb_name: str, value: int) -> None:
        ...

    @overload
    def set_source_data_arbitrary_dac(self, source_num: int, syntax: SourceDataArbitraryDacSyntax.BLOCKINT16, arb_name: str, binary_block: Union[bytes] | None) -> None:
        ...

    @validate_parameters(
        rules_list=[{'name': 'syntax', 'type_options': ['SourceDataArbitraryDacSyntax']}, {'name': 'arb_name', 'type_options': ['str']}, {'name': 'data', 'type_options': ['Any']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_data_arbitrary_dac(self, syntax: SourceDataArbitraryDacSyntax, arb_name: str, data: Any, source_num: int = 1) -> None:
        """
        Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            syntax (SourceDataArbitraryDacSyntax): The syntax variant to use for this command

            For syntax Ascii:
                arb_name (str): The arbitrary sequence name to be downloaded to.
                value (int): The DAC codes to be loaded into waveform memory as a list of integers. (Repeatable: *)

            For syntax BlockInt16:
                arb_name (str): The arbitrary sequence name to be downloaded to.
                binary_block (Union[bytes] | None): Binary block data.
        """
        match syntax:
            case SourceDataArbitraryDacSyntax.ASCII:
                cmd = f":SOURce{source_num}:DATA:ARBitrary:DAC {arb_name}, {data}"

                self._rsrc.write(cmd)
            case SourceDataArbitraryDacSyntax.BLOCKINT16:
                cmd = f":SOURce{source_num}:DATA:ARBitrary:DAC {arb_name}, {data}"

                self._write_binary_data(cmd, data, "BlockInt16")
            case _:
                raise ValueError(f"Unsupported syntax '{syntax}' for command set_source_data_arbitrary_dac.")



    @overload
    def set_source_data_arbitrary2(self, source_num: int, syntax: SourceDataArbitrary2Syntax.BLOCKREAL32, arb_name: str, binary_block: Union[bytes] | None) -> None:
        ...

    @overload
    def set_source_data_arbitrary2(self, source_num: int, syntax: SourceDataArbitrary2Syntax.ASCII, arb_name: str, value: float) -> None:
        ...

    @validate_parameters(
        rules_list=[{'name': 'syntax', 'type_options': ['SourceDataArbitrary2Syntax']}, {'name': 'arb_name', 'type_options': ['str']}, {'name': 'data', 'type_options': ['Any']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_data_arbitrary2(self, syntax: SourceDataArbitrary2Syntax, arb_name: str, data: Any, source_num: int = 1) -> None:
        """
        Downloads integer values representing DAC codes (DATA:ARBitrary[2]:DAC) or floating point values (DATA:ARBitrary[2]) into waveform volatile memory as either a list of comma separated values or binary block of data.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            syntax (SourceDataArbitrary2Syntax): The syntax variant to use for this command

            For syntax BlockReal32:
                arb_name (str): The arbitrary sequence to be downloaded to.
                binary_block (Union[bytes] | None): List of values to be downloaded into waveform memory.

            For syntax Ascii:
                arb_name (str): The arbitrary sequence to be downloaded to.
                value (float): List of values to be downloaded into waveform memory. (Repeatable: *)
        """
        match syntax:
            case SourceDataArbitrary2Syntax.BLOCKREAL32:
                cmd = f":SOURce{source_num}:DATA:ARBitrary2 {arb_name}, {data}"

                self._write_binary_data(cmd, data, "BlockReal32")
            case SourceDataArbitrary2Syntax.ASCII:
                cmd = f":SOURce{source_num}:DATA:ARBitrary2 {arb_name}, {data}"

                self._rsrc.write(cmd)
            case _:
                raise ValueError(f"Unsupported syntax '{syntax}' for command set_source_data_arbitrary2.")

    @overload
    def set_source_data_arbitrary2_dac(self, source_num: int, syntax: SourceDataArbitrary2DacSyntax.ASCII, arb_name: str, value: int) -> None:
        ...

    @overload
    def set_source_data_arbitrary2_dac(self, source_num: int, syntax: SourceDataArbitrary2DacSyntax.BLOCKINT16, arb_name: str, binary_block: Union[bytes] | None) -> None:
        ...

    @validate_parameters(
        rules_list=[{'name': 'syntax', 'type_options': ['SourceDataArbitrary2DacSyntax']}, {'name': 'arb_name', 'type_options': ['str']}, {'name': 'data', 'type_options': ['Any']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_data_arbitrary2_dac(self, syntax: SourceDataArbitrary2DacSyntax, arb_name: str, data: Any, source_num: int = 1) -> None:
        """
        Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            syntax (SourceDataArbitrary2DacSyntax): The syntax variant to use for this command

            For syntax Ascii:
                arb_name (str): The arbitrary sequence name to be downloaded to.
                value (int): The DAC codes to be loaded into waveform memory as a list of integers. (Repeatable: *)

            For syntax BlockInt16:
                arb_name (str): The arbitrary sequence name to be downloaded to.
                binary_block (Union[bytes] | None): Binary block data.
        """
        match syntax:
            case SourceDataArbitrary2DacSyntax.ASCII:
                cmd = f":SOURce{source_num}:DATA:ARBitrary2:DAC {arb_name}, {data}"

                self._rsrc.write(cmd)
            case SourceDataArbitrary2DacSyntax.BLOCKINT16:
                cmd = f":SOURce{source_num}:DATA:ARBitrary2:DAC {arb_name}, {data}"

                self._write_binary_data(cmd, data, "BlockInt16")
            case _:
                raise ValueError(f"Unsupported syntax '{syntax}' for command set_source_data_arbitrary2_dac.")


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_data_arbitrary2_format(self, source_num: int = 1) -> SourceDataArb2Format:
        """
        Specifies whether the format for data points in DATA:ARB2 and DATA:ARB2:DAC commands is interleaved (ABAB) or all of channel 1 followed by all of channel 2 (AABB).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns an interleaved data format for dual arbitrary waveform data
        """
        cmd = f":SOURce{source_num}:DATA:ARBitrary2:FORMat?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'format', 'type_options': ['SourceDataArb2Format']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_data_arbitrary2_format(self, format: SourceDataArb2Format, source_num: int = 1) -> None:
        """
        Specifies whether the format for data points in DATA:ARB2 and DATA:ARB2:DAC commands is interleaved (ABAB) or all of channel 1 followed by all of channel 2 (AABB).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            format (str): An interleaved data format for dual arbitrary waveform data
        """
        cmd = f":SOURce{source_num}:DATA:ARBitrary2:FORMat {format}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_data_attribute_average(self, source_num: int = 1) -> float:
        """
        Returns the arithmetic mean of all data points for the specified arbitrary waveform INTERNAL or USB memory, or loaded into waveform memory.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the arithmetic mean of all data points for the specified arbitrary waveform INTERNAL or USB memory, or loaded into waveform memory.
        """
        cmd = f":SOURce{source_num}:DATA:ATTRibute:AVERage?"
        response = self._rsrc.query(cmd)
        return float(response)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_data_attribute_cfactor(self, source_num: int = 1) -> float:
        """
        Returns the crest factor of all data points for the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the crest factor of all data points for the specified arbitrary waveform
        """
        cmd = f":SOURce{source_num}:DATA:ATTRibute:CFACtor?"
        response = self._rsrc.query(cmd)
        return float(response)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_data_attribute_points(self, source_num: int = 1) -> int:
        """
        Returns the number of points in the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            int: Returns the number of points in the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.
        """
        cmd = f":SOURce{source_num}:DATA:ATTRibute:POINts?"
        response = self._rsrc.query(cmd)
        return int(response)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_data_attribute_ptpeak(self, source_num: int = 1) -> float:
        """
        This query calculates the peak-to-peak value of all data points for the specified arbitrary waveform segment in INTERNAL or USB memory, or loaded into waveform memory.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the peak-to-peak value
        """
        cmd = f":SOURce{source_num}:DATA:ATTRibute:PTPeak?"
        response = self._rsrc.query(cmd)
        return float(response)



    @validate_parameters(
        rules_list=[{'name': 'block_descriptor', 'type_options': ['Union[bytes] | None']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_data_sequence(self, block_descriptor: Union[bytes] | None, source_num: int = 1) -> None:
        """
        Defines a sequence of waveforms already loaded into waveform memory via MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            block_descriptor (Union[bytes] | None): Defines a sequence of waveforms
        """
        cmd = f":SOURce{source_num}:DATA:SEQuence {block_descriptor}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_data_volatile_catalog(self, source_num: int = 1) -> str:
        """
        Returns the contents of volatile waveform memory, including arbitrary waveforms and sequences.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the contents of volatile waveform memory, including arbitrary waveforms and sequences.
        """
        cmd = f":SOURce{source_num}:DATA:VOLatile:CATalog?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def source_data_volatile_clear(self, source_num: int = 1) -> None:
        """
        Clears waveform memory for the specified channel and reloads the default waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":SOURce{source_num}:DATA:VOLatile:CLEar"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_data_volatile_free(self, source_num: int = 1) -> int:
        """
        Returns number of points available (free) in volatile memory. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            int: Returns number of points available (free) in volatile memory.
        """
        cmd = f":SOURce{source_num}:DATA:VOLatile:FREE?"
        response = self._rsrc.query(cmd)
        return int(response)




    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fm_deviation(self, source_num: int = 1) -> float:
        """
        Sets the peak frequency deviation in Hz. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of  the peak frequency deviation in Hz.
        """
        cmd = f":SOURce{source_num}:FM:DEViation?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'peak_deviation_in_Hz', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fm_deviation(self, peak_deviation_in_Hz: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the peak frequency deviation in Hz. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            peak_deviation_in_Hz (float):  the peak frequency deviation in Hz.
        """
        cmd = f":SOURce{source_num}:FM:DEViation {peak_deviation_in_Hz}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fm_internal_frequency(self, source_num: int = 1) -> float:
        """
        Sets the frequency of the modulating waveform. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the frequency of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:FM:INTernal:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fm_internal_frequency(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the frequency of the modulating waveform. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:FM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fm_internal_function(self, source_num: int = 1) -> SourAmIntFuncShapeclone:
        """
        This command selects the shape of the modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current shape of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:FM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'function', 'type_options': ['SourAmIntFuncShapeclone']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fm_internal_function(self, function: SourAmIntFuncShapeclone, source_num: int = 1) -> None:
        """
        This command selects the shape of the modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The shape of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:FM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fm_source(self, source_num: int = 1) -> SourFmSource:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce:FM:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourFmSource']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fm_source(self, source: SourFmSource, source_num: int = 1) -> None:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of the modulating signal.
        """
        cmd = f":SOURce:FM:SOURce {source}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fm_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of modulation.
        """
        cmd = f":SOURce{source_num}:FM:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fm_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable modulation.
        """
        cmd = f":SOURce{source_num}:FM:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency(self, source_num: int = 1) -> float:
        """
        Sets the output frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current output frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the output frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The output frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency {frequency}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_center(self, source_num: int = 1) -> float:
        """
        Sets the center frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current center frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency:CENTer?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_center(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the center frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The center frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency:CENTer {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_couple_mode(self, source_num: int = 1) -> SourFreqCoupMode:
        """
        Sets the type of frequency coupling between frequency coupled channels; OFFSet specifies a constant frequency offset between channels; RATio specifies a constant ratio between the channels' frequencies.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current frequency coupling mode
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:MODE?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mode', 'type_options': ['SourFreqCoupMode']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_couple_mode(self, mode: SourFreqCoupMode, source_num: int = 1) -> None:
        """
        Sets the type of frequency coupling between frequency coupled channels; OFFSet specifies a constant frequency offset between channels; RATio specifies a constant ratio between the channels' frequencies.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The frequency coupling mode
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:MODE {mode}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_couple_offset(self, source_num: int = 1) -> float:
        """
        Sets the offset frequency when an instrument is in frequency coupled mode OFFSet.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current offset frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:OFFSet?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_couple_offset(self, frequency: float, source_num: int = 1) -> None:
        """
        Sets the offset frequency when an instrument is in frequency coupled mode OFFSet.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The offset frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:OFFSet {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_couple_ratio(self, source_num: int = 1) -> float:
        """
        Sets offset ratio between channel frequencies in frequency coupled mode RATio.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current offset ratio.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:RATio?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'ratio', 'type_options': ['float']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_couple_ratio(self, ratio: float, source_num: int = 1) -> None:
        """
        Sets offset ratio between channel frequencies in frequency coupled mode RATio.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            ratio (float): The offset ratio.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:RATio {ratio}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_couple_state(self, source_num: int = 1) -> Boolean:
        """
        Enables/disables frequency coupling between channels in a two-channel instrument.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of frequency coupling state.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_couple_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables/disables frequency coupling between channels in a two-channel instrument.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enables/disables frequency coupling state.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_mode(self, source_num: int = 1) -> SourFreqMode:
        """
        Sets the type of frequency mode as a continuous wave at a fixed frequency (CW or FIXed), a frequency sweep (SWEep), or a frequency list (LIST).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the type of frequency mode.
        """
        cmd = f":SOURce{source_num}:FREQuency:MODE?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mode', 'type_options': ['SourFreqMode']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_mode(self, mode: SourFreqMode, source_num: int = 1) -> None:
        """
        Sets the type of frequency mode as a continuous wave at a fixed frequency (CW or FIXed), a frequency sweep (SWEep), or a frequency list (LIST).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The frequency mode .
        """
        cmd = f":SOURce{source_num}:FREQuency:MODE {mode}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_span(self, source_num: int = 1) -> float:
        """
        Sets frequency span (used in conjunction with the center frequency) for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the frequency span.
        """
        cmd = f":SOURce{source_num}:FREQuency:SPAN?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_span(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets frequency span (used in conjunction with the center frequency) for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency span.
        """
        cmd = f":SOURce{source_num}:FREQuency:SPAN {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_start(self, source_num: int = 1) -> float:
        """
        Sets the start frequencies for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the start frequencies for a frequency sweep.
        """
        cmd = f":SOURce{source_num}:FREQuency:STARt?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_start(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the start frequencies for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The start frequencies for a frequency sweep.
        """
        cmd = f":SOURce{source_num}:FREQuency:STARt {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_frequency_stop(self, source_num: int = 1) -> float:
        """
        Sets the stop frequencies for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the stop frequencies for a frequency sweep.
        """
        cmd = f":SOURce{source_num}:FREQuency:STOP?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_frequency_stop(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the stop frequencies for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The stop frequencies for a frequency sweep.
        """
        cmd = f":SOURce{source_num}:FREQuency:STOP {frequency}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fskey_frequency(self, source_num: int = 1) -> float:
        """
        Sets the FSK alternate (or "hop") frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the FSK alternate (or "hop") frequency.
        """
        cmd = f":SOURce{source_num}:FSKey:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fskey_frequency(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the FSK alternate (or "hop") frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The FSK alternate (or "hop") frequency.
        """
        cmd = f":SOURce{source_num}:FSKey:FREQuency {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fskey_internal_rate(self, source_num: int = 1) -> float:
        """
        Sets the rate at which output frequency "shifts" between the carrier and hop frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the rate at which output frequency "shifts" between the carrier and hop frequency.
        """
        cmd = f":SOURce{source_num}:FSKey:INTernal:RATE?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'rate_in_Hz', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fskey_internal_rate(self, rate_in_Hz: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the rate at which output frequency "shifts" between the carrier and hop frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            rate_in_Hz (float): The rate at which output frequency "shifts" between the carrier and hop frequency.
        """
        cmd = f":SOURce{source_num}:FSKey:INTernal:RATE {rate_in_Hz}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fskey_source(self, source_num: int = 1) -> SourAmSourceclone:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce:FSKey:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourAmSourceclone']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fskey_source(self, source: SourAmSourceclone, source_num: int = 1) -> None:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of the modulating signal.
        """
        cmd = f":SOURce:FSKey:SOURce {source}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_fskey_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of modulation.
        """
        cmd = f":SOURce{source_num}:FSKey:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_fskey_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable modulation.
        """
        cmd = f":SOURce{source_num}:FSKey:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function(self, source_num: int = 1) -> SourFuncShapeclone:
        """
        Selects output function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current output function.
        """
        cmd = f":SOURce{source_num}:FUNCtion?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'function', 'type_options': ['SourFuncShapeclone']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function(self, function: SourFuncShapeclone, source_num: int = 1) -> None:
        """
        Selects output function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The output function.
        """
        print(f":SOURce{source_num}:FUNCtion {function}")
        cmd = f":SOURce{source_num}:FUNCtion {function}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary(self, source_num: int = 1) -> str:
        """
        Selects an arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'filename', 'type_options': ['str']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary(self, filename: str, source_num: int = 1) -> None:
        """
        Selects an arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            filename (str): The arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary {filename}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_advance(self, source_num: int = 1) -> SourFuncShapArbAdvance:
        """
        Specifies the method for advancing to the next arbitrary waveform data point for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the method for advancing to the next arbitrary waveform data point for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:ADVance?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mode', 'type_options': ['SourFuncShapArbAdvance']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_advance(self, mode: SourFuncShapArbAdvance, source_num: int = 1) -> None:
        """
        Specifies the method for advancing to the next arbitrary waveform data point for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The method for advancing to the next arbitrary waveform data point for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:ADVance {mode}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_balance_gain(self, source_num: int = 1) -> float:
        """
        Sets the gain balance ratio for dual arbitrary waveforms.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the gain balance ratio for dual arbitrary waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:GAIN?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'percent', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_balance_gain(self, percent: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the gain balance ratio for dual arbitrary waveforms.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            percent (float): The gain balance ratio for dual arbitrary waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:GAIN {percent}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_balance_offset1(self, source_num: int = 1) -> float:
        """
        Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:OFFSet1?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'volts', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_balance_offset1(self, volts: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            volts (float): The offset (in volts) added to the dual arbitrary waveform offset for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:OFFSet1 {volts}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_balance_offset2(self, source_num: int = 1) -> float:
        """
        Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:OFFSet2?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'volts', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_balance_offset2(self, volts: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            volts (float): The offset (in volts) added to the dual arbitrary waveform offset for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:OFFSet2 {volts}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_balance_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables channel balancing for dual arbitrary waveforms 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of the channel balancing for dual arbitrary waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_balance_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables channel balancing for dual arbitrary waveforms 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the channel balancing for dual arbitrary waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_filter(self, source_num: int = 1) -> SourFuncShapArbFilter:
        """
        Specifies the filter setting for an arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the filter setting for an arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:FILTer?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'filter', 'type_options': ['SourFuncShapArbFilter']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_filter(self, filter: SourFuncShapArbFilter, source_num: int = 1) -> None:
        """
        Specifies the filter setting for an arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            filter (str): The filter setting for an arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:FILTer {filter}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_frequency(self, source_num: int = 1) -> float:
        """
        Sets the frequency for the arbitrary waveform.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the frequency for the arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_frequency(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the frequency for the arbitrary waveform.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency for the arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:FREQuency {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_period(self, source_num: int = 1) -> float:
        """
        Sets the period for the arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the period for the arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:PERiod?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'period', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_period(self, period: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the period for the arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            period (float): The period for the arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:PERiod {period}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_points(self, source_num: int = 1) -> int:
        """
        Returns the number of points in the currently selected arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            int: Returns the number of points in the currently selected arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:POINts?"
        response = self._rsrc.query(cmd)
        return int(response)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_ptpeak(self, source_num: int = 1) -> float:
        """
        Sets peak to peak voltage.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of peak to peak voltage.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:PTPeak?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'voltage', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_ptpeak(self, voltage: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets peak to peak voltage.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): Peak to peak voltage.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:PTPeak {voltage}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_skew_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables skew time compensation (FUNCtion:ARBitrary:SKEW:TIME). This is always OFF for modulated signals, sweeps, lists, and bursts.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of the skew time compensation function.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SKEW:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_skew_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables skew time compensation (FUNCtion:ARBitrary:SKEW:TIME). This is always OFF for modulated signals, sweeps, lists, and bursts.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the skew time compensation function.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SKEW:STATe {state}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_skew_time(self, source_num: int = 1) -> float:
        """
        Sets a small time difference between the channels to compensate for minor variations in timing at the connector output plane or at the device under test (DUT). 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the skew time
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SKEW:TIME?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'time', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_skew_time(self, time: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets a small time difference between the channels to compensate for minor variations in timing at the connector output plane or at the device under test (DUT). 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            time (float): The skew time
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SKEW:TIME {time}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_arbitrary_srate(self, source_num: int = 1) -> float:
        """
        Sets the sample rate for the arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the sample rate for the arbitary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SRATe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'sample_rate', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_arbitrary_srate(self, sample_rate: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the sample rate for the arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sample_rate (float): The sample rate for the arbitary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SRATe {sample_rate}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def source_function_arbitrary_synchronize(self, source_num: int = 1) -> None:
        """
        Causes two independent arbitrary waveforms to synchronize to first point of each waveform (two-channel instruments only).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SYNChronize"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_noise_bandwidth(self, source_num: int = 1) -> float:
        """
        Sets bandwidth of noise function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of bandwidth of noise function.
        """
        cmd = f":SOURce{source_num}:FUNCtion:NOISe:BANDwidth?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'bandwidth', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_noise_bandwidth(self, bandwidth: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets bandwidth of noise function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            bandwidth (float): Bandwidth of noise function.
        """
        cmd = f":SOURce{source_num}:FUNCtion:NOISe:BANDwidth {bandwidth}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_prbs_brate(self, source_num: int = 1) -> float:
        """
        Sets the pseudo-random binary sequence (PRBS) bit rate.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: The pseudo-random binary sequence (PRBS) bit rate.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:BRATe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'bit_rate', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_prbs_brate(self, bit_rate: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the pseudo-random binary sequence (PRBS) bit rate.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            bit_rate (float): The pseudo-random binary sequence (PRBS) bit rate.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:BRATe {bit_rate}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_prbs_data(self, source_num: int = 1) -> SourFuncShapPrbsData:
        """
        Sets the pseudo-random binary sequence (PRBS) type. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: The pseudo-random binary sequence (PRBS) type.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:DATA?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'sequence_type', 'type_options': ['SourFuncShapPrbsData']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_prbs_data(self, sequence_type: SourFuncShapPrbsData, source_num: int = 1) -> None:
        """
        Sets the pseudo-random binary sequence (PRBS) type. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sequence_type (str): The pseudo-random binary sequence (PRBS) type.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:DATA {sequence_type}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_prbs_transition_both(self, source_num: int = 1) -> float:
        """
        Sets PRBS transition edge time on both edges of a PRBS transition.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the pRBS transition edge time on both edges of a PRBS transition.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:TRANsition:BOTH?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_prbs_transition_both(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets PRBS transition edge time on both edges of a PRBS transition.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): PRBS transition edge time on both edges of a PRBS transition.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:TRANsition:BOTH {seconds}"
        self._rsrc.write(cmd)




    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_pulse_dcycle(self, source_num: int = 1) -> float:
        """
        Sets pulse duty cycle.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of pulse duty cycle.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:DCYCle?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'percent', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_pulse_dcycle(self, percent: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets pulse duty cycle.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            percent (float): Pulse duty cycle.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:DCYCle {percent}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_pulse_hold(self, source_num: int = 1) -> SourFuncShapPulsHold:
        """
        Sets the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:HOLD?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'pulse', 'type_options': ['SourFuncShapPulsHold']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_pulse_hold(self, pulse: SourFuncShapPulsHold, source_num: int = 1) -> None:
        """
        Sets the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            pulse (str): The pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:HOLD {pulse}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_pulse_period(self, source_num: int = 1) -> float:
        """
        Sets the period for pulse waveforms.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: The period for pulse waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:PERiod?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_pulse_period(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the period for pulse waveforms.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The period for pulse waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:PERiod {seconds}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_pulse_transition_both(self, source_num: int = 1) -> float:
        """
        Sets the pulse edge time on both edges of a pulse.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current pulse edge time on both edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:BOTH?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_pulse_transition_both(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the pulse edge time on both edges of a pulse.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The pulse edge time on both edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:BOTH {seconds}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_pulse_transition_leading(self, source_num: int = 1) -> float:
        """
        Sets the pulse edge time on the leading edges of a pulse.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the pulse edge time on the leading edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:LEADing?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_pulse_transition_leading(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the pulse edge time on the leading edges of a pulse.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The pulse edge time on the leading edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:LEADing {seconds}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_pulse_transition_trailing(self, source_num: int = 1) -> float:
        """
        Sets the pulse edge time on the trailing edges of a pulse.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the pulse edge time on the trailing edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:TRAiling?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_pulse_transition_trailing(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the pulse edge time on the trailing edges of a pulse.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The pulse edge time on the trailing edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:TRAiling {seconds}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_pulse_width(self, source_num: int = 1) -> float:
        """
        Sets pulse width.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the pulse width.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:WIDTh?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_pulse_width(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets pulse width.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The pulse width.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:WIDTh {seconds}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_ramp_symmetry(self, source_num: int = 1) -> float:
        """
        Sets the symmetry percentage for ramp waves.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the symmetry percentage for ramp waves.
        """
        cmd = f":SOURce{source_num}:FUNCtion:RAMP:SYMMetry?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'percent', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_ramp_symmetry(self, percent: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the symmetry percentage for ramp waves.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            percent (float): The symmetry percentage for ramp waves.
        """
        cmd = f":SOURce{source_num}:FUNCtion:RAMP:SYMMetry {percent}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_square_dcycle(self, source_num: int = 1) -> float:
        """
        Sets duty cycle percentage for square wave.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the duty cycle percentage for square wave.
        """
        cmd = f":SOURce{source_num}:FUNCtion:SQUare:DCYCle?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'percent', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_square_dcycle(self, percent: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets duty cycle percentage for square wave.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            percent (float): The duty cycle percentage for square wave.
        """
        cmd = f":SOURce{source_num}:FUNCtion:SQUare:DCYCle {percent}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_function_square_period(self, source_num: int = 1) -> float:
        """
        Sets period for square wave.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the period for square wave.
        """
        cmd = f":SOURce{source_num}:FUNCtion:SQUare:PERiod?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_function_square_period(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets period for square wave.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): Period for square wave.
        """
        cmd = f":SOURce{source_num}:FUNCtion:SQUare:PERiod {seconds}"
        self._rsrc.write(cmd)




    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_list_dwell(self, source_num: int = 1) -> float:
        """
        Sets dwell time, the amount of time each frequency in a frequency list is generated.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current dwell time.
        """
        cmd = f":SOURce{source_num}:LIST:DWELl?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_list_dwell(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets dwell time, the amount of time each frequency in a frequency list is generated.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The dwell time.
        """
        cmd = f":SOURce{source_num}:LIST:DWELl {seconds}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_list_frequency(self, source_num: int = 1) -> float:
        """
        Specifies frequency values in a frequency list.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current frequency values in a frequency list.
        """
        cmd = f":SOURce{source_num}:LIST:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_list_frequency(self, frequency: float, source_num: int = 1) -> None:
        """
        Specifies frequency values in a frequency list.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float):  frequency values in a frequency list. (Repeatable: *)
        """
        cmd = f":SOURce{source_num}:LIST:FREQuency {frequency}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_list_frequency_points(self, source_num: int = 1) -> int:
        """
        Returns number of frequencies in current frequency list.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            int: Returns number of frequencies in current frequency list.
        """
        cmd = f":SOURce{source_num}:LIST:FREQuency:POINts?"
        response = self._rsrc.query(cmd)
        return int(response)




    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_marker_cycle(self, source_num: int = 1) -> float:
        """
        Sets the marker cycle number at which the front-panel Sync signal goes low in a burst mode operation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current marker cycle number
        """
        cmd = f":SOURce{source_num}:MARKer:CYCLe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'cycle_num', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_marker_cycle(self, cycle_num: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the marker cycle number at which the front-panel Sync signal goes low in a burst mode operation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            cycle_num (float): The marker cycle number.
        """
        cmd = f":SOURce{source_num}:MARKer:CYCLe {cycle_num}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_marker_frequency(self, source_num: int = 1) -> float:
        """
        Sets the marker frequency at which the front-panel Sync signal goes low during a sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the marker frequency.
        """
        cmd = f":SOURce{source_num}:MARKer:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_marker_frequency(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the marker frequency at which the front-panel Sync signal goes low during a sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The marker frequency.
        """
        cmd = f":SOURce{source_num}:MARKer:FREQuency {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_marker_point(self, source_num: int = 1) -> float:
        """
        Sets the sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:MARKer:POINt?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'sample_number', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_marker_point(self, sample_number: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sample_number (float): The sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:MARKer:POINt {sample_number}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_modulation_phase(self, source_num: int = 1) -> float:
        """
        Sets the phase of the internal modulation source when modulating by the internal source with shape SIN, SQU, RAMP, NRAMp, or TRI. This command applies to the 336xx models only.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current phase of the internal modulation source when modulating by the internal source.
        """
        cmd = f":SOURce{source_num}:MODulation:PHASe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'angle', 'type_options': ['float', 'Enumminmaxdef']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_modulation_phase(self, angle: Union[float, Enumminmaxdef], source_num: int = 1) -> None:
        """
        Sets the phase of the internal modulation source when modulating by the internal source with shape SIN, SQU, RAMP, NRAMp, or TRI. This command applies to the 336xx models only.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            angle (float): The phase of the internal modulation source when modulating by the internal source.
        """
        cmd = f":SOURce{source_num}:MODulation:PHASe {angle}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def source_phase_reference(self, source_num: int = 1) -> None:
        """
        Simultaneously removes the offset set by PHASe and adjusts the primary phase generator by an amount equivalent to the PHASe setting.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":SOURce{source_num}:PHASe:REFerence"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def source_phase_synchronize(self, source_num: int = 1) -> None:
        """
        Simultaneously resets all phase generators in the instrument, including the modulation phase generators, to establish a common, internal phase zero reference point.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":SOURce{source_num}:PHASe:SYNChronize"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_phase_unlock_error_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables the generation of an error if the phase-lock is ever lost by the instrument timebase.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of the generation of phase-lock error.
        """
        cmd = f":SOURce{source_num}:PHASe:UNLock:ERRor:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_phase_unlock_error_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables the generation of an error if the phase-lock is ever lost by the instrument timebase.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the generation of phase-lock error.
        """
        cmd = f":SOURce{source_num}:PHASe:UNLock:ERRor:STATe {state}"
        self._rsrc.write(cmd)





    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pm_deviation(self, source_num: int = 1) -> float:
        """
        Sets the phase deviation in degrees. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current phase deviation in degrees.
        """
        cmd = f":SOURce{source_num}:PM:DEViation?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'deviation_in_degrees', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pm_deviation(self, deviation_in_degrees: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the phase deviation in degrees. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            deviation_in_degrees (float): The phase deviation in degrees.
        """
        cmd = f":SOURce{source_num}:PM:DEViation {deviation_in_degrees}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pm_internal_frequency(self, source_num: int = 1) -> float:
        """
        Sets the frequency of the modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the frequency of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:PM:INTernal:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pm_internal_frequency(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the frequency of the modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:PM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pm_internal_function(self, source_num: int = 1) -> SourAmIntFuncShapeclone:
        """
        Selects shape of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current shape of modulating waveform.
        """
        cmd = f":SOURce{source_num}:PM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'function', 'type_options': ['SourAmIntFuncShapeclone']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pm_internal_function(self, function: SourAmIntFuncShapeclone, source_num: int = 1) -> None:
        """
        Selects shape of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The shape of modulating waveform.
        """
        cmd = f":SOURce{source_num}:PM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pm_source(self, source_num: int = 1) -> SourPmSource:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce:PM:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourPmSource']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pm_source(self, source: SourPmSource, source_num: int = 1) -> None:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of the modulating signal.
        """
        cmd = f":SOURce:PM:SOURce {source}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pm_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of modulation function.
        """
        cmd = f":SOURce{source_num}:PM:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pm_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable modulation function.
        """
        cmd = f":SOURce{source_num}:PM:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pwm_deviation(self, source_num: int = 1) -> float:
        """
        Sets pulse width deviation; the ± variation in width (in seconds) from the pulse width of the carrier pulse waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the pulse width deviation.
        """
        cmd = f":SOURce{source_num}:PWM:DEViation?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'deviation', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pwm_deviation(self, deviation: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets pulse width deviation; the ± variation in width (in seconds) from the pulse width of the carrier pulse waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            deviation (float): The pulse width deviation.
        """
        cmd = f":SOURce{source_num}:PWM:DEViation {deviation}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pwm_deviation_dcycle(self, source_num: int = 1) -> float:
        """
        Sets duty cycle deviation in percent of period.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the duty cycle deviation in percent
        """
        cmd = f":SOURce{source_num}:PWM:DEViation:DCYCle?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'deviation_in_pct', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pwm_deviation_dcycle(self, deviation_in_pct: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets duty cycle deviation in percent of period.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            deviation_in_pct (float): The duty cycle deviation in percent.
        """
        cmd = f":SOURce{source_num}:PWM:DEViation:DCYCle {deviation_in_pct}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pwm_internal_frequency(self, source_num: int = 1) -> float:
        """
        Selects frequency at which output pulse width shifts through its pulse width deviation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the Frequency at which output pulse width shifts through its pulse width deviation. 
        """
        cmd = f":SOURce{source_num}:PWM:INTernal:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pwm_internal_frequency(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Selects frequency at which output pulse width shifts through its pulse width deviation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The Frequency at which output pulse width shifts through its pulse width deviation. 
        """
        cmd = f":SOURce{source_num}:PWM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pwm_internal_function(self, source_num: int = 1) -> SourAmIntFuncShapeclone:
        """
        Selects shape of the internal modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current shape of the internal modulating waveform.
        """
        cmd = f":SOURce{source_num}:PWM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'function', 'type_options': ['SourSumIntFunctionclone']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pwm_internal_function(self, function: SourSumIntFunctionclone, source_num: int = 1) -> None:
        """
        Selects shape of the internal modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The shape of the internal modulating waveform.
        """
        cmd = f":SOURce{source_num}:PWM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pwm_source(self, source_num: int = 1) -> SourPwmSource:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce:PWM:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourPwmSource']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pwm_source(self, source: SourPwmSource, source_num: int = 1) -> None:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of the modulating signal.
        """
        cmd = f":SOURce:PWM:SOURce {source}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_pwm_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of modulation function.
        """
        cmd = f":SOURce{source_num}:PWM:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_pwm_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disables modulation function.
        """
        cmd = f":SOURce{source_num}:PWM:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_rate_couple_mode(self, source_num: int = 1) -> SourRateCoupMode:
        """
        Sets type of sample rate coupling to either a constant sample rate offset (OFFSet) or a constant ratio (RATio) between the channels' sample rates.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the sample rate coupling mode
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:MODE?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mode', 'type_options': ['SourRateCoupMode']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_rate_couple_mode(self, mode: SourRateCoupMode, source_num: int = 1) -> None:
        """
        Sets type of sample rate coupling to either a constant sample rate offset (OFFSet) or a constant ratio (RATio) between the channels' sample rates.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The sample rate coupling mode
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:MODE {mode}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_rate_couple_offset(self, source_num: int = 1) -> float:
        """
        Sets sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:OFFSet?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'sample_rate', 'type_options': ['float']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_rate_couple_offset(self, sample_rate: float, source_num: int = 1) -> None:
        """
        Sets sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sample_rate (float): The sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:OFFSet {sample_rate}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_rate_couple_ratio(self, source_num: int = 1) -> float:
        """
        Sets offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:RATio?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'ratio', 'type_options': ['float']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_rate_couple_ratio(self, ratio: float, source_num: int = 1) -> None:
        """
        Sets offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            ratio (float): The offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:RATio {ratio}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_rate_couple_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables sample rate coupling between channels, or allows one-time copying of one channel's sample rate into the other channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of sample rate coupled state.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_rate_couple_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables sample rate coupling between channels, or allows one-time copying of one channel's sample rate into the other channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable sample rate coupled state.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:STATe {state}"
        self._rsrc.write(cmd)




    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_roscillator_source(self, source_num: int = 1) -> SourRoscSource:
        """
        Selects the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.
        """
        cmd = f":SOURce:ROSCillator:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourRoscSource']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_roscillator_source(self, source: SourRoscSource, source_num: int = 1) -> None:
        """
        Selects the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.
        """
        cmd = f":SOURce:ROSCillator:SOURce {source}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_roscillator_source_auto(self, source_num: int = 1) -> SourRoscSourAuto:
        """
        Disables or enables automatic selection of the reference oscillator.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the automatic selection of the reference oscillator.
        """
        cmd = f":SOURce:ROSCillator:SOURce:AUTO?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['SourRoscSourAuto']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_roscillator_source_auto(self, state: SourRoscSourAuto, source_num: int = 1) -> None:
        """
        Disables or enables automatic selection of the reference oscillator.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (str): Enable/disable the automatic selection of the reference oscillator.
        """
        cmd = f":SOURce:ROSCillator:SOURce:AUTO {state}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_roscillator_source_current(self, source_num: int = 1) -> SourRoscSourCurrent:
        """
        Indicates which reference oscillator signal is currently in use when ROSC:SOURce:AUTO is ON.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Determine reference signal source
        """
        cmd = f":SOURce:ROSCillator:SOURce:CURRent?"
        response = self._rsrc.query(cmd)
        return response




    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sum_amplitude(self, source_num: int = 1) -> float:
        """
        Sets internal modulation depth (or "percent modulation") in percent.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the internal SUM signal amplitude.
        """
        cmd = f":SOURce{source_num}:SUM:AMPLitude?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'amplitude', 'type_options': ['float']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sum_amplitude(self, amplitude: float, source_num: int = 1) -> None:
        """
        Sets internal modulation depth (or "percent modulation") in percent.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            amplitude (float): The internal SUM signal amplitude.
        """
        cmd = f":SOURce{source_num}:SUM:AMPLitude {amplitude}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sum_internal_frequency(self, source_num: int = 1) -> float:
        """
        Sets the frequency of the summing waveform when internal sum source is selected (SUM:SOURce:INTernal). 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current frequency of the summing waveform when internal sum source is selected.
        """
        cmd = f":SOURce{source_num}:SUM:INTernal:FREQuency?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'frequency', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sum_internal_frequency(self, frequency: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the frequency of the summing waveform when internal sum source is selected (SUM:SOURce:INTernal). 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): Sets the frequency of the summing waveform when internal sum source is selected.
        """
        cmd = f":SOURce{source_num}:SUM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sum_internal_function(self, source_num: int = 1) -> SourSumIntFunctionclone:
        """
        Selects the summing waveform (the waveform added to the primary waveform).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the summing waveform.
        """
        cmd = f":SOURce{source_num}:SUM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'function', 'type_options': ['SourSumIntFunctionclone']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sum_internal_function(self, function: SourSumIntFunctionclone, source_num: int = 1) -> None:
        """
        Selects the summing waveform (the waveform added to the primary waveform).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The summing waveform.
        """
        cmd = f":SOURce{source_num}:SUM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sum_source(self, source_num: int = 1) -> SourAmSource:
        """
        Selects source of summing signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of summing signal.
        """
        cmd = f":SOURce:SUM:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['SourAmSource']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sum_source(self, source: SourAmSource, source_num: int = 1) -> None:
        """
        Selects source of summing signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of summing signal.
        """
        cmd = f":SOURce:SUM:SOURce {source}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sum_state(self, source_num: int = 1) -> Boolean:
        """
        Disables or enables SUM function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of the SUM function.
        """
        cmd = f":SOURce{source_num}:SUM:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sum_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Disables or enables SUM function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the SUM function.
        """
        cmd = f":SOURce{source_num}:SUM:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sweep_htime(self, source_num: int = 1) -> float:
        """
        Sets number of seconds the sweep holds (pauses) at the stop frequency before returning to the start frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current sweep hold time
        """
        cmd = f":SOURce{source_num}:SWEep:HTIMe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'hold_time', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sweep_htime(self, hold_time: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets number of seconds the sweep holds (pauses) at the stop frequency before returning to the start frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            hold_time (float): The sweep hold time
        """
        cmd = f":SOURce{source_num}:SWEep:HTIMe {hold_time}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sweep_rtime(self, source_num: int = 1) -> float:
        """
        Sets number of seconds the sweep takes to return from stop frequency to start frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the sweep return time.
        """
        cmd = f":SOURce{source_num}:SWEep:RTIMe?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'return_time', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sweep_rtime(self, return_time: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets number of seconds the sweep takes to return from stop frequency to start frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            return_time (float): The sweep return time.
        """
        cmd = f":SOURce{source_num}:SWEep:RTIMe {return_time}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sweep_spacing(self, source_num: int = 1) -> SourSweSpacing:
        """
        Selects linear or logarithmic spacing for sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current sweep spacing.
        """
        cmd = f":SOURce{source_num}:SWEep:SPACing?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'spacing', 'type_options': ['SourSweSpacing']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sweep_spacing(self, spacing: SourSweSpacing, source_num: int = 1) -> None:
        """
        Selects linear or logarithmic spacing for sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            spacing (str): The sweep spacing.
        """
        cmd = f":SOURce{source_num}:SWEep:SPACing {spacing}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sweep_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables the sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of the sweep function.
        """
        cmd = f":SOURce{source_num}:SWEep:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sweep_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables the sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the sweep function.
        """
        cmd = f":SOURce{source_num}:SWEep:STATe {state}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_sweep_time(self, source_num: int = 1) -> float:
        """
        Sets time (seconds) to sweep from start frequency to stop frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current the sweep time.
        """
        cmd = f":SOURce{source_num}:SWEep:TIME?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'seconds', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_sweep_time(self, seconds: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets time (seconds) to sweep from start frequency to stop frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The sweep time.
        """
        cmd = f":SOURce{source_num}:SWEep:TIME {seconds}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_track(self, source_num: int = 1) -> SourTrack:
        """
        Causes channels 1 and 2 of a two-channel instrument to output the same signal, or an inverted polarity signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the two-channel instrument to output the same signal, or an inverted polarity signal.
        """
        cmd = f":SOURce{source_num}:TRACk?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'track', 'type_options': ['SourTrack']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_track(self, track: SourTrack, source_num: int = 1) -> None:
        """
        Causes channels 1 and 2 of a two-channel instrument to output the same signal, or an inverted polarity signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            track (str): Sets the two-channel instrument to output the same signal, or an inverted polarity signal.
        """
        cmd = f":SOURce{source_num}:TRACk {track}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage(self, source_num: int = 1) -> float:
        """
        Sets output amplitude.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of desired output amplitude in volts.
        """
        cmd = f":SOURce{source_num}:VOLTage?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'amplitude', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage(self, amplitude: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets output amplitude.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            amplitude (float): Desired output amplitude in volts.
        """
        cmd = f":SOURce{source_num}:VOLTage {amplitude}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_limit_high(self, source_num: int = 1) -> float:
        """
        Sets the high limits for output voltage.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the high limits for output voltage.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:HIGH?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'voltage', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_limit_high(self, voltage: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the high limits for output voltage.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): The high limits for output voltage.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:HIGH {voltage}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_limit_low(self, source_num: int = 1) -> float:
        """
        Sets the low limits for output voltage.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the low limits for output voltage.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:LOW?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'voltage', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_limit_low(self, voltage: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets the low limits for output voltage.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): The low limits for output voltage.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:LOW {voltage}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_limit_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables output amplitude voltage limits.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of output amplitude voltage limits.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_limit_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables output amplitude voltage limits.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disables output amplitude voltage limits.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_range_auto(self, source_num: int = 1) -> Boolean:
        """
        Disables or enables voltage autoranging for all functions.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of the voltage autoranging.
        """
        cmd = f":SOURce{source_num}:VOLTage:RANGe:AUTO?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['int', 'SourVoltRangAuto']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_range_auto(self, state: Union[int, SourVoltRangAuto], source_num: int = 1) -> None:
        """
        Disables or enables voltage autoranging for all functions.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (int): Enable/disable the voltage autoranging.
        """
        cmd = f":SOURce{source_num}:VOLTage:RANGe:AUTO {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_unit(self, source_num: int = 1) -> SourVoltLevUnit:
        """
        Selects the units for output amplitude.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of output amplitude units
        """
        cmd = f":SOURce{source_num}:VOLTage:UNIT?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'unit', 'type_options': ['SourVoltLevUnit']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_unit(self, unit: SourVoltLevUnit, source_num: int = 1) -> None:
        """
        Selects the units for output amplitude.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            unit (str): Output amplitude units
        """
        cmd = f":SOURce{source_num}:VOLTage:UNIT {unit}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_couple_state(self, source_num: int = 1) -> Boolean:
        """
        Enables or disables the maintaining of the same amplitude, offset, range, load, and units on both channels of a two-channel instrument. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            bool: Returns the current value of the maintaining of the same amplitude, offset, range, load, and units on both channels of a two-channel instrument.
        """
        cmd = f":SOURce{source_num}:VOLTage:COUPle:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_couple_state(self, state: Boolean, source_num: int = 1) -> None:
        """
        Enables or disables the maintaining of the same amplitude, offset, range, load, and units on both channels of a two-channel instrument. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the maintaining of the same amplitude, offset, range, load, and ns on both channels of a two-channel instrument.
        """
        cmd = f":SOURce{source_num}:VOLTage:COUPle:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_high(self, source_num: int = 1) -> float:
        """
        Set the waveform's high voltage levels.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the desired high voltage level.
        """
        cmd = f":SOURce{source_num}:VOLTage:HIGH?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'voltage', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_high(self, voltage: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Set the waveform's high voltage levels.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): The desired high voltage level.
        """
        cmd = f":SOURce{source_num}:VOLTage:HIGH {voltage}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_low(self, source_num: int = 1) -> float:
        """
        Set the waveform's low voltage levels.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the low voltage level for the specified channel.
        """
        cmd = f":SOURce{source_num}:VOLTage:LOW?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'voltage', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_low(self, voltage: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Set the waveform's low voltage levels.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): The low voltage level for the specified channel.
        """
        cmd = f":SOURce{source_num}:VOLTage:LOW {voltage}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_source_voltage_offset(self, source_num: int = 1) -> float:
        """
        Sets DC offset voltage.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the DC offset voltage for the specified channel.
        """
        cmd = f":SOURce{source_num}:VOLTage:OFFSet?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'offset', 'type_options': ['float', 'StdNumEnums']}, {'name': 'source_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_source_voltage_offset(self, offset: Union[float, StdNumEnums], source_num: int = 1) -> None:
        """
        Sets DC offset voltage.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            offset (float): The DC offset voltage for the specified channel.
        """
        cmd = f":SOURce{source_num}:VOLTage:OFFSet {offset}"
        self._rsrc.write(cmd)




    def get_status_operation_condition(self) -> int:
        """
        Queries the condition register for the Standard Operation Register group. 


        Returns:
            int: The condition register for the Standard Operation Register group.
        """
        cmd = f":STATus:OPERation:CONDition?"
        response = self._rsrc.query(cmd)
        return int(response)


    def get_status_operation_enable(self) -> int:
        """
        Enables bits in the enable register for the Standard Operation Register group.


        Returns:
            int: Returns the current value of enables bits in the enable register for the Standard Operation Register group.
        """
        cmd = f":STATus:OPERation:ENABle?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'enable_value', 'type_options': ['int']}]
    )
    def set_status_operation_enable(self, enable_value: int) -> None:
        """
        Enables bits in the enable register for the Standard Operation Register group.

        Args:
            enable_value (int): Enables bits in the enable register for the Standard Operation Register group.
        """
        cmd = f":STATus:OPERation:ENABle {enable_value}"
        self._rsrc.write(cmd)


    def get_status_operation_event(self) -> int:
        """
        Queries the event register for the Standard Operation Register group.


        Returns:
            int: The event register for the Standard Operation Register group.
        """
        cmd = f":STATus:OPERation:EVENt?"
        response = self._rsrc.query(cmd)
        return int(response)



    def status_preset(self) -> None:
        """
        Clears Questionable Data enable register and Standard Operation enable register.

        Args:
        """
        cmd = f":STATus:PRESet"
        self._rsrc.write(cmd)


    def get_status_questionable_condition(self) -> int:
        """
        Queries the condition register for the Questionable Data Register group.


        Returns:
            int: The condition register for the Questionable Data Register group
        """
        cmd = f":STATus:QUEStionable:CONDition?"
        response = self._rsrc.query(cmd)
        return int(response)


    def get_status_questionable_enable(self) -> int:
        """
        Enables bits in the enable register for the Questionable Data Register group. 


        Returns:
            int: Returns a decimal value equal to the binary-weighted sum of all bits set in the register.
        """
        cmd = f":STATus:QUEStionable:ENABle?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'enable_value', 'type_options': ['int']}]
    )
    def set_status_questionable_enable(self, enable_value: int) -> None:
        """
        Enables bits in the enable register for the Questionable Data Register group. 

        Args:
            enable_value (int): Enables bits in the enable register for the Questionable Data Register group. 
        """
        cmd = f":STATus:QUEStionable:ENABle {enable_value}"
        self._rsrc.write(cmd)


    def get_status_questionable_event(self) -> int:
        """
        Queries the event register for the Questionable Data Register group. 


        Returns:
            int: The event register for the Questionable Data Register group.
        """
        cmd = f":STATus:QUEStionable:EVENt?"
        response = self._rsrc.query(cmd)
        return int(response)




    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def system_beeper_immediate(self, system_num: int = 1) -> None:
        """
        Issues a single beep.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:BEEPer:IMMediate"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_beeper_state(self, system_num: int = 1) -> Boolean:
        """
        Disables or enables the beeper tone heard when an error is generated from the front panel or remote interface. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            bool: Returns the current value of the beeper state.
        """
        cmd = f":SYSTem{system_num}:BEEPer:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_beeper_state(self, state: Boolean, system_num: int = 1) -> None:
        """
        Disables or enables the beeper tone heard when an error is generated from the front panel or remote interface. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            state (bool): Enable/disable the beeper state.
        """
        cmd = f":SYSTem{system_num}:BEEPer:STATe {state}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_enable(self, system_num: int = 1) -> Boolean:
        """
        Disables or enables the GPIB, USB, or LAN remote interface.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            bool: Returns the current value of the interface state.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:ENABle?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'interface', 'type_options': ['SystCommEnableCommandParameter2clone']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_enable(self, state: Boolean, interface: SystCommEnableCommandParameter2clone, system_num: int = 1) -> None:
        """
        Disables or enables the GPIB, USB, or LAN remote interface.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            state (bool): Enable/disable the interface state.
            interface (str): Interface
        """
        cmd = f":SYSTem{system_num}:COMMunicate:ENABle {state}, {interface}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_gpib_address(self, system_num: int = 1) -> int:
        """
        Assigns instrument's GPIB (IEEE-488) address, which is displayed at power-on. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            int: Returns the current value of the instrument's GPIB instrument address.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:GPIB:ADDRess?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'address', 'type_options': ['int']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_gpib_address(self, address: int, system_num: int = 1) -> None:
        """
        Assigns instrument's GPIB (IEEE-488) address, which is displayed at power-on. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            address (int): The instrument's GPIB instrument address.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:GPIB:ADDRess {address}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_control(self, system_num: int = 1) -> int:
        """
        Reads the initial Control connection port number for Sockets communications.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            int: The initial Control connection port number
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:CONTrol?"
        response = self._rsrc.query(cmd)
        return int(response)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_dhcp(self, system_num: int = 1) -> Boolean:
        """
        Disables or enables instrument's use of DHCP.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            bool: Returns the current value of the instrument's use of DHCP.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:DHCP?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'state', 'type_options': ['Boolean']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_dhcp(self, state: Boolean, system_num: int = 1) -> None:
        """
        Disables or enables instrument's use of DHCP.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            state (bool): Enable/disable the instrument's use of DHCP.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:DHCP {state}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}, {'name': 'dns_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_dns(self, system_num: int = 1, dns_num: int = 1) -> str:
        """
        Assigns static IP addresses of Domain Name System (DNS) servers.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            dns_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the static IP addresses of Domain Name System (DNS) servers.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:DNS{dns_num}?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'address', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}, {'name': 'dns_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_dns(self, address: str, system_num: int = 1, dns_num: int = 1) -> None:
        """
        Assigns static IP addresses of Domain Name System (DNS) servers.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            dns_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            address (str): The static IP addresses of Domain Name System (DNS) servers.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:DNS{dns_num} {address}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_domain(self, system_num: int = 1) -> str:
        """
        Returns the domain name of the LAN to which the instrument is connected.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the domain name of the LAN to which the instrument is connected.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:DOMain?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_gateway(self, system_num: int = 1) -> str:
        """
        Assigns a default gateway for the instrument.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the current value of the default gateway which allows the instrument to communicate with systems that are not on the local subnet.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:GATeway?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'address', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_gateway(self, address: str, system_num: int = 1) -> None:
        """
        Assigns a default gateway for the instrument.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            address (str): The default gateway which allows the instrument to communicate with systems that are not on the local subnet.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:GATeway {address}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_hostname(self, system_num: int = 1) -> str:
        """
        Assigns a hostname to the instrument.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the current hostname.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:HOSTname?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'name', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_hostname(self, name: str, system_num: int = 1) -> None:
        """
        Assigns a hostname to the instrument.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            name (str): The hostname.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:HOSTname {name}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_ipaddress(self, system_num: int = 1) -> str:
        """
        Assigns a static Internet Protocol (IP) address for the instrument. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the current static Internet Protocol (IP) address.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:IPADdress?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'address', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_ipaddress(self, address: str, system_num: int = 1) -> None:
        """
        Assigns a static Internet Protocol (IP) address for the instrument. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            address (str): A static Internet Protocol (IP) address.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:IPADdress {address}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_mac(self, system_num: int = 1) -> str:
        """
        Reads the instrument's Media Access Control (MAC) address.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: The instrument's Media Access Control (MAC) address.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:MAC?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_smask(self, system_num: int = 1) -> str:
        """
        Assigns a subnet mask for the instrument. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the current subnet mask.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:SMASk?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'mask', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_smask(self, mask: str, system_num: int = 1) -> None:
        """
        Assigns a subnet mask for the instrument. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            mask (str): The subnet mask.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:SMASk {mask}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_telnet_prompt(self, system_num: int = 1) -> str:
        """
        Sets the command prompt seen when communicating with the instrument via Telnet.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the current value of the command prompt seen when communicating with the instrument via Telnet.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:TELNet:PROMpt?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'string', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_telnet_prompt(self, string: str, system_num: int = 1) -> None:
        """
        Sets the command prompt seen when communicating with the instrument via Telnet.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            string (str): The command prompt seen when communicating with the instrument via Telnet.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:TELNet:PROMpt {string}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_telnet_wmessage(self, system_num: int = 1) -> str:
        """
        Sets welcome message seen when communicating with instrument via Telnet.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the current welcome message.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:TELNet:WMESsage?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'string', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_telnet_wmessage(self, string: str, system_num: int = 1) -> None:
        """
        Sets welcome message seen when communicating with instrument via Telnet.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            string (str): The welcome message.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:TELNet:WMESsage {string}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def system_communicate_lan_update(self, system_num: int = 1) -> None:
        """
        Stores any changes made to the LAN settings into non-volatile memory and restarts the LAN driver with the updated settings.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:UPDate"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}, {'name': 'wins_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_communicate_lan_wins(self, system_num: int = 1, wins_num: int = 1) -> str:
        """
        Assigns the static IP addresses of the Windows Internet Name System (WINS) servers.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            wins_num (int): Windows Internet Name System (WINS) server number. (Range: 1-2)

        Returns:
            str: Returns the static IP addresses of the Windows Internet Name System (WINS) servers.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:WINS{wins_num}?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'address', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}, {'name': 'wins_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_communicate_lan_wins(self, address: str, system_num: int = 1, wins_num: int = 1) -> None:
        """
        Assigns the static IP addresses of the Windows Internet Name System (WINS) servers.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            wins_num (int): Windows Internet Name System (WINS) server number. (Range: 1-2)
            address (str): The static IP addresses of the Windows Internet Name System (WINS) servers.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:WINS{wins_num} {address}"
        self._rsrc.write(cmd)




    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_date(self, system_num: int = 1) -> int:
        """
        Sets system clock date.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            int: Returns the current value of the year.
            int: Returns the current value of the month.
            int: Returns the current value of the day.
        """
        cmd = f":SYSTem{system_num}:DATE?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'year', 'type_options': ['int']}, {'name': 'month', 'type_options': ['int']}, {'name': 'day', 'type_options': ['int']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_date(self, year: int, month: int, day: int, system_num: int = 1) -> None:
        """
        Sets system clock date.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            year (int): The year.
            month (int): The month.
            day (int): The day.
        """
        cmd = f":SYSTem{system_num}:DATE {year}, {month}, {day}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_error(self, system_num: int = 1) -> int:
        """
        Reads and clears one error from error queue.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            int: A three-digit code.
            str: A string that describes the type of error.
        """
        cmd = f":SYSTem{system_num}:ERRor?"
        response = self._rsrc.query(cmd)
        return int(response)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_license_catalog(self, system_num: int = 1) -> str:
        """
        Returns a comma separated list of installed, licensed options.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Return currently licensed options.
        """
        cmd = f":SYSTem{system_num}:LICense:CATalog?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'option_name', 'type_options': ['SystLicsDel']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_license_delete(self, option_name: SystLicsDel, system_num: int = 1) -> None:
        """
        Deletes a license.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            option_name (str): Deletes a license.
        """
        cmd = f":SYSTem{system_num}:LICense:DELete {option_name}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def system_license_delete_all(self, system_num: int = 1) -> None:
        """
        Deletes all licenses.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:LICense:DELete:ALL"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_license_description(self, system_num: int = 1) -> str:
        """
        Returns a description of specified option, regardless of whether it is currently licensed.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns a description of specified option.
        """
        cmd = f":SYSTem{system_num}:LICense:DESCription?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_license_error(self, system_num: int = 1) -> NDArray[Any]:
        """
        Returns a string of all the errors produced by SYSTem:LICense:INSTall.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            NDArray[Any]: Return the license installation error string.
        """
        cmd = f":SYSTem{system_num}:LICense:ERRor?"
        response = self._rsrc.query(cmd)
        return np.array(response)

    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_license_error_count(self, system_num: int = 1) -> int:
        """
        Returns the number of license errors generated by SYSTem:LICense:INSTall.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            int: Return number of license errors.
        """
        cmd = f":SYSTem{system_num}:LICense:ERRor:COUNt?"
        response = self._rsrc.query(cmd)
        return int(response)



    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_license_install(self, system_num: int = 1) -> Boolean:
        """
        This command installs all licenses from a specified file or from all license files in the specified folder. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            bool: Returns 0 or 1 to indicate whether the specified license is installed.
        """
        cmd = f":SYSTem{system_num}:LICense:INSTall?"
        response = self._rsrc.query(cmd)
        return bool(response)

    @validate_parameters(
        rules_list=[{'name': 'fileFolder', 'type_options': ['str']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_license_install(self, fileFolder: str, system_num: int = 1) -> None:
        """
        This command installs all licenses from a specified file or from all license files in the specified folder. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            fileFolder (str): The file or folder to install licenses from.
        """
        cmd = f":SYSTem{system_num}:LICense:INSTall {fileFolder}"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_lock_name(self, system_num: int = 1) -> str:
        """
        Returns the current I/O interface (the I/O interface in use by the querying computer).

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the current I/O interface.
        """
        cmd = f":SYSTem{system_num}:LOCK:NAME?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_lock_owner(self, system_num: int = 1) -> str:
        """
        Returns the I/O interface that currently has a lock.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Returns the I/O interface that currently has a lock.
        """
        cmd = f":SYSTem{system_num}:LOCK:OWNer?"
        response = self._rsrc.query(cmd)
        return response


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def system_lock_release(self, system_num: int = 1) -> None:
        """
        Decrements the lock count by 1 and may release the I/O interface from which the command is executed.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:LOCK:RELease"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_lock_request(self, system_num: int = 1) -> Boolean:
        """
        Requests a lock of the current I/O interface.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            bool: Requests a lock of the current I/O interface.
        """
        cmd = f":SYSTem{system_num}:LOCK:REQuest?"
        response = self._rsrc.query(cmd)
        return bool(response)



    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def system_security_immediate(self, system_num: int = 1) -> None:
        """
        Sanitizes all user-accessible instrument memory.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:SECurity:IMMediate"
        self._rsrc.write(cmd)



    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_time(self, system_num: int = 1) -> int:
        """
        Sets system clock time.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            int: Returns the hour.
            int: Returns the minute.
            float: Returns the seconds.
        """
        cmd = f":SYSTem{system_num}:TIME?"
        response = self._rsrc.query(cmd)
        return int(response)

    @validate_parameters(
        rules_list=[{'name': 'hour', 'type_options': ['int']}, {'name': 'minute', 'type_options': ['int']}, {'name': 'seconds', 'type_options': ['float']}, {'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_system_time(self, hour: int, minute: int, seconds: float, system_num: int = 1) -> None:
        """
        Sets system clock time.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            hour (int): The hour.
            minute (int): The minute.
            seconds (float): The seconds.
        """
        cmd = f":SYSTem{system_num}:TIME {hour}, {minute}, {seconds}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'system_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_system_version(self, system_num: int = 1) -> str:
        """
        Returns version of the SCPI (Standard Commands for Programmable Instruments) that the instrument complies with. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)

        Returns:
            str: Return the SCPI version.
        """
        cmd = f":SYSTem{system_num}:VERSion?"
        response = self._rsrc.query(cmd)
        return response



    @validate_parameters(
        rules_list=[{'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def trigger(self, trigger_num: int = 1) -> None:
        """
        Forces immediate trigger to initiate sequence, sweep, list, or burst.

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":TRIGger{trigger_num}"
        self._rsrc.write(cmd)

    @validate_parameters(
        rules_list=[{'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_trigger_count(self, trigger_num: int = 1) -> float:
        """
        Sets trigger count.

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current value of the trigger count.
        """
        cmd = f":TRIGger{trigger_num}:COUNt?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'number', 'type_options': ['float']}, {'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_trigger_count(self, number: float, trigger_num: int = 1) -> None:
        """
        Sets trigger count.

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            number (float): The trigger count.
        """
        cmd = f":TRIGger{trigger_num}:COUNt {number}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_trigger_delay(self, trigger_num: int = 1) -> float:
        """
        Sets trigger delay, (time from assertion of trigger to occurrence of triggered event).

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current trigger delay time.
        """
        cmd = f":TRIGger{trigger_num}:DELay?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'delay', 'type_options': ['float', 'StdNumEnums']}, {'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_trigger_delay(self, delay: Union[float, StdNumEnums], trigger_num: int = 1) -> None:
        """
        Sets trigger delay, (time from assertion of trigger to occurrence of triggered event).

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            delay (float): Trigger delay time.
        """
        cmd = f":TRIGger{trigger_num}:DELay {delay}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_trigger_timer(self, trigger_num: int = 1) -> float:
        """
        Sets timer used when TRIGger[1|2]:SOURce is TIMer.

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            float: Returns the current trigger timer.
        """
        cmd = f":TRIGger{trigger_num}:TIMer?"
        response = self._rsrc.query(cmd)
        return float(response)

    @validate_parameters(
        rules_list=[{'name': 'timer', 'type_options': ['float', 'StdNumEnums']}, {'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_trigger_timer(self, timer: Union[float, StdNumEnums], trigger_num: int = 1) -> None:
        """
        Sets timer used when TRIGger[1|2]:SOURce is TIMer.

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            timer (float): The trigger timer.
        """
        cmd = f":TRIGger{trigger_num}:TIMer {timer}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_trigger_slope(self, trigger_num: int = 1) -> TrigSeqSlope:
        """
        Specifies polarity of trigger signal on rear-panel Trig In connector for any externally-triggered mode. 

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current trigger slope.
        """
        cmd = f":TRIGger{trigger_num}:SLOPe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'edge', 'type_options': ['TrigSeqSlope']}, {'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_trigger_slope(self, edge: TrigSeqSlope, trigger_num: int = 1) -> None:
        """
        Specifies polarity of trigger signal on rear-panel Trig In connector for any externally-triggered mode. 

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            edge (str): POSitive|NEGative.
        """
        cmd = f":TRIGger{trigger_num}:SLOPe {edge}"
        self._rsrc.write(cmd)


    @validate_parameters(
        rules_list=[{'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def get_trigger_source(self, trigger_num: int = 1) -> TrigSeqSource:
        """
        Selects the trigger source for sequence, list, burst or sweep. 

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current trigger source.
        """
        cmd = f":TRIGger{trigger_num}:SOURce?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'source', 'type_options': ['TrigSeqSource']}, {'name': 'trigger_num', 'type_options': ['int'], 'min_val': 1, 'max_val': 2}]
    )
    def set_trigger_source(self, source: TrigSeqSource, trigger_num: int = 1) -> None:
        """
        Selects the trigger source for sequence, list, burst or sweep. 

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            source (str): IMMediate|EXTernal|TIMer|BUS.
        """
        cmd = f":TRIGger{trigger_num}:SOURce {source}"
        self._rsrc.write(cmd)



    def get_unit_angle(self) -> UnitAngleclone:
        """
        Specifies the angle units that displayed on the screen and used for specifying angles.


        Returns:
            str: Returns the current angle units.
        """
        cmd = f":UNIT:ANGLe?"
        response = self._rsrc.query(cmd)
        return response

    @validate_parameters(
        rules_list=[{'name': 'unit', 'type_options': ['UnitAngleclone']}]
    )
    def set_unit_angle(self, unit: UnitAngleclone) -> None:
        """
        Specifies the angle units that displayed on the screen and used for specifying angles.

        Args:
            unit (str): DEGree|RADian|SECond|DEFault.
        """
        cmd = f":UNIT:ANGLe {unit}"
        self._rsrc.write(cmd)




# For basic testing or example usage:
if __name__ == '__main__':
    # This section is for demonstration and won't run in a typical import scenario.
    # To use the driver:
    # 1. Ensure you have a VISA backend installed (e.g., NI-VISA, pyvisa-py).
    # 2. Connect your instrument.
    # 3. Instantiate the class:
    #    instrument = Keysight33500B(visa_address='YOUR_INSTRUMENT_VISA_ADDRESS')
    #    # Example: instrument = Keysight33500B(visa_address='GPIB0::10::INSTR')
    #
    # 4. Call methods:
    #    # idn = instrument.get_idn() # If *IDN? is defined and generates get_idn()
    #    # print(idn)
    #    # instrument.set_output1_function(Output1Function.SIN) # Example assuming such methods
    
    print(f"Class 'Keysight33500B' is defined in this file.")
    print(f"To use it, import it into your script and instantiate with a VISA address.")