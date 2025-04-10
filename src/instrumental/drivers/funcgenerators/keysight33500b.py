from enum import Enum
from typing import Any, Union, overload
import pyvisa
import numpy as np

# Generated SCPI enums from SDL file
# This file is auto-generated. Do not edit manually.

class Enum33500bStdNumEnums(Enum):
    """
    Enum for enum_33500B_std_num_enums
    """

    MINIMUM = 1
    # Aliases: MIN

    MAXIMUM = 2
    # Aliases: MAX



class DispWindFocusCommandParameter1(Enum):
    """
    Enum for disp_wind_focus_command_parameter_1
    """

    CH1 = 0

    CH2 = 1



class DispWindFocusQueryResponse1(Enum):
    """
    Enum for disp_wind_focus_query_response_1
    """

    CH1 = 0

    CH2 = 1



class DispWindUnitArbrateCommandParameter1(Enum):
    """
    Enum for disp_wind_unit_arbrate_command_parameter_1
    """

    SRATE = 0
    # Aliases: SRAT

    FREQUENCY = 1
    # Aliases: FREQ

    PERIOD = 2
    # Aliases: PER



class DispWindUnitArbrateQueryResponse1(Enum):
    """
    Enum for disp_wind_unit_arbrate_query_response_1
    """

    SRATE = 0
    # Aliases: SRAT

    FREQUENCY = 1
    # Aliases: FREQ

    PERIOD = 2
    # Aliases: PER



class DispWindUnitPulseCommandParameter1(Enum):
    """
    Enum for disp_wind_unit_pulse_command_parameter_1
    """

    WIDTH = 0
    # Aliases: WID

    DUTY = 1
    # Aliases: DUT



class DispWindUnitPulseQueryResponse1(Enum):
    """
    Enum for disp_wind_unit_pulse_query_response_1
    """

    WIDTH = 0
    # Aliases: WID

    DUTY = 1
    # Aliases: DUT



class DispWindUnitRateCommandParameter1(Enum):
    """
    Enum for disp_wind_unit_rate_command_parameter_1
    """

    FREQUENCY = 0
    # Aliases: FREQ

    PERIOD = 1
    # Aliases: PER



class DispWindUnitRateQueryResponse1(Enum):
    """
    Enum for disp_wind_unit_rate_query_response_1
    """

    FREQUENCY = 0
    # Aliases: FREQ

    PERIOD = 1
    # Aliases: PER



class DispWindUnitSweepCommandParameter1(Enum):
    """
    Enum for disp_wind_unit_sweep_command_parameter_1
    """

    STARTSTOP = 0
    # Aliases: STAR

    CENTERSPAN = 1
    # Aliases: CENT



class DispWindUnitSweepQueryResponse1(Enum):
    """
    Enum for disp_wind_unit_sweep_query_response_1
    """

    STARTSTOP = 0
    # Aliases: STAR

    CENTERSPAN = 1
    # Aliases: CENT



class DispWindUnitVoltageCommandParameter1(Enum):
    """
    Enum for disp_wind_unit_voltage_command_parameter_1
    """

    AMPLITUDEOFF = 0
    # Aliases: AMPL

    HIGHLOW = 1
    # Aliases: HIGH



class DispWindUnitVoltageQueryResponse1(Enum):
    """
    Enum for disp_wind_unit_voltage_query_response_1
    """

    AMPLITUDEOFF = 0
    # Aliases: AMPL

    HIGHLOW = 1
    # Aliases: HIGH



class DispWindViewCommandParameter1(Enum):
    """
    Enum for disp_wind_view_command_parameter_1
    """

    STANDARD = 0
    # Aliases: STAN

    TEXT = 1

    GRAPH = 2

    DUAL = 3



class DispWindViewQueryResponse1(Enum):
    """
    Enum for disp_wind_view_query_response_1
    """

    STANDARD = 0
    # Aliases: STAN

    TEXT = 1

    GRAPH = 2

    DUAL = 3



class FormBorderCommandParameter1(Enum):
    """
    Enum for form_border_command_parameter_1
    """

    NORMAL = 0
    # Aliases: NORM

    SWAPPED = 1
    # Aliases: SWAP



class FormBorderQueryResponse1(Enum):
    """
    Enum for form_border_query_response_1
    """

    NORMAL = 0
    # Aliases: NORM

    SWAPPED = 1
    # Aliases: SWAP



class HcopSdumDataFormatCommandParameter1(Enum):
    """
    Enum for hcop_sdum_data_format_command_parameter_1
    """

    BMP = 0

    PNG = 1



class Enum33500bEnumminmaxdefinf(Enum):
    """
    Enum for enum_33500B_enumMinMaxDefInf
    """

    MINIMUM = 1
    # Aliases: MIN

    MAXIMUM = 2
    # Aliases: MAX

    INFINITY = 7
    # Aliases: INF



class OutpModeCommandParameter1(Enum):
    """
    Enum for outp_mode_command_parameter_1
    """

    NORMAL = 0
    # Aliases: NORM

    GATED = 1
    # Aliases: GAT



class OutpModeQueryResponse1(Enum):
    """
    Enum for outp_mode_query_response_1
    """

    NORMAL = 0
    # Aliases: NORM

    GATED = 1
    # Aliases: GAT



class OutpPolarityCommandParameter1(Enum):
    """
    Enum for outp_polarity_command_parameter_1
    """

    NORMAL = 0
    # Aliases: NORM

    INVERTED = 1
    # Aliases: INV



class OutpPolarityQueryResponse1(Enum):
    """
    Enum for outp_polarity_query_response_1
    """

    NORMAL = 0
    # Aliases: NORM

    INVERTED = 1
    # Aliases: INV



class OutpSyncModeCommandParameter1(Enum):
    """
    Enum for outp_sync_mode_command_parameter_1
    """

    NORMAL = 0
    # Aliases: NORM

    CARRIER = 1
    # Aliases: CARR

    MARKER = 2
    # Aliases: MARK



class OutpSyncModeQueryResponse1(Enum):
    """
    Enum for outp_sync_mode_query_response_1
    """

    NORMAL = 0
    # Aliases: NORM

    CARRIER = 1
    # Aliases: CARR

    MARKER = 2
    # Aliases: MARK



class OutpSyncPolarityCommandParameter1(Enum):
    """
    Enum for outp_sync_polarity_command_parameter_1
    """

    NORMAL = 0
    # Aliases: NORM

    INVERTED = 1
    # Aliases: INV



class OutpSyncPolarityQueryResponse1(Enum):
    """
    Enum for outp_sync_polarity_query_response_1
    """

    NORMAL = 0
    # Aliases: NORM

    INVERTED = 1
    # Aliases: INV



class OutpSyncSourceCommandParameter1(Enum):
    """
    Enum for outp_sync_source_command_parameter_1
    """

    CH1 = 0

    CH2 = 1



class OutpSyncSourceQueryResponse1(Enum):
    """
    Enum for outp_sync_source_query_response_1
    """

    CH1 = 0

    CH2 = 1



class OutpTrigSlopeCommandParameter1(Enum):
    """
    Enum for outp_trig_slope_command_parameter_1
    """

    POSITIVE = 1
    # Aliases: POS

    NEGATIVE = 2
    # Aliases: NEG



class OutpTrigSlopeQueryResponse1(Enum):
    """
    Enum for outp_trig_slope_query_response_1
    """

    POSITIVE = 1
    # Aliases: POS

    NEGATIVE = 2
    # Aliases: NEG



class OutpTrigSourceCommandParameter1(Enum):
    """
    Enum for outp_trig_source_command_parameter_1
    """

    CH1 = 0

    CH2 = 1



class OutpTrigSourceQueryResponse1(Enum):
    """
    Enum for outp_trig_source_query_response_1
    """

    CH1 = 0

    CH2 = 1



class Enum33500bEnumminmaxdef(Enum):
    """
    Enum for enum_33500B_enumMinMaxDef
    """

    MINIMUM = 1
    # Aliases: MIN

    MAXIMUM = 2
    # Aliases: MAX



class SourAmSourceCommandParameter1(Enum):
    """
    Enum for sour_am_source_command_parameter_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT

    CH1 = 2

    CH2 = 3



class SourAmSourceQueryResponse1(Enum):
    """
    Enum for sour_am_source_query_response_1
    """

    INTERNAL = 0
    # Aliases: INT BOTH

    EXTERNAL = 1
    # Aliases: EXT

    CH1 = 2

    CH2 = 3



class SourBursGatePolarityCommandParameter1(Enum):
    """
    Enum for sour_burs_gate_polarity_command_parameter_1
    """

    NORMAL = 0
    # Aliases: NORM

    INVERTED = 1
    # Aliases: INV



class SourBursGatePolarityQueryResponse1(Enum):
    """
    Enum for sour_burs_gate_polarity_query_response_1
    """

    NORMAL = 0
    # Aliases: NORM

    INVERTED = 1
    # Aliases: INV



class SourBursModeCommandParameter1(Enum):
    """
    Enum for sour_burs_mode_command_parameter_1
    """

    TRIGGERED = 0
    # Aliases: TRIG

    GATED = 1
    # Aliases: GAT



class SourBursModeQueryResponse1(Enum):
    """
    Enum for sour_burs_mode_query_response_1
    """

    TRIGGERED = 0
    # Aliases: TRIG

    GATED = 1
    # Aliases: GAT



class SourCombFeedCommandParameter1(Enum):
    """
    Enum for sour_comb_feed_command_parameter_1
    """

    CH1 = 0

    CH2 = 1

    NONE = 2



class SourCombFeedQueryResponse1(Enum):
    """
    Enum for sour_comb_feed_query_response_1
    """

    CH1 = 0

    CH2 = 1

    NONE = 2



class SourceDataArb2FormatCommandParameter1(Enum):
    """
    Enum for source_data_arb2_format_command_parameter_1
    """

    AABB = 0

    ABAB = 1



class SourceDataArb2FormatQueryResponse1(Enum):
    """
    Enum for source_data_arb2_format_query_response_1
    """

    AABB = 0

    ABAB = 1



class SourFmSourceCommandParameter1(Enum):
    """
    Enum for sour_fm_source_command_parameter_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT

    CH1 = 2

    CH2 = 3



class SourFmSourceQueryResponse1(Enum):
    """
    Enum for sour_fm_source_query_response_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT

    CH1 = 2

    CH2 = 3



class SourFreqCoupModeCommandParameter1(Enum):
    """
    Enum for sour_freq_coup_mode_command_parameter_1
    """

    OFFSET = 0
    # Aliases: OFFS

    RATIO = 1
    # Aliases: RAT



class SourFreqCoupModeQueryResponse1(Enum):
    """
    Enum for sour_freq_coup_mode_query_response_1
    """

    OFFSET = 0
    # Aliases: OFFS

    RATIO = 1
    # Aliases: RAT



class SourFreqModeCommandParameter1(Enum):
    """
    Enum for sour_freq_mode_command_parameter_1
    """

    FIXED = 0
    # Aliases: FIX

    SWEEP = 2
    # Aliases: SWE

    CW = 3

    LIST = 4



class SourFreqModeQueryResponse1(Enum):
    """
    Enum for sour_freq_mode_query_response_1
    """

    FIXED = 0
    # Aliases: FIX

    SWEEP = 2
    # Aliases: SWE

    LIST = 4

    CW = 3



class SourFuncShapArbAdvanceCommandParameter1(Enum):
    """
    Enum for sour_func_shap_arb_advance_command_parameter_1
    """

    TRIGGER = 0
    # Aliases: TRIG

    SRATE = 1
    # Aliases: SRAT



class SourFuncShapArbAdvanceQueryResponse1(Enum):
    """
    Enum for sour_func_shap_arb_advance_query_response_1
    """

    TRIGGER = 0
    # Aliases: TRIG

    SRATE = 1
    # Aliases: SRAT



class SourFuncShapArbFilterCommandParameter1(Enum):
    """
    Enum for sour_func_shap_arb_filter_command_parameter_1
    """

    OFF = 0

    NORMAL = 1
    # Aliases: NORM

    STEP = 2



class SourFuncShapArbFilterQueryResponse1(Enum):
    """
    Enum for sour_func_shap_arb_filter_query_response_1
    """

    OFF = 0

    NORMAL = 1
    # Aliases: NORM

    STEP = 2



class SourFuncShapPrbsDataCommandParameter1(Enum):
    """
    Enum for sour_func_shap_prbs_data_command_parameter_1
    """

    PN7 = 0

    PN9 = 1

    PN11 = 2

    PN15 = 3

    PN20 = 4

    PN23 = 5



class SourFuncShapPrbsDataQueryResponse1(Enum):
    """
    Enum for sour_func_shap_prbs_data_query_response_1
    """

    PN7 = 0

    PN9 = 1

    PN11 = 2

    PN15 = 3

    PN20 = 4

    PN23 = 5



class SourFuncShapPulsHoldCommandParameter1(Enum):
    """
    Enum for sour_func_shap_puls_hold_command_parameter_1
    """

    WIDTH = 0
    # Aliases: WIDT

    DCYCLE = 1
    # Aliases: DCYC



class SourFuncShapPulsHoldQueryResponse1(Enum):
    """
    Enum for sour_func_shap_puls_hold_query_response_1
    """

    WIDTH = 0
    # Aliases: WIDT

    DCYCLE = 1
    # Aliases: DCYC



class SourPmSourceCommandParameter1(Enum):
    """
    Enum for sour_pm_source_command_parameter_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT

    CH1 = 2

    CH2 = 3



class SourPmSourceQueryResponse1(Enum):
    """
    Enum for sour_pm_source_query_response_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT

    CH1 = 2

    CH2 = 3



class SourPwmSourceCommandParameter1(Enum):
    """
    Enum for sour_pwm_source_command_parameter_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT

    CH1 = 2

    CH2 = 3



class SourPwmSourceQueryResponse1(Enum):
    """
    Enum for sour_pwm_source_query_response_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT

    CH1 = 2

    CH2 = 3



class SourRateCoupModeCommandParameter1(Enum):
    """
    Enum for sour_rate_coup_mode_command_parameter_1
    """

    OFFSET = 0
    # Aliases: OFFS

    RATIO = 1
    # Aliases: RAT



class SourRateCoupModeQueryResponse1(Enum):
    """
    Enum for sour_rate_coup_mode_query_response_1
    """

    OFFSET = 0
    # Aliases: OFFS

    RATIO = 1
    # Aliases: RAT



class SourRoscSourceCommandParameter1(Enum):
    """
    Enum for sour_rosc_source_command_parameter_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT



class SourRoscSourceQueryResponse1(Enum):
    """
    Enum for sour_rosc_source_query_response_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT



class SourRoscSourAutoCommandParameter1(Enum):
    """
    Enum for sour_rosc_sour_auto_command_parameter_1
    """

    OFF = 0

    ON = 1



class SourRoscSourAutoQueryResponse1(Enum):
    """
    Enum for sour_rosc_sour_auto_query_response_1
    """

    OFF = 0

    ON = 1



class SourRoscSourCurrentQueryResponse1(Enum):
    """
    Enum for sour_rosc_sour_current_query_response_1
    """

    INTERNAL = 0
    # Aliases: INT

    EXTERNAL = 1
    # Aliases: EXT



class SourSweSpacingCommandParameter1(Enum):
    """
    Enum for sour_swe_spacing_command_parameter_1
    """

    LINEAR = 0
    # Aliases: LIN

    LOGARITHMIC = 1
    # Aliases: LOG



class SourSweSpacingQueryResponse1(Enum):
    """
    Enum for sour_swe_spacing_query_response_1
    """

    LINEAR = 0
    # Aliases: LIN

    LOGARITHMIC = 1
    # Aliases: LOG



class SourTrackCommandParameter1(Enum):
    """
    Enum for sour_track_command_parameter_1
    """

    OFF = 0

    ON = 1

    INVERTED = 2
    # Aliases: INV



class SourTrackQueryResponse1(Enum):
    """
    Enum for sour_track_query_response_1
    """

    OFF = 0

    ON = 1

    INVERTED = 2
    # Aliases: INV



class SourVoltLevUnitCommandParameter1(Enum):
    """
    Enum for sour_volt_lev_unit_command_parameter_1
    """

    VPP = 0
    # Aliases: DEFault DEF

    VRMS = 1

    DBM = 2



class SourVoltLevUnitQueryResponse1(Enum):
    """
    Enum for sour_volt_lev_unit_query_response_1
    """

    VPP = 0
    # Aliases: DEFault DEF

    VRMS = 1

    DBM = 2



class SourVoltRangAutoCommandParameter1(Enum):
    """
    Enum for sour_volt_rang_auto_command_parameter_1
    """

    OFF = 0

    ON = 1

    ONCE = 2



class Enum33500bEnumstaticcurrent(Enum):
    """
    Enum for enum_33500B_enumStaticCurrent
    """

    STATIC = 0
    # Aliases: STAT

    CURRENT = 1
    # Aliases: CURR



class TrigSeqSlopeCommandParameter1(Enum):
    """
    Enum for trig_seq_slope_command_parameter_1
    """

    POSITIVE = 0
    # Aliases: POS

    NEGATIVE = 1
    # Aliases: NEG



class TrigSeqSlopeQueryResponse1(Enum):
    """
    Enum for trig_seq_slope_query_response_1
    """

    POSITIVE = 0
    # Aliases: POS

    NEGATIVE = 1
    # Aliases: NEG



class TrigSeqSourceCommandParameter1(Enum):
    """
    Enum for trig_seq_source_command_parameter_1
    """

    IMMEDIATE = 0
    # Aliases: IMM

    EXTERNAL = 1
    # Aliases: EXT

    BUS = 2

    TIMER = 3
    # Aliases: TIM



class TrigSeqSourceQueryResponse1(Enum):
    """
    Enum for trig_seq_source_query_response_1
    """

    IMMEDIATE = 0
    # Aliases: IMM

    EXTERNAL = 1
    # Aliases: EXT

    BUS = 2

    TIMER = 3
    # Aliases: TIM



class Enum33500bBoolean(Enum):
    """
    Enum for enum_33500B_boolean
    """

    ON = 1

    OFF = 0



class UnitAngleCommandParameter1clone(Enum):
    """
    Enum for unit_angle_command_parameter_1Clone
    """

    DEGREE = 0
    # Aliases: DEG

    RADIAN = 1
    # Aliases: RAD

    SECOND = 2
    # Aliases: SEC

    DEFAULT = 3
    # Aliases: DEF



class Enum33500bStdNumEnumsclone(Enum):
    """
    Enum for enum_33500B_std_num_enumsClone
    """

    MINIMUM = 1
    # Aliases: MIN

    MAXIMUM = 2
    # Aliases: MAX

    DEFAULT = 3
    # Aliases: DEF



class Enum33500bStdNumEnumscloneclone(Enum):
    """
    Enum for enum_33500B_std_num_enumsCloneClone
    """

    DEFAULT = 3
    # Aliases: DEF



class SourAmSourceCommandParameter1clone(Enum):
    """
    Enum for sour_am_source_command_parameter_1Clone
    """

    INTERNAL = 0
    # Aliases: INT BOTH

    EXTERNAL = 1
    # Aliases: EXT



class SystCommEnableCommandParameter2clone(Enum):
    """
    Enum for syst_comm_enable_command_parameter_2Clone
    """

    GPIB = 0

    USB = 1

    LAN = 2

    SOCKETS = 3
    # Aliases: SOCK

    TELNET = 4
    # Aliases: TELN

    VXI11 = 5

    WEB = 6



class SourAmIntFuncShapeCommandParameter1clone(Enum):
    """
    Enum for sour_am_int_func_shape_command_parameter_1Clone
    """

    SINUSOID = 0
    # Aliases: SIN

    SQUARE = 1
    # Aliases: SQU

    TRIANGLE = 2
    # Aliases: TRI

    RAMP = 3

    NRAMP = 4
    # Aliases: NRAM

    NOISE = 5
    # Aliases: NOIS

    PRBS = 6

    ARB = 7



class SourFuncShapeCommandParameter1clone(Enum):
    """
    Enum for sour_func_shape_command_parameter_1Clone
    """

    SINUSOID = 0
    # Aliases: SIN

    SQUARE = 1
    # Aliases: SQU

    RAMP = 2

    PULSE = 3
    # Aliases: PULS

    ARB = 4

    TRIANGLE = 5
    # Aliases: TRI

    NOISE = 6
    # Aliases: NOIS

    PRBS = 7

    DC = 8



class SourSumIntFunctionCommandParameter1clone(Enum):
    """
    Enum for sour_sum_int_function_command_parameter_1Clone
    """

    SINUSOID = 0
    # Aliases: SIN

    SQUARE = 1
    # Aliases: SQU

    TRIANGLE = 2
    # Aliases: TRI

    RAMP = 3

    NRAMP = 4
    # Aliases: NRAM

    NOISE = 5
    # Aliases: NOIS

    PRBS = 6

    ARB = 7



class SystCommEnableCommandParameter2clone2(Enum):
    """
    Enum for syst_comm_enable_command_parameter_2Clone_2
    """

    SEC = 0

    IQP = 1

    MEM = 2

    BW30 = 3




# Generated SCPI command syntax enums
# These enums represent different syntax variants for commands that support multiple formats

class SourceDataArbitrarySyntax(Enum):
    """
    Enum for command syntaxes of SOURce:DATA:ARBitrary
    """

    BLOCKREAL32 = "BlockReal32"
    # Parameters:
    #   - arb_name (String)
    #     Description: The arbitrary sequence to be downloaded to.
    #   - binary_block (1-D Array)
    #     Description: List of values to be downloaded into waveform memory.

    ASCII = "Ascii"
    # Parameters:
    #   - arb_name (String)
    #     Description: The arbitrary sequence to be downloaded to.
    #   - value (Real)
    #     Description: List of values to be downloaded into waveform memory.
    #     Repeat: *



class SourceDataArbitraryDacSyntax(Enum):
    """
    Enum for command syntaxes of SOURce:DATA:ARBitrary:DAC
    """

    ASCII = "Ascii"
    # Parameters:
    #   - arb_name (String)
    #     Description: The arbitrary sequence name to be downloaded to.
    #   - value (Integer)
    #     Description: The DAC codes to be loaded into waveform memory as a list of integers.
    #     Repeat: *

    BLOCKINT16 = "BlockInt16"
    # Parameters:
    #   - arb_name (String)
    #     Description: The arbitrary sequence name to be downloaded to.
    #   - binary_block (1-D Array)
    #     Description: Binary block data.



class SourceDataArbitrary2Syntax(Enum):
    """
    Enum for command syntaxes of SOURce:DATA:ARBitrary2
    """

    BLOCKREAL32 = "BlockReal32"
    # Parameters:
    #   - arb_name (String)
    #     Description: The arbitrary sequence to be downloaded to.
    #   - binary_block (1-D Array)
    #     Description: List of values to be downloaded into waveform memory.

    ASCII = "Ascii"
    # Parameters:
    #   - arb_name (String)
    #     Description: The arbitrary sequence to be downloaded to.
    #   - value (Real)
    #     Description: List of values to be downloaded into waveform memory.
    #     Repeat: *



class SourceDataArbitrary2DacSyntax(Enum):
    """
    Enum for command syntaxes of SOURce:DATA:ARBitrary2:DAC
    """

    ASCII = "Ascii"
    # Parameters:
    #   - arb_name (String)
    #     Description: The arbitrary sequence name to be downloaded to.
    #   - value (Integer)
    #     Description: The DAC codes to be loaded into waveform memory as a list of integers.
    #     Repeat: *

    BLOCKINT16 = "BlockInt16"
    # Parameters:
    #   - arb_name (String)
    #     Description: The arbitrary sequence name to be downloaded to.
    #   - binary_block (1-D Array)
    #     Description: Binary block data.




# Main Keysight33500B class
# This class provides access to all SCPI commands and subsystems

from instrumental.drivers import VisaMixin
from instrumental.drivers.funcgenerators import FunctionGenerator
import numpy as np
from numpy.typing import NDArray

class Keysight33500B(FunctionGenerator, VisaMixin):
    """Main class for controlling the Keysight 33500B_program_reference/33500B function generators."""
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('Agilent Technologies', ['33509B', '33510B', '33511B', '33512B', '33519B', '33520B', '33521B', '33522B', '33609A', '33610A', '33611A', '33612A', '33619A', '33620A', '33621A', '33622A'])

    def _initialize(self):
        self._rsrc.timeout = 2000  # 2 second timeout
        self._rsrc.write_termination = '\n'
        self._rsrc.read_termination = '\n'


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


    def cls(self):
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


    def set_ese(self, enable_value: int):
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
        return str(response)


    def get_opc(self) -> int:
        """
        Sets "Operation Complete" (bit 0) in the Standard Event register at the completion of the current operation. Returns 1 to the output buffer after all pending commands complete.


        Returns:
            int: Returns returns "1" to the output buffer when the current operation completes.
        """
        cmd = f"*OPC?"
        response = self._rsrc.query(cmd)
        return int(response)


    def opc(self):
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
        return str(response)


    def get_psc(self) -> Enum33500bBoolean:
        """
        Power-On Status Clear. Enables (1) or disables (0) clearing of two specific registers at power on.


        Returns:
            int: Returns the current state of the Power-On Status Clear.
        """
        cmd = f"*PSC?"
        response = self._rsrc.query(cmd)
        return int(response)


    def set_psc(self, psc: int):
        """
        Power-On Status Clear. Enables (1) or disables (0) clearing of two specific registers at power on.

        Args:
            psc (int): 0|1.
        """
        cmd = f"*PSC {psc}"
        self._rsrc.write(cmd)


    def set_rcl(self, rcl: int):
        """
        Recalls (*RCL) instrument state in specified non-volatile location.

        Args:
            rcl (int): 0|1|2|3|4.
        """
        cmd = f"*RCL {rcl}"
        self._rsrc.write(cmd)


    def rst(self):
        """
        Resets instrument to factory default state.

        Args:
        """
        cmd = f"*RST"
        self._rsrc.write(cmd)


    def set_sav(self, sav: int):
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


    def set_sre(self, enable_value: int):
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


    def trg(self):
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


    def wai(self):
        """
        Configures the instrument to wait for all pending operations to complete before executing any additional commands over the interface.

        Args:
        """
        cmd = f"*WAI"
        self._rsrc.write(cmd)



   # Generated SCPI subsystem methods
   # These methods provide a Pythonic interface to SCPI commands

    def abort(self):
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

    def set_calibration_secure_code(self, new_code: str):
        """
        Sets the security code to prevent unauthorized calibrations.

        Args:
            new_code (str): The new security code.
        """
        cmd = f":CALibration:SECure:CODE {new_code}"
        self._rsrc.write(cmd)

    def get_calibration_secure_state(self) -> Enum33500bBoolean:
        """
        Unsecures or secures the instrument for calibration. 


        Returns:
            bool: Returns the current state of the instrument for calibration.
        """
        cmd = f":CALibration:SECure:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    def set_calibration_secure_state(self, state: Enum33500bBoolean, code: str):
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

    def set_calibration_setup(self, step: int):
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
        return str(response)

    def set_calibration_string(self, string: str):
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

    def set_calibration_value(self, value: float):
        """
        Specifies the value of the known calibration signal.

        Args:
            value (float): The calibration value.
        """
        cmd = f":CALibration:VALue {value}"
        self._rsrc.write(cmd)



    def get_display(self) -> Enum33500bBoolean:
        """
        Disables or enables the front-panel display.


        Returns:
            bool: Returns the current state of the front-panel display.
        """
        cmd = f":DISPlay?"
        response = self._rsrc.query(cmd)
        return bool(response)

    def set_display(self, state: Enum33500bBoolean):
        """
        Disables or enables the front-panel display.

        Args:
            state (bool): ON|1|OFF|0.
        """
        cmd = f":DISPlay {state}"
        self._rsrc.write(cmd)

    def get_display_focus(self) -> DispWindFocusQueryResponse1:
        """
        selects the channel displayed "in front" on a two-channel instrument 


        Returns:
            str: Returns the current selected the channel that is displayed "in front" on a two-channel instrument.
        """
        cmd = f":DISPlay:FOCus?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_display_focus(self, focus: DispWindFocusCommandParameter1):
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
        return str(response)

    def set_display_text(self, string: str):
        """
        Displays a text message on the front-panel display.   

        Args:
            string (str): Displays a text message on the front-panel display.
        """
        cmd = f":DISPlay:TEXT {string}"
        self._rsrc.write(cmd)

    def display_text_clear(self):
        """
        Clears the text message from the front-panel display.

        Args:
        """
        cmd = f":DISPlay:TEXT:CLEar"
        self._rsrc.write(cmd)

    def get_display_unit_arbrate(self) -> DispWindUnitArbrateQueryResponse1:
        """
        Specifies whether the rate units for arbitrary waveforms are samples per second, (SRATe), Hz (FREQ) or seconds (PER).


        Returns:
            str: Returns the current units for arbitrary waveforms.
        """
        cmd = f":DISPlay:UNIT:ARBRate?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_display_unit_arbrate(self, arbrate: DispWindUnitArbrateCommandParameter1):
        """
        Specifies whether the rate units for arbitrary waveforms are samples per second, (SRATe), Hz (FREQ) or seconds (PER).

        Args:
            arbrate (str): SRATe|FREQuency|PERiod
        """
        cmd = f":DISPlay:UNIT:ARBRate {arbrate}"
        self._rsrc.write(cmd)

    def get_display_unit_pulse(self) -> DispWindUnitPulseQueryResponse1:
        """
        Selects the method for specifying pulse duration.


        Returns:
            str: Returns the current method for specifying pulse duration.
        """
        cmd = f":DISPlay:UNIT:PULSe?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_display_unit_pulse(self, pulse: DispWindUnitPulseCommandParameter1):
        """
        Selects the method for specifying pulse duration.

        Args:
            pulse (str): WIDTh|DUTY.
        """
        cmd = f":DISPlay:UNIT:PULSe {pulse}"
        self._rsrc.write(cmd)

    def get_display_unit_rate(self) -> DispWindUnitRateQueryResponse1:
        """
        Specifies whether the rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).


        Returns:
            str: Returns the current rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).
        """
        cmd = f":DISPlay:UNIT:RATE?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_display_unit_rate(self, rate: DispWindUnitRateCommandParameter1):
        """
        Specifies whether the rate units for sine, square, ramp, pulse, and triangle waves are Hz (FREQ) or seconds (PER).

        Args:
            rate (str): FREQuency|PERiod.
        """
        cmd = f":DISPlay:UNIT:RATE {rate}"
        self._rsrc.write(cmd)

    def get_display_unit_sweep(self) -> DispWindUnitSweepQueryResponse1:
        """
        Selects the method for specifying sweep frequency range.


        Returns:
            str: Returns the current method for specifying sweep frequency range.
        """
        cmd = f":DISPlay:UNIT:SWEep?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_display_unit_sweep(self, sweep: DispWindUnitSweepCommandParameter1):
        """
        Selects the method for specifying sweep frequency range.

        Args:
            sweep (str): STARtstop|CENTerspan.
        """
        cmd = f":DISPlay:UNIT:SWEep {sweep}"
        self._rsrc.write(cmd)

    def get_display_unit_voltage(self) -> DispWindUnitVoltageQueryResponse1:
        """
        Selects the method for specifying voltage ranges.


        Returns:
            str: Returns the current method for specifying voltage ranges.
        """
        cmd = f":DISPlay:UNIT:VOLTage?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_display_unit_voltage(self, voltage: DispWindUnitVoltageCommandParameter1):
        """
        Selects the method for specifying voltage ranges.

        Args:
            voltage (str): AMPLitudeoffset|HIGHlow.
        """
        cmd = f":DISPlay:UNIT:VOLTage {voltage}"
        self._rsrc.write(cmd)

    def get_display_view(self) -> DispWindViewQueryResponse1:
        """
        Selects the screen layout.


        Returns:
            str: Returns the current screen layout.
        """
        cmd = f":DISPlay:VIEW?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_display_view(self, view: DispWindViewCommandParameter1):
        """
        Selects the screen layout.

        Args:
            view (str): STANdard|TEXT|GRAPh|DUAL.
        """
        cmd = f":DISPlay:VIEW {view}"
        self._rsrc.write(cmd)



    def get_format_border(self) -> FormBorderQueryResponse1:
        """
        Sets the byte order used in binary data point transfers in the block mode.


        Returns:
            str: Returns the current byte order.
        """
        cmd = f":FORMat:BORDer?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_format_border(self, border: FormBorderCommandParameter1):
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
        return str(response)

    def set_hcopy_sdump_data_format(self, format: HcopSdumDataFormatCommandParameter1):
        """
        Specifies the image format for images returned by HCOPy:SDUMp:DATA?.

        Args:
            format (str): PNG|BMP.
        """
        cmd = f":HCOPy:SDUMp:DATA:FORMat {format}"
        self._rsrc.write(cmd)



    def get_initiate_continuous(self, initiate_num: int = 1) -> Enum33500bBoolean:
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

    def set_initiate_continuous(self, state: Enum33500bBoolean, initiate_num: int = 1):
        """
        Specifies whether the trigger system for one channel always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0
        """
        cmd = f":INITiate{initiate_num}:CONTinuous {state}"
        self._rsrc.write(cmd)

    def set_initiate_continuous_all(self, state: Enum33500bBoolean, initiate_num: int = 1):
        """
        Specifies whether the trigger system for both channels (ALL) always returns to the "wait-for-trigger" state (ON) or remains in the "idle" state (OFF), ignoring triggers until INITiate:IMMediate is issued.

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)
            state (bool): The current state of the function.
        """
        cmd = f":INITiate{initiate_num}:CONTinuous:ALL {state}"
        self._rsrc.write(cmd)

    def initiate_immediate(self, initiate_num: int = 1):
        """
        Change state of triggering system for both channels (ALL) from "idle" to "wait-for-trigger" for the number of triggers specified by TRIGger[1|2]:COUNt.

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":INITiate{initiate_num}:IMMediate"
        self._rsrc.write(cmd)

    def initiate_immediate_all(self, initiate_num: int = 1):
        """
        Change state of triggering system for both channels (ALL) from "idle" to "wait-for-trigger" for the number of triggers specified by TRIGger[1|2]:COUNt

        Args:
            initiate_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":INITiate{initiate_num}:IMMediate:ALL"
        self._rsrc.write(cmd)



    def get_lxi_identify_state(self) -> Enum33500bBoolean:
        """
        Turns the LXI Identify Indicator on the display on or off.


        Returns:
            bool: Returns the current state of the LXI Identify Indicator display.
        """
        cmd = f":LXI:IDENtify:STATe?"
        response = self._rsrc.query(cmd)
        return bool(response)

    def set_lxi_identify_state(self, state: Enum33500bBoolean):
        """
        Turns the LXI Identify Indicator on the display on or off.

        Args:
            state (bool): ON|1|OFF|0.
        """
        cmd = f":LXI:IDENtify:STATe {state}"
        self._rsrc.write(cmd)

    def get_lxi_mdns_enable(self) -> Enum33500bBoolean:
        """
        Disables or enables the Multicast Domain Name System (mDNS).


        Returns:
            bool: Returns the current state of the Multicast Domain Name System (mDNS).
        """
        cmd = f":LXI:MDNS:ENABle?"
        response = self._rsrc.query(cmd)
        return bool(response)

    def set_lxi_mdns_enable(self, state: Enum33500bBoolean):
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
        return str(response)

    def get_lxi_mdns_sname_desired(self) -> str:
        """
        Sets the desired mDNS service name.


        Returns:
            str: Returns the desired mDNS service name.
        """
        cmd = f":LXI:MDNS:SNAMe:DESired?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_lxi_mdns_sname_desired(self, name: str):
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
        return str(response)

    def lxi_reset(self):
        """
        Resets LAN settings to a known operating state, beginning with DHCP. 

        Args:
        """
        cmd = f":LXI:RESet"
        self._rsrc.write(cmd)

    def lxi_restart(self):
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
        return str(response)

    def set_memory_state_delete(self, location: int):
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
        return str(response)

    def set_memory_state_name(self, sLocation: int, name: str):
        """
        Names a storage location. 

        Args:
            sLocation (int): 0|1|2|3|4.
            name (str): Names a storage location. 
        """
        cmd = f":MEMory:STATe:NAME {sLocation}, {name}"
        self._rsrc.write(cmd)

    def get_memory_state_recall_auto(self) -> Enum33500bBoolean:
        """
        Disables or enables automatic recall of instrument state in storage location "0" at power on.


        Returns:
            bool: Returns the current state of automatic recall of instrument state.
        """
        cmd = f":MEMory:STATe:RECall:AUTO?"
        response = self._rsrc.query(cmd)
        return bool(response)

    def set_memory_state_recall_auto(self, state: Enum33500bBoolean):
        """
        Disables or enables automatic recall of instrument state in storage location "0" at power on.

        Args:
            state (bool): ON|1|OFF|0.
        """
        cmd = f":MEMory:STATe:RECall:AUTO {state}"
        self._rsrc.write(cmd)

    def get_memory_state_valid(self) -> Enum33500bBoolean:
        """
        Indicates whether a valid state is currently stored in a storage location.


        Returns:
            bool: Return state of memory location.
        """
        cmd = f":MEMory:STATe:VALid?"
        response = self._rsrc.query(cmd)
        return bool(response)



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
        return str(response)

    def set_mmemory_cdirectory(self, folder: str, mmemory_num: int = 1):
        """
        MMEMory:CDIRectory selects the default folder for the MMEMory subsystem commands. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            folder (str): The default folder for the MMEMory subsystem commands.
        """
        cmd = f":MMEMory{mmemory_num}:CDIRectory {folder}"
        self._rsrc.write(cmd)

    def set_mmemory_copy(self, file1: str, file2: str, mmemory_num: int = 1):
        """
        Copies <file1> to <file2>. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            file1 (str): The source file name.
            file2 (str): The destination file name.
        """
        cmd = f":MMEMory{mmemory_num}:COPY {file1}, {file2}"
        self._rsrc.write(cmd)

    def set_mmemory_copy_sequence(self, source: str, destination: str, mmemory_num: int = 1):
        """
        Copies a sequence from <source> to <destination>. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source.
            destination (str): The destination.
        """
        cmd = f":MMEMory{mmemory_num}:COPY:SEQuence {source}, {destination}"
        self._rsrc.write(cmd)

    def set_mmemory_delete(self, file: str, mmemory_num: int = 1):
        """
        Deletes a file. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            file (str): The file to be deleted.
        """
        cmd = f":MMEMory{mmemory_num}:DELete {file}"
        self._rsrc.write(cmd)

    def set_mmemory_download_data(self, binary_block: Union[bytes] | None, mmemory_num: int = 1):
        """
        Downloads data from the host computer to a file in the instrument.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            binary_block (Union[bytes] | None): Any IEEE-488 definite or indefinite block.
        """
        cmd = f":MMEMory{mmemory_num}:DOWNload:DATA {binary_block}"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_mmemory_download_fname(self, filename: str, mmemory_num: int = 1):
        """
        Creates or opens the specified filename prior to writing data to that file with MMEMory:DOWNload:DATA.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name.
        """
        cmd = f":MMEMory{mmemory_num}:DOWNload:FNAMe {filename}"
        self._rsrc.write(cmd)

    def set_mmemory_load_all(self, filename: str, mmemory_num: int = 1):
        """
        Loads a complete instrument setup, using a named file on the mass storage.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name on current mass storage directory.
        """
        cmd = f":MMEMory{mmemory_num}:LOAD:ALL {filename}"
        self._rsrc.write(cmd)

    def set_mmemory_load_data(self, filename: str, mmemory_num: int = 1, data_num: int = 1):
        """
        Loads the specified arb segment(.arb/.barb) or arb sequence (.seq) file in INTERNAL or USB memory into volatile memory for the specified channel.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            data_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name.
        """
        cmd = f":MMEMory{mmemory_num}:LOAD:DATA{data_num} {filename}"
        self._rsrc.write(cmd)

    def set_mmemory_load_list(self, filename: str, mmemory_num: int = 1, list_num: int = 1):
        """
        Loads a frequency list file (.lst).

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            list_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name on the mass memory device.
        """
        cmd = f":MMEMory{mmemory_num}:LOAD:LIST{list_num} {filename}"
        self._rsrc.write(cmd)

    def set_mmemory_load_state(self, filename: str, mmemory_num: int = 1):
        """
        Stores the current instrument state to a state file. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): The state file to load the instrument from.
        """
        cmd = f":MMEMory{mmemory_num}:LOAD:STATe {filename}"
        self._rsrc.write(cmd)

    def set_mmemory_mdirectory(self, folder: str, mmemory_num: int = 1):
        """
        MMEMory:MDIRectory makes a new directory (folder) on the mass storage medium.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            folder (str): The new folder to be created.
        """
        cmd = f":MMEMory{mmemory_num}:MDIRectory {folder}"
        self._rsrc.write(cmd)

    def set_mmemory_move(self, file1: str, file2: str, mmemory_num: int = 1):
        """
        Moves and/or renames <file1> to <file2>. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            file1 (str): The source file.
            file2 (str): The destination file.
        """
        cmd = f":MMEMory{mmemory_num}:MOVE {file1}, {file2}"
        self._rsrc.write(cmd)

    def set_mmemory_rdirectory(self, folder: str, mmemory_num: int = 1):
        """
        MMEMory:RDIRectory removes a directory (folder) on the mass storage medium.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            folder (str): The folder to be removed.
        """
        cmd = f":MMEMory{mmemory_num}:RDIRectory {folder}"
        self._rsrc.write(cmd)

    def set_mmemory_store_all(self, filename: str, mmemory_num: int = 1):
        """
        Loads or saves a complete instrument setup, using a named file on the mass storage.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name on current mass storage directory.
        """
        cmd = f":MMEMory{mmemory_num}:STORe:ALL {filename}"
        self._rsrc.write(cmd)

    def set_mmemory_store_data(self, filename: str, mmemory_num: int = 1, data_num: int = 1):
        """
        Stores the specified arb segment(.arb/.barb) or arb sequence (.seq) data in the channel specified volatile memory (default, channel 1) in INTERNAL or USB memory.

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            data_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name.
        """
        cmd = f":MMEMory{mmemory_num}:STORe:DATA{data_num} {filename}"
        self._rsrc.write(cmd)

    def set_mmemory_store_list(self, filename: str, mmemory_num: int = 1, list_num: int = 1):
        """
        Loads or stores a frequency list file (.lst).

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            list_num (int): The channel number identifier. (Range: 1-2)
            filename (str): The file name to store the currently loaded frequency list in.
        """
        cmd = f":MMEMory{mmemory_num}:STORe:LIST{list_num} {filename}"
        self._rsrc.write(cmd)

    def set_mmemory_store_state(self, filename: str, mmemory_num: int = 1):
        """
        Stores the current instrument state to a state file. 

        Args:
            mmemory_num (int): The channel number identifier. (Range: 1-2)
            filename (str): Any valid file name on the current directory.
        """
        cmd = f":MMEMory{mmemory_num}:STORe:STATe {filename}"
        self._rsrc.write(cmd)

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



    def get_output(self, output_num: int = 1) -> Enum33500bBoolean:
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

    def set_output(self, state: Enum33500bBoolean, output_num: int = 1):
        """
        Enables or disables the front-panel output connector.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":OUTPut{output_num} {state}"
        self._rsrc.write(cmd)

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

    def set_output_load(self, ohms: Union[float, Enum33500bEnumminmaxdefinf], output_num: int = 1):
        """
        Sets expected output termination.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            ohms (float): The expected output termination.
        """
        cmd = f":OUTPut{output_num}:LOAD {ohms}"
        self._rsrc.write(cmd)

    def get_output_mode(self, output_num: int = 1) -> OutpModeQueryResponse1:
        """
        Enables (GATed) or disables (NORMal) gating of the output waveform signal on and off using the trigger input.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the mode.
        """
        cmd = f":OUTPut{output_num}:MODE?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_output_mode(self, mode: OutpModeCommandParameter1, output_num: int = 1):
        """
        Enables (GATed) or disables (NORMal) gating of the output waveform signal on and off using the trigger input.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            mode (str): NORMal|GATed.
        """
        cmd = f":OUTPut{output_num}:MODE {mode}"
        self._rsrc.write(cmd)

    def get_output_polarity(self, output_num: int = 1) -> OutpPolarityQueryResponse1:
        """
        Inverts waveform relative to the offset voltage.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the polarity.
        """
        cmd = f":OUTPut{output_num}:POLarity?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_output_polarity(self, polarity: OutpPolarityCommandParameter1, output_num: int = 1):
        """
        Inverts waveform relative to the offset voltage.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            polarity (str): NORMal|INVerted.
        """
        cmd = f":OUTPut{output_num}:POLarity {polarity}"
        self._rsrc.write(cmd)

    def get_output_sync(self, output_num: int = 1) -> Enum33500bBoolean:
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

    def set_output_sync(self, state: Enum33500bBoolean, output_num: int = 1):
        """
        Disables or enables the front-panel Sync connector.  

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":OUTPut{output_num}:SYNC {state}"
        self._rsrc.write(cmd)

    def get_output_sync_mode(self, output_num: int = 1) -> OutpSyncModeQueryResponse1:
        """
        Specifies normal Sync behavior (NORMal), forces Sync to follow the carrier waveform (CARRier), or indicates marker position (MARKer).

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the mode.
        """
        cmd = f":OUTPut{output_num}:SYNC:MODE?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_output_sync_mode(self, mode: OutpSyncModeCommandParameter1, output_num: int = 1):
        """
        Specifies normal Sync behavior (NORMal), forces Sync to follow the carrier waveform (CARRier), or indicates marker position (MARKer).

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            mode (str): NORMal|CARRier|MARKer
        """
        cmd = f":OUTPut{output_num}:SYNC:MODE {mode}"
        self._rsrc.write(cmd)

    def get_output_sync_polarity(self, output_num: int = 1) -> OutpSyncPolarityQueryResponse1:
        """
        Sets the desired output polarity of the Sync output to trigger external equipment that may require falling or rising edge triggers.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the desired output polarity of the Sync output.
        """
        cmd = f":OUTPut{output_num}:SYNC:POLarity?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_output_sync_polarity(self, polarity: OutpSyncPolarityCommandParameter1, output_num: int = 1):
        """
        Sets the desired output polarity of the Sync output to trigger external equipment that may require falling or rising edge triggers.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            polarity (str): NORMal|INVerted
        """
        cmd = f":OUTPut{output_num}:SYNC:POLarity {polarity}"
        self._rsrc.write(cmd)

    def get_output_sync_source(self, output_num: int = 1) -> OutpSyncSourceQueryResponse1:
        """
        Sets the source for the Sync output connector.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the source for the Sync output connector.
        """
        cmd = f":OUTPut{output_num}:SYNC:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_output_sync_source(self, channel: OutpSyncSourceCommandParameter1, output_num: int = 1):
        """
        Sets the source for the Sync output connector.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            channel (str): CH1|CH2
        """
        cmd = f":OUTPut{output_num}:SYNC:SOURce {channel}"
        self._rsrc.write(cmd)

    def get_output_trigger(self, output_num: int = 1) -> Enum33500bBoolean:
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

    def set_output_trigger(self, state: Enum33500bBoolean, output_num: int = 1):
        """
        Disables or enables the "trigger out" signal for sweep and burst modes.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":OUTPut{output_num}:TRIGger {state}"
        self._rsrc.write(cmd)

    def get_output_trigger_slope(self, output_num: int = 1) -> OutpTrigSlopeQueryResponse1:
        """
        Selects whether the instrument uses the rising edge or falling edge for the "trigger out" signal.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns whether the instrument uses the rising edge or falling edge for the "trigger out" signal.
        """
        cmd = f":OUTPut{output_num}:TRIGger:SLOPe?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_output_trigger_slope(self, edge: OutpTrigSlopeCommandParameter1, output_num: int = 1):
        """
        Selects whether the instrument uses the rising edge or falling edge for the "trigger out" signal.

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            edge (str): POSitive|NEGative
        """
        cmd = f":OUTPut{output_num}:TRIGger:SLOPe {edge}"
        self._rsrc.write(cmd)

    def get_output_trigger_source(self, output_num: int = 1) -> OutpTrigSourceQueryResponse1:
        """
        Selects the source channel used by trigger output on a two-channel instrument. 

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source channel.
        """
        cmd = f":OUTPut{output_num}:TRIGger:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_output_trigger_source(self, channel: OutpTrigSourceCommandParameter1, output_num: int = 1):
        """
        Selects the source channel used by trigger output on a two-channel instrument. 

        Args:
            output_num (int): The channel number identifier. (Range: 1-2)
            channel (str): Selects the source channel used by trigger output on a two-channel instrument.
        """
        cmd = f":OUTPut{output_num}:TRIGger:SOURce {channel}"
        self._rsrc.write(cmd)



    def get_source_burst_gate_polarity(self, source_num: int = 1) -> SourBursGatePolarityQueryResponse1:
        """
        Selects true-high (NORMal) or true-low (INVerted) logic levels on the rear-panel Trig In connector for an externally gated burst.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the logic levels on the rear-panel Trig In connector for an externally gated burst.
        """
        cmd = f":SOURce{source_num}:BURSt:GATE:POLarity?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_burst_gate_polarity(self, polarity: SourBursGatePolarityCommandParameter1, source_num: int = 1):
        """
        Selects true-high (NORMal) or true-low (INVerted) logic levels on the rear-panel Trig In connector for an externally gated burst.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            polarity (str): The logic levels on the rear-panel Trig In connector for an externally gated burst.

        """
        cmd = f":SOURce{source_num}:BURSt:GATE:POLarity {polarity}"
        self._rsrc.write(cmd)

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

    def set_source_burst_internal_period(self, seconds: Union[float, Enum33500bEnumminmaxdef], source_num: int = 1):
        """
        Sets the burst period for internally-triggered bursts.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The burst period for internally-triggered bursts.
        """
        cmd = f":SOURce{source_num}:BURSt:INTernal:PERiod {seconds}"
        self._rsrc.write(cmd)

    def get_source_burst_mode(self, source_num: int = 1) -> SourBursModeQueryResponse1:
        """
        Selects the burst mode.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current burst mode.
        """
        cmd = f":SOURce{source_num}:BURSt:MODE?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_burst_mode(self, mode: SourBursModeCommandParameter1, source_num: int = 1):
        """
        Selects the burst mode.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The burst mode.
        """
        cmd = f":SOURce{source_num}:BURSt:MODE {mode}"
        self._rsrc.write(cmd)

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

    def set_source_burst_ncycles(self, num_cycles: Union[float, Enum33500bEnumminmaxdefinf], source_num: int = 1):
        """
        Sets the number of cycles to be output per burst (triggered burst mode only).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            num_cycles (float): The number of cycles to be output per burst.
        """
        cmd = f":SOURce{source_num}:BURSt:NCYCles {num_cycles}"
        self._rsrc.write(cmd)

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

    def set_source_burst_phase(self, angle: Union[float, Enum33500bEnumminmaxdef], source_num: int = 1):
        """
        Sets the starting phase angle for the burst.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            angle (float): The starting phase angle for the burst.
        """
        cmd = f":SOURce{source_num}:BURSt:PHASe {angle}"
        self._rsrc.write(cmd)

    def get_source_burst_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_burst_state(self, boolean: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables burst mode.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            boolean (bool): Enables or disables burst mode.
        """
        cmd = f":SOURce{source_num}:BURSt:STATe {boolean}"
        self._rsrc.write(cmd)

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

    def set_source_am_depth(self, depth_in_percent: Union[float, Enum33500bEnumminmaxdef], source_num: int = 1):
        """
        Sets internal modulation depth ("percent modulation") in percent.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            depth_in_percent (float): Internal modulation depth ("percent modulation") in percent.
        """
        cmd = f":SOURce{source_num}:AM:DEPTh {depth_in_percent}"
        self._rsrc.write(cmd)

    def get_source_am_dssc(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_am_dssc(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Selects Amplitude Modulation mode 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":SOURce{source_num}:AM:DSSC {state}"
        self._rsrc.write(cmd)

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

    def set_source_am_internal_frequency(self, frequency: Union[float, Enum33500bEnumminmaxdef], source_num: int = 1):
        """
        Sets frequency of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency of modulating waveform.
        """
        cmd = f":SOURce{source_num}:AM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)

    def get_source_am_internal_function(self, source_num: int = 1) -> SourAmIntFuncShapeCommandParameter1clone:
        """
        Selects shape of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current shape of modulating waveform.
        """
        cmd = f":SOURce{source_num}:AM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_am_internal_function(self, function: SourAmIntFuncShapeCommandParameter1clone, source_num: int = 1):
        """
        Selects shape of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): Shape of modulating waveform.
        """
        cmd = f":SOURce{source_num}:AM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)

    def get_source_am_source(self, source_num: int = 1) -> SourAmSourceQueryResponse1:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:AM:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_am_source(self, source: SourAmSourceCommandParameter1, source_num: int = 1):
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): INTernal|EXTernal|CH1|CH2.
        """
        cmd = f":SOURce{source_num}:AM:SOURce {source}"
        self._rsrc.write(cmd)

    def get_source_am_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_am_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0
        """
        cmd = f":SOURce{source_num}:AM:STATe {state}"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_source_apply_arbitrary(self, sample_rate: Union[float, Enum33500bStdNumEnumsclone], amplitude: Union[float, Enum33500bStdNumEnumsclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_apply_dc(self, frequency: Union[float, Enum33500bStdNumEnumscloneclone], amplitude: Union[float, Enum33500bStdNumEnumscloneclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_apply_noise(self, frequency: Union[float, Enum33500bStdNumEnumscloneclone], amplitude: Union[float, Enum33500bStdNumEnumsclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_apply_prbs(self, frequency: Union[float, Enum33500bStdNumEnumscloneclone], amplitude: Union[float, Enum33500bStdNumEnumsclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_apply_pulse(self, frequency: Union[float, Enum33500bStdNumEnumsclone], amplitude: Union[float, Enum33500bStdNumEnumsclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_apply_ramp(self, frequency: Union[float, Enum33500bStdNumEnumsclone], amplitude: Union[float, Enum33500bStdNumEnumsclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_apply_sinusoid(self, frequency: Union[float, Enum33500bStdNumEnumsclone], amplitude: Union[float, Enum33500bStdNumEnumsclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_apply_square(self, frequency: Union[float, Enum33500bStdNumEnumsclone], amplitude: Union[float, Enum33500bStdNumEnumsclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_apply_triangle(self, frequency: Union[float, Enum33500bStdNumEnumsclone], amplitude: Union[float, Enum33500bStdNumEnumsclone], offset: Union[float, Enum33500bStdNumEnumsclone], source_num: int = 1):
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

    def set_source_bpsk_internal_rate(self, modulating_frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the rate at which the output phase "shifts" between the carrier and offset phase.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            modulating_frequency (float): The rate at which the output phase "shifts" between the carrier and offset phase.
        """
        cmd = f":SOURce{source_num}:BPSK:INTernal:RATE {modulating_frequency}"
        self._rsrc.write(cmd)

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

    def set_source_bpsk_phase(self, angle: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the Binary Phase Shift Keying phase shift in degrees.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            angle (float): The Binary Phase Shift Keying.
        """
        cmd = f":SOURce{source_num}:BPSK:PHASe {angle}"
        self._rsrc.write(cmd)

    def get_source_bpsk_source(self, source_num: int = 1) -> SourAmSourceCommandParameter1clone:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:BPSK:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_bpsk_source(self, source: SourAmSourceCommandParameter1clone, source_num: int = 1):
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): INTernal|EXTernal.
        """
        cmd = f":SOURce{source_num}:BPSK:SOURce {source}"
        self._rsrc.write(cmd)

    def get_source_bpsk_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_bpsk_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): ON|1|OFF|0.
        """
        cmd = f":SOURce{source_num}:BPSK:STATe {state}"
        self._rsrc.write(cmd)

    def get_source_combine_feed(self, source_num: int = 1) -> SourCombFeedQueryResponse1:
        """
        Enables or disables the combining of both channels' outputs on a two-channel instrument into a single channel connector.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current  source channel.
        """
        cmd = f":SOURce{source_num}:COMBine:FEED?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_combine_feed(self, source: SourCombFeedCommandParameter1, source_num: int = 1):
        """
        Enables or disables the combining of both channels' outputs on a two-channel instrument into a single channel connector.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): CH1|CH2|NONE.
        """
        cmd = f":SOURce{source_num}:COMBine:FEED {source}"
        self._rsrc.write(cmd)

    @overload
    def set_source_data_arbitrary(self, source_num: int, syntax: SourceDataArbitrarySyntax.BLOCKREAL32, arb_name: str, binary_block: Union[bytes] | None) -> None: ...

    @overload
    def set_source_data_arbitrary(self, source_num: int, syntax: SourceDataArbitrarySyntax.ASCII, arb_name: str, value: float) -> None: ...

    def set_source_data_arbitrary(self, arb_name: str, data: Union[int, Any], syntax: SourceDataArbitrarySyntax, source_num: int = 1):
        """
        Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            syntax (SOURCEDATAARBITRARYSyntax): The syntax variant to use for this command

            For syntax BlockReal32:
                arb_name (str): The arbitrary sequence to be downloaded to.
                binary_block (Union[bytes] | None): List of values to be downloaded into waveform memory.

            For syntax Ascii:
                arb_name (str): The arbitrary sequence to be downloaded to.
                value (float): List of values to be downloaded into waveform memory. (Repeatable: *)
        """
        # Get parameters based on selected syntax
        match syntax:
            case SourceDataArbitrarySyntax.BLOCKREAL32:
                cmd = f":SOURce{source_num}:DATA:ARBitrary {arb_name}, {data}"
            case SourceDataArbitrarySyntax.ASCII:
                if not isinstance(data, int):
                    raise TypeError("For ASCII syntax, data must be an integer")
                cmd = f":SOURce{source_num}:DATA:ARBitrary {arb_name}, {data}"
        # Handle binary data
        if isinstance(data, (list, tuple, np.ndarray)):
            self._write_binary_data(cmd, data, syntax.name)
        else:
            self._rsrc.write(cmd)

    @overload
    def set_source_data_arbitrary_dac(self, source_num: int, syntax: SourceDataArbitraryDacSyntax.ASCII, arb_name: str, value: int) -> None: ...

    @overload
    def set_source_data_arbitrary_dac(self, source_num: int, syntax: SourceDataArbitraryDacSyntax.BLOCKINT16, arb_name: str, binary_block: Union[bytes] | None) -> None: ...

    def set_source_data_arbitrary_dac(self, arb_name: str, data: Union[int, Any], syntax: SourceDataArbitraryDacSyntax, source_num: int = 1):
        """
        Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            syntax (SOURCEDATAARBITRARYDACSyntax): The syntax variant to use for this command

            For syntax Ascii:
                arb_name (str): The arbitrary sequence name to be downloaded to.
                value (int): The DAC codes to be loaded into waveform memory as a list of integers. (Repeatable: *)

            For syntax BlockInt16:
                arb_name (str): The arbitrary sequence name to be downloaded to.
                binary_block (Union[bytes] | None): Binary block data.
        """
        # Get parameters based on selected syntax
        match syntax:
            case SourceDataArbitraryDacSyntax.ASCII:
                if not isinstance(data, int):
                    raise TypeError("For ASCII syntax, data must be an integer")
                cmd = f":SOURce{source_num}:DATA:ARBitrary:DAC {arb_name}, {data}"
            case SourceDataArbitraryDacSyntax.BLOCKINT16:
                cmd = f":SOURce{source_num}:DATA:ARBitrary:DAC {arb_name}, {data}"
        # Handle binary data
        if isinstance(data, (list, tuple, np.ndarray)):
            self._write_binary_data(cmd, data, syntax.name)
        else:
            self._rsrc.write(cmd)

    @overload
    def set_source_data_arbitrary2(self, source_num: int, syntax: SourceDataArbitrary2Syntax.BLOCKREAL32, arb_name: str, binary_block: Union[bytes] | None) -> None: ...

    @overload
    def set_source_data_arbitrary2(self, source_num: int, syntax: SourceDataArbitrary2Syntax.ASCII, arb_name: str, value: float) -> None: ...

    def set_source_data_arbitrary2(self, arb_name: str, data: Union[int, Any], syntax: SourceDataArbitrary2Syntax, source_num: int = 1):
        """
        Downloads integer values representing DAC codes (DATA:ARBitrary[2]:DAC) or floating point values (DATA:ARBitrary[2]) into waveform volatile memory as either a list of comma separated values or binary block of data.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            syntax (SOURCEDATAARBITRARY2Syntax): The syntax variant to use for this command

            For syntax BlockReal32:
                arb_name (str): The arbitrary sequence to be downloaded to.
                binary_block (Union[bytes] | None): List of values to be downloaded into waveform memory.

            For syntax Ascii:
                arb_name (str): The arbitrary sequence to be downloaded to.
                value (float): List of values to be downloaded into waveform memory. (Repeatable: *)
        """
        # Get parameters based on selected syntax
        match syntax:
            case SourceDataArbitrary2Syntax.BLOCKREAL32:
                cmd = f":SOURce{source_num}:DATA:ARBitrary2 {arb_name}, {data}"
            case SourceDataArbitrary2Syntax.ASCII:
                if not isinstance(data, int):
                    raise TypeError("For ASCII syntax, data must be an integer")
                cmd = f":SOURce{source_num}:DATA:ARBitrary2 {arb_name}, {data}"
        # Handle binary data
        if isinstance(data, (list, tuple, np.ndarray)):
            self._write_binary_data(cmd, data, syntax.name)
        else:
            self._rsrc.write(cmd)

    @overload
    def set_source_data_arbitrary2_dac(self, source_num: int, syntax: SourceDataArbitrary2DacSyntax.ASCII, arb_name: str, value: int) -> None: ...

    @overload
    def set_source_data_arbitrary2_dac(self, source_num: int, syntax: SourceDataArbitrary2DacSyntax.BLOCKINT16, arb_name: str, binary_block: Union[bytes] | None) -> None: ...

    def set_source_data_arbitrary2_dac(self, arb_name: str, data: Union[int, Any], syntax: SourceDataArbitrary2DacSyntax, source_num: int = 1):
        """
        Downloads integer values representing DAC codes (DATA:ARBitrary[1|2]:DAC) or floating point values (DATA:ARBitrary[1|2]) into waveform volatile memory as either a list of comma separated values or binary block of data.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            syntax (SOURCEDATAARBITRARY2DACSyntax): The syntax variant to use for this command

            For syntax Ascii:
                arb_name (str): The arbitrary sequence name to be downloaded to.
                value (int): The DAC codes to be loaded into waveform memory as a list of integers. (Repeatable: *)

            For syntax BlockInt16:
                arb_name (str): The arbitrary sequence name to be downloaded to.
                binary_block (Union[bytes] | None): Binary block data.
        """
        # Get parameters based on selected syntax
        match syntax:
            case SourceDataArbitrary2DacSyntax.ASCII:
                if not isinstance(data, int):
                    raise TypeError("For ASCII syntax, data must be an integer")
                cmd = f":SOURce{source_num}:DATA:ARBitrary2:DAC {arb_name}, {data}"
            case SourceDataArbitrary2DacSyntax.BLOCKINT16:
                cmd = f":SOURce{source_num}:DATA:ARBitrary2:DAC {arb_name}, {data}"
        # Handle binary data
        if isinstance(data, (list, tuple, np.ndarray)):
            self._write_binary_data(cmd, data, syntax.name)
        else:
            self._rsrc.write(cmd)

    def get_source_data_arbitrary2_format(self, source_num: int = 1) -> SourceDataArb2FormatQueryResponse1:
        """
        Specifies whether the format for data points in DATA:ARB2 and DATA:ARB2:DAC commands is interleaved (ABAB) or all of channel 1 followed by all of channel 2 (AABB).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns an interleaved data format for dual arbitrary waveform data
        """
        cmd = f":SOURce{source_num}:DATA:ARBitrary2:FORMat?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_data_arbitrary2_format(self, format: SourceDataArb2FormatCommandParameter1, source_num: int = 1):
        """
        Specifies whether the format for data points in DATA:ARB2 and DATA:ARB2:DAC commands is interleaved (ABAB) or all of channel 1 followed by all of channel 2 (AABB).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            format (str): An interleaved data format for dual arbitrary waveform data
        """
        cmd = f":SOURce{source_num}:DATA:ARBitrary2:FORMat {format}"
        self._rsrc.write(cmd)

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

    def set_source_data_sequence(self, block_descriptor: Union[bytes] | None, source_num: int = 1):
        """
        Defines a sequence of waveforms already loaded into waveform memory via MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            block_descriptor (Union[bytes] | None): Defines a sequence of waveforms
        """
        cmd = f":SOURce{source_num}:DATA:SEQuence {block_descriptor}"
        self._rsrc.write(cmd)

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
        return str(response)

    def source_data_volatile_clear(self, source_num: int = 1):
        """
        Clears waveform memory for the specified channel and reloads the default waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":SOURce{source_num}:DATA:VOLatile:CLEar"
        self._rsrc.write(cmd)

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

    def set_source_fm_deviation(self, peak_deviation_in_Hz: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the peak frequency deviation in Hz. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            peak_deviation_in_Hz (float):  the peak frequency deviation in Hz.
        """
        cmd = f":SOURce{source_num}:FM:DEViation {peak_deviation_in_Hz}"
        self._rsrc.write(cmd)

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

    def set_source_fm_internal_frequency(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the frequency of the modulating waveform. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:FM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)

    def get_source_fm_internal_function(self, source_num: int = 1) -> SourAmIntFuncShapeCommandParameter1clone:
        """
        This command selects the shape of the modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current shape of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:FM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_fm_internal_function(self, function: SourAmIntFuncShapeCommandParameter1clone, source_num: int = 1):
        """
        This command selects the shape of the modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The shape of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:FM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)

    def get_source_fm_source(self, source_num: int = 1) -> SourFmSourceQueryResponse1:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:FM:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_fm_source(self, source: SourFmSourceCommandParameter1, source_num: int = 1):
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:FM:SOURce {source}"
        self._rsrc.write(cmd)

    def get_source_fm_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_fm_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable modulation.
        """
        cmd = f":SOURce{source_num}:FM:STATe {state}"
        self._rsrc.write(cmd)

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

    def set_source_frequency(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the output frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The output frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_frequency_center(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the center frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The center frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency:CENTer {frequency}"
        self._rsrc.write(cmd)

    def get_source_frequency_couple_mode(self, source_num: int = 1) -> SourFreqCoupModeQueryResponse1:
        """
        Sets the type of frequency coupling between frequency coupled channels; OFFSet specifies a constant frequency offset between channels; RATio specifies a constant ratio between the channels' frequencies.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current frequency coupling mode
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:MODE?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_frequency_couple_mode(self, mode: SourFreqCoupModeCommandParameter1, source_num: int = 1):
        """
        Sets the type of frequency coupling between frequency coupled channels; OFFSet specifies a constant frequency offset between channels; RATio specifies a constant ratio between the channels' frequencies.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The frequency coupling mode
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:MODE {mode}"
        self._rsrc.write(cmd)

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

    def set_source_frequency_couple_offset(self, frequency: float, source_num: int = 1):
        """
        Sets the offset frequency when an instrument is in frequency coupled mode OFFSet.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The offset frequency.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:OFFSet {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_frequency_couple_ratio(self, ratio: float, source_num: int = 1):
        """
        Sets offset ratio between channel frequencies in frequency coupled mode RATio.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            ratio (float): The offset ratio.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:RATio {ratio}"
        self._rsrc.write(cmd)

    def get_source_frequency_couple_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_frequency_couple_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables/disables frequency coupling between channels in a two-channel instrument.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enables/disables frequency coupling state.
        """
        cmd = f":SOURce{source_num}:FREQuency:COUPle:STATe {state}"
        self._rsrc.write(cmd)

    def get_source_frequency_mode(self, source_num: int = 1) -> SourFreqModeQueryResponse1:
        """
        Sets the type of frequency mode as a continuous wave at a fixed frequency (CW or FIXed), a frequency sweep (SWEep), or a frequency list (LIST).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the type of frequency mode.
        """
        cmd = f":SOURce{source_num}:FREQuency:MODE?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_frequency_mode(self, mode: SourFreqModeCommandParameter1, source_num: int = 1):
        """
        Sets the type of frequency mode as a continuous wave at a fixed frequency (CW or FIXed), a frequency sweep (SWEep), or a frequency list (LIST).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The frequency mode .
        """
        cmd = f":SOURce{source_num}:FREQuency:MODE {mode}"
        self._rsrc.write(cmd)

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

    def set_source_frequency_span(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets frequency span (used in conjunction with the center frequency) for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency span.
        """
        cmd = f":SOURce{source_num}:FREQuency:SPAN {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_frequency_start(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the start frequencies for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The start frequencies for a frequency sweep.
        """
        cmd = f":SOURce{source_num}:FREQuency:STARt {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_frequency_stop(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the stop frequencies for a frequency sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The stop frequencies for a frequency sweep.
        """
        cmd = f":SOURce{source_num}:FREQuency:STOP {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_fskey_frequency(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the FSK alternate (or "hop") frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The FSK alternate (or "hop") frequency.
        """
        cmd = f":SOURce{source_num}:FSKey:FREQuency {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_fskey_internal_rate(self, rate_in_Hz: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the rate at which output frequency "shifts" between the carrier and hop frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            rate_in_Hz (float): The rate at which output frequency "shifts" between the carrier and hop frequency.
        """
        cmd = f":SOURce{source_num}:FSKey:INTernal:RATE {rate_in_Hz}"
        self._rsrc.write(cmd)

    def get_source_fskey_source(self, source_num: int = 1) -> SourAmSourceCommandParameter1clone:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:FSKey:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_fskey_source(self, source: SourAmSourceCommandParameter1clone, source_num: int = 1):
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:FSKey:SOURce {source}"
        self._rsrc.write(cmd)

    def get_source_fskey_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_fskey_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable modulation.
        """
        cmd = f":SOURce{source_num}:FSKey:STATe {state}"
        self._rsrc.write(cmd)

    def get_source_function(self, source_num: int = 1) -> SourFuncShapeCommandParameter1clone:
        """
        Selects output function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current output function.
        """
        cmd = f":SOURce{source_num}:FUNCtion?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_function(self, function: SourFuncShapeCommandParameter1clone, source_num: int = 1):
        """
        Selects output function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The output function.
        """
        cmd = f":SOURce{source_num}:FUNCtion {function}"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_source_function_arbitrary(self, filename: str, source_num: int = 1):
        """
        Selects an arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            filename (str): The arbitrary waveform (.arb/.barb) or sequence (.seq) that has previously been loaded into volatile memory for the channel specified with MMEMory:LOAD:DATA[1|2] or DATA:ARBitrary.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary {filename}"
        self._rsrc.write(cmd)

    def get_source_function_arbitrary_advance(self, source_num: int = 1) -> SourFuncShapArbAdvanceQueryResponse1:
        """
        Specifies the method for advancing to the next arbitrary waveform data point for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the method for advancing to the next arbitrary waveform data point for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:ADVance?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_function_arbitrary_advance(self, mode: SourFuncShapArbAdvanceCommandParameter1, source_num: int = 1):
        """
        Specifies the method for advancing to the next arbitrary waveform data point for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The method for advancing to the next arbitrary waveform data point for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:ADVance {mode}"
        self._rsrc.write(cmd)

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

    def set_source_function_arbitrary_balance_gain(self, percent: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the gain balance ratio for dual arbitrary waveforms.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            percent (float): The gain balance ratio for dual arbitrary waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:GAIN {percent}"
        self._rsrc.write(cmd)

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

    def set_source_function_arbitrary_balance_offset1(self, volts: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            volts (float): The offset (in volts) added to the dual arbitrary waveform offset for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:OFFSet1 {volts}"
        self._rsrc.write(cmd)

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

    def set_source_function_arbitrary_balance_offset2(self, volts: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Specifies the offset (in volts) added to the dual arbitrary waveform offset for the specified channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            volts (float): The offset (in volts) added to the dual arbitrary waveform offset for the specified channel.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:OFFSet2 {volts}"
        self._rsrc.write(cmd)

    def get_source_function_arbitrary_balance_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_function_arbitrary_balance_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables channel balancing for dual arbitrary waveforms 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the channel balancing for dual arbitrary waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:BALance:STATe {state}"
        self._rsrc.write(cmd)

    def get_source_function_arbitrary_filter(self, source_num: int = 1) -> SourFuncShapArbFilterQueryResponse1:
        """
        Specifies the filter setting for an arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the filter setting for an arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:FILTer?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_function_arbitrary_filter(self, filter: SourFuncShapArbFilterCommandParameter1, source_num: int = 1):
        """
        Specifies the filter setting for an arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            filter (str): The filter setting for an arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:FILTer {filter}"
        self._rsrc.write(cmd)

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

    def set_source_function_arbitrary_frequency(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the frequency for the arbitrary waveform.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency for the arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:FREQuency {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_function_arbitrary_period(self, period: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the period for the arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            period (float): The period for the arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:PERiod {period}"
        self._rsrc.write(cmd)

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

    def set_source_function_arbitrary_ptpeak(self, voltage: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets peak to peak voltage.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): Peak to peak voltage.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:PTPeak {voltage}"
        self._rsrc.write(cmd)

    def get_source_function_arbitrary_skew_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_function_arbitrary_skew_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables skew time compensation (FUNCtion:ARBitrary:SKEW:TIME). This is always OFF for modulated signals, sweeps, lists, and bursts.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the skew time compensation function.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SKEW:STATe {state}"
        self._rsrc.write(cmd)

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

    def set_source_function_arbitrary_skew_time(self, time: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets a small time difference between the channels to compensate for minor variations in timing at the connector output plane or at the device under test (DUT). 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            time (float): The skew time
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SKEW:TIME {time}"
        self._rsrc.write(cmd)

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

    def set_source_function_arbitrary_srate(self, sample_rate: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the sample rate for the arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sample_rate (float): The sample rate for the arbitary waveform.
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SRATe {sample_rate}"
        self._rsrc.write(cmd)

    def source_function_arbitrary_synchronize(self, source_num: int = 1):
        """
        Causes two independent arbitrary waveforms to synchronize to first point of each waveform (two-channel instruments only).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":SOURce{source_num}:FUNCtion:ARBitrary:SYNChronize"
        self._rsrc.write(cmd)

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

    def set_source_function_noise_bandwidth(self, bandwidth: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets bandwidth of noise function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            bandwidth (float): Bandwidth of noise function.
        """
        cmd = f":SOURce{source_num}:FUNCtion:NOISe:BANDwidth {bandwidth}"
        self._rsrc.write(cmd)

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

    def set_source_function_prbs_brate(self, bit_rate: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the pseudo-random binary sequence (PRBS) bit rate.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            bit_rate (float): The pseudo-random binary sequence (PRBS) bit rate.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:BRATe {bit_rate}"
        self._rsrc.write(cmd)

    def get_source_function_prbs_data(self, source_num: int = 1) -> SourFuncShapPrbsDataQueryResponse1:
        """
        Sets the pseudo-random binary sequence (PRBS) type. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: The pseudo-random binary sequence (PRBS) type.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:DATA?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_function_prbs_data(self, sequence_type: SourFuncShapPrbsDataCommandParameter1, source_num: int = 1):
        """
        Sets the pseudo-random binary sequence (PRBS) type. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sequence_type (str): The pseudo-random binary sequence (PRBS) type.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:DATA {sequence_type}"
        self._rsrc.write(cmd)

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

    def set_source_function_prbs_transition_both(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets PRBS transition edge time on both edges of a PRBS transition.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): PRBS transition edge time on both edges of a PRBS transition.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PRBS:TRANsition:BOTH {seconds}"
        self._rsrc.write(cmd)

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

    def set_source_function_pulse_dcycle(self, percent: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets pulse duty cycle.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            percent (float): Pulse duty cycle.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:DCYCle {percent}"
        self._rsrc.write(cmd)

    def get_source_function_pulse_hold(self, source_num: int = 1) -> SourFuncShapPulsHoldQueryResponse1:
        """
        Sets the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:HOLD?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_function_pulse_hold(self, pulse: SourFuncShapPulsHoldCommandParameter1, source_num: int = 1):
        """
        Sets the pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            pulse (str): The pulse waveform parameter (either pulse width or duty cycle) to be held constant as other parameters are varied.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:HOLD {pulse}"
        self._rsrc.write(cmd)

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

    def set_source_function_pulse_period(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the period for pulse waveforms.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The period for pulse waveforms.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:PERiod {seconds}"
        self._rsrc.write(cmd)

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

    def set_source_function_pulse_transition_both(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the pulse edge time on both edges of a pulse.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The pulse edge time on both edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:BOTH {seconds}"
        self._rsrc.write(cmd)

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

    def set_source_function_pulse_transition_leading(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the pulse edge time on the leading edges of a pulse.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The pulse edge time on the leading edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:LEADing {seconds}"
        self._rsrc.write(cmd)

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

    def set_source_function_pulse_transition_trailing(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the pulse edge time on the trailing edges of a pulse.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The pulse edge time on the trailing edges of a pulse.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:TRANsition:TRAiling {seconds}"
        self._rsrc.write(cmd)

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

    def set_source_function_pulse_width(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets pulse width.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The pulse width.
        """
        cmd = f":SOURce{source_num}:FUNCtion:PULSe:WIDTh {seconds}"
        self._rsrc.write(cmd)

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

    def set_source_function_ramp_symmetry(self, percent: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the symmetry percentage for ramp waves.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            percent (float): The symmetry percentage for ramp waves.
        """
        cmd = f":SOURce{source_num}:FUNCtion:RAMP:SYMMetry {percent}"
        self._rsrc.write(cmd)

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

    def set_source_function_square_dcycle(self, percent: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets duty cycle percentage for square wave.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            percent (float): The duty cycle percentage for square wave.
        """
        cmd = f":SOURce{source_num}:FUNCtion:SQUare:DCYCle {percent}"
        self._rsrc.write(cmd)

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

    def set_source_function_square_period(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets period for square wave.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): Period for square wave.
        """
        cmd = f":SOURce{source_num}:FUNCtion:SQUare:PERiod {seconds}"
        self._rsrc.write(cmd)

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

    def set_source_list_dwell(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets dwell time, the amount of time each frequency in a frequency list is generated.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The dwell time.
        """
        cmd = f":SOURce{source_num}:LIST:DWELl {seconds}"
        self._rsrc.write(cmd)

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

    def set_source_list_frequency(self, frequency: float, source_num: int = 1):
        """
        Specifies frequency values in a frequency list.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float):  frequency values in a frequency list. (Repeatable: *)
        """
        cmd = f":SOURce{source_num}:LIST:FREQuency {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_marker_cycle(self, cycle_num: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the marker cycle number at which the front-panel Sync signal goes low in a burst mode operation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            cycle_num (float): The marker cycle number.
        """
        cmd = f":SOURce{source_num}:MARKer:CYCLe {cycle_num}"
        self._rsrc.write(cmd)

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

    def set_source_marker_frequency(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the marker frequency at which the front-panel Sync signal goes low during a sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The marker frequency.
        """
        cmd = f":SOURce{source_num}:MARKer:FREQuency {frequency}"
        self._rsrc.write(cmd)

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

    def set_source_marker_point(self, sample_number: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sample_number (float): The sample number at which the front-panel Sync signal goes low within the active arbitrary waveform.
        """
        cmd = f":SOURce{source_num}:MARKer:POINt {sample_number}"
        self._rsrc.write(cmd)

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

    def set_source_modulation_phase(self, angle: Union[float, Enum33500bEnumminmaxdef], source_num: int = 1):
        """
        Sets the phase of the internal modulation source when modulating by the internal source with shape SIN, SQU, RAMP, NRAMp, or TRI. This command applies to the 336xx models only.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            angle (float): The phase of the internal modulation source when modulating by the internal source.
        """
        cmd = f":SOURce{source_num}:MODulation:PHASe {angle}"
        self._rsrc.write(cmd)

    def source_phase_reference(self, source_num: int = 1):
        """
        Simultaneously removes the offset set by PHASe and adjusts the primary phase generator by an amount equivalent to the PHASe setting.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":SOURce{source_num}:PHASe:REFerence"
        self._rsrc.write(cmd)

    def source_phase_synchronize(self, source_num: int = 1):
        """
        Simultaneously resets all phase generators in the instrument, including the modulation phase generators, to establish a common, internal phase zero reference point.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":SOURce{source_num}:PHASe:SYNChronize"
        self._rsrc.write(cmd)

    def get_source_phase_unlock_error_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_phase_unlock_error_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables the generation of an error if the phase-lock is ever lost by the instrument timebase.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the generation of phase-lock error.
        """
        cmd = f":SOURce{source_num}:PHASe:UNLock:ERRor:STATe {state}"
        self._rsrc.write(cmd)

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

    def set_source_pm_deviation(self, deviation_in_degrees: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the phase deviation in degrees. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            deviation_in_degrees (float): The phase deviation in degrees.
        """
        cmd = f":SOURce{source_num}:PM:DEViation {deviation_in_degrees}"
        self._rsrc.write(cmd)

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

    def set_source_pm_internal_frequency(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the frequency of the modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The frequency of the modulating waveform.
        """
        cmd = f":SOURce{source_num}:PM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)

    def get_source_pm_internal_function(self, source_num: int = 1) -> SourAmIntFuncShapeCommandParameter1clone:
        """
        Selects shape of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current shape of modulating waveform.
        """
        cmd = f":SOURce{source_num}:PM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_pm_internal_function(self, function: SourAmIntFuncShapeCommandParameter1clone, source_num: int = 1):
        """
        Selects shape of modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The shape of modulating waveform.
        """
        cmd = f":SOURce{source_num}:PM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)

    def get_source_pm_source(self, source_num: int = 1) -> SourPmSourceQueryResponse1:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:PM:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_pm_source(self, source: SourPmSourceCommandParameter1, source_num: int = 1):
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:PM:SOURce {source}"
        self._rsrc.write(cmd)

    def get_source_pm_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_pm_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable modulation function.
        """
        cmd = f":SOURce{source_num}:PM:STATe {state}"
        self._rsrc.write(cmd)

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

    def set_source_pwm_deviation(self, deviation: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets pulse width deviation; the ± variation in width (in seconds) from the pulse width of the carrier pulse waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            deviation (float): The pulse width deviation.
        """
        cmd = f":SOURce{source_num}:PWM:DEViation {deviation}"
        self._rsrc.write(cmd)

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

    def set_source_pwm_deviation_dcycle(self, deviation_in_pct: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets duty cycle deviation in percent of period.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            deviation_in_pct (float): The duty cycle deviation in percent.
        """
        cmd = f":SOURce{source_num}:PWM:DEViation:DCYCle {deviation_in_pct}"
        self._rsrc.write(cmd)

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

    def set_source_pwm_internal_frequency(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Selects frequency at which output pulse width shifts through its pulse width deviation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): The Frequency at which output pulse width shifts through its pulse width deviation. 
        """
        cmd = f":SOURce{source_num}:PWM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)

    def get_source_pwm_internal_function(self, source_num: int = 1) -> SourAmIntFuncShapeCommandParameter1clone:
        """
        Selects shape of the internal modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current shape of the internal modulating waveform.
        """
        cmd = f":SOURce{source_num}:PWM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_pwm_internal_function(self, function: SourSumIntFunctionCommandParameter1clone, source_num: int = 1):
        """
        Selects shape of the internal modulating waveform.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The shape of the internal modulating waveform.
        """
        cmd = f":SOURce{source_num}:PWM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)

    def get_source_pwm_source(self, source_num: int = 1) -> SourPwmSourceQueryResponse1:
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:PWM:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_pwm_source(self, source: SourPwmSourceCommandParameter1, source_num: int = 1):
        """
        Select the source of the modulating signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of the modulating signal.
        """
        cmd = f":SOURce{source_num}:PWM:SOURce {source}"
        self._rsrc.write(cmd)

    def get_source_pwm_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_pwm_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables modulation.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disables modulation function.
        """
        cmd = f":SOURce{source_num}:PWM:STATe {state}"
        self._rsrc.write(cmd)

    def get_source_rate_couple_mode(self, source_num: int = 1) -> SourRateCoupModeQueryResponse1:
        """
        Sets type of sample rate coupling to either a constant sample rate offset (OFFSet) or a constant ratio (RATio) between the channels' sample rates.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the sample rate coupling mode
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:MODE?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_rate_couple_mode(self, mode: SourRateCoupModeCommandParameter1, source_num: int = 1):
        """
        Sets type of sample rate coupling to either a constant sample rate offset (OFFSet) or a constant ratio (RATio) between the channels' sample rates.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            mode (str): The sample rate coupling mode
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:MODE {mode}"
        self._rsrc.write(cmd)

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

    def set_source_rate_couple_offset(self, sample_rate: float, source_num: int = 1):
        """
        Sets sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            sample_rate (float): The sample rate offset when a two-channel instrument is in sample rate coupled mode OFFSet.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:OFFSet {sample_rate}"
        self._rsrc.write(cmd)

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

    def set_source_rate_couple_ratio(self, ratio: float, source_num: int = 1):
        """
        Sets offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            ratio (float): The offset ratio between channel sample rates when a two-channel instrument is in sample rate coupled mode RATio.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:RATio {ratio}"
        self._rsrc.write(cmd)

    def get_source_rate_couple_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_rate_couple_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables sample rate coupling between channels, or allows one-time copying of one channel's sample rate into the other channel.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable sample rate coupled state.
        """
        cmd = f":SOURce{source_num}:RATE:COUPle:STATe {state}"
        self._rsrc.write(cmd)

    def get_source_roscillator_source(self, source_num: int = 1) -> SourRoscSourceQueryResponse1:
        """
        Selects the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.
        """
        cmd = f":SOURce{source_num}:ROSCillator:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_roscillator_source(self, source: SourRoscSourceCommandParameter1, source_num: int = 1):
        """
        Selects the source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source for the reference oscillator used as the frequency/phase reference for signals generated by the instrument.
        """
        cmd = f":SOURce{source_num}:ROSCillator:SOURce {source}"
        self._rsrc.write(cmd)

    def get_source_roscillator_source_auto(self, source_num: int = 1) -> SourRoscSourAutoQueryResponse1:
        """
        Disables or enables automatic selection of the reference oscillator.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the automatic selection of the reference oscillator.
        """
        cmd = f":SOURce{source_num}:ROSCillator:SOURce:AUTO?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_roscillator_source_auto(self, state: SourRoscSourAutoCommandParameter1, source_num: int = 1):
        """
        Disables or enables automatic selection of the reference oscillator.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (str): Enable/disable the automatic selection of the reference oscillator.
        """
        cmd = f":SOURce{source_num}:ROSCillator:SOURce:AUTO {state}"
        self._rsrc.write(cmd)

    def get_source_roscillator_source_current(self, source_num: int = 1) -> SourRoscSourCurrentQueryResponse1:
        """
        Indicates which reference oscillator signal is currently in use when ROSC:SOURce:AUTO is ON.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Determine reference signal source
        """
        cmd = f":SOURce{source_num}:ROSCillator:SOURce:CURRent?"
        response = self._rsrc.query(cmd)
        return str(response)

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

    def set_source_sum_amplitude(self, amplitude: float, source_num: int = 1):
        """
        Sets internal modulation depth (or "percent modulation") in percent.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            amplitude (float): The internal SUM signal amplitude.
        """
        cmd = f":SOURce{source_num}:SUM:AMPLitude {amplitude}"
        self._rsrc.write(cmd)

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

    def set_source_sum_internal_frequency(self, frequency: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the frequency of the summing waveform when internal sum source is selected (SUM:SOURce:INTernal). 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            frequency (float): Sets the frequency of the summing waveform when internal sum source is selected.
        """
        cmd = f":SOURce{source_num}:SUM:INTernal:FREQuency {frequency}"
        self._rsrc.write(cmd)

    def get_source_sum_internal_function(self, source_num: int = 1) -> SourSumIntFunctionCommandParameter1clone:
        """
        Selects the summing waveform (the waveform added to the primary waveform).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the summing waveform.
        """
        cmd = f":SOURce{source_num}:SUM:INTernal:FUNCtion?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_sum_internal_function(self, function: SourSumIntFunctionCommandParameter1clone, source_num: int = 1):
        """
        Selects the summing waveform (the waveform added to the primary waveform).

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            function (str): The summing waveform.
        """
        cmd = f":SOURce{source_num}:SUM:INTernal:FUNCtion {function}"
        self._rsrc.write(cmd)

    def get_source_sum_source(self, source_num: int = 1) -> SourAmSourceCommandParameter1:
        """
        Selects source of summing signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current source of summing signal.
        """
        cmd = f":SOURce{source_num}:SUM:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_sum_source(self, source: SourAmSourceCommandParameter1, source_num: int = 1):
        """
        Selects source of summing signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            source (str): The source of summing signal.
        """
        cmd = f":SOURce{source_num}:SUM:SOURce {source}"
        self._rsrc.write(cmd)

    def get_source_sum_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_sum_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Disables or enables SUM function.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the SUM function.
        """
        cmd = f":SOURce{source_num}:SUM:STATe {state}"
        self._rsrc.write(cmd)

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

    def set_source_sweep_htime(self, hold_time: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets number of seconds the sweep holds (pauses) at the stop frequency before returning to the start frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            hold_time (float): The sweep hold time
        """
        cmd = f":SOURce{source_num}:SWEep:HTIMe {hold_time}"
        self._rsrc.write(cmd)

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

    def set_source_sweep_rtime(self, return_time: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets number of seconds the sweep takes to return from stop frequency to start frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            return_time (float): The sweep return time.
        """
        cmd = f":SOURce{source_num}:SWEep:RTIMe {return_time}"
        self._rsrc.write(cmd)

    def get_source_sweep_spacing(self, source_num: int = 1) -> SourSweSpacingQueryResponse1:
        """
        Selects linear or logarithmic spacing for sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current sweep spacing.
        """
        cmd = f":SOURce{source_num}:SWEep:SPACing?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_sweep_spacing(self, spacing: SourSweSpacingCommandParameter1, source_num: int = 1):
        """
        Selects linear or logarithmic spacing for sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            spacing (str): The sweep spacing.
        """
        cmd = f":SOURce{source_num}:SWEep:SPACing {spacing}"
        self._rsrc.write(cmd)

    def get_source_sweep_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_sweep_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables the sweep.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the sweep function.
        """
        cmd = f":SOURce{source_num}:SWEep:STATe {state}"
        self._rsrc.write(cmd)

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

    def set_source_sweep_time(self, seconds: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets time (seconds) to sweep from start frequency to stop frequency.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            seconds (float): The sweep time.
        """
        cmd = f":SOURce{source_num}:SWEep:TIME {seconds}"
        self._rsrc.write(cmd)

    def get_source_track(self, source_num: int = 1) -> SourTrackQueryResponse1:
        """
        Causes channels 1 and 2 of a two-channel instrument to output the same signal, or an inverted polarity signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of the two-channel instrument to output the same signal, or an inverted polarity signal.
        """
        cmd = f":SOURce{source_num}:TRACk?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_track(self, track: SourTrackCommandParameter1, source_num: int = 1):
        """
        Causes channels 1 and 2 of a two-channel instrument to output the same signal, or an inverted polarity signal.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            track (str): Sets the two-channel instrument to output the same signal, or an inverted polarity signal.
        """
        cmd = f":SOURce{source_num}:TRACk {track}"
        self._rsrc.write(cmd)

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

    def set_source_voltage(self, amplitude: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets output amplitude.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            amplitude (float): Desired output amplitude in volts.
        """
        cmd = f":SOURce{source_num}:VOLTage {amplitude}"
        self._rsrc.write(cmd)

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

    def set_source_voltage_limit_high(self, voltage: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the high limits for output voltage.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): The high limits for output voltage.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:HIGH {voltage}"
        self._rsrc.write(cmd)

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

    def set_source_voltage_limit_low(self, voltage: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Sets the low limits for output voltage.



        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): The low limits for output voltage.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:LOW {voltage}"
        self._rsrc.write(cmd)

    def get_source_voltage_limit_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_voltage_limit_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables output amplitude voltage limits.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disables output amplitude voltage limits.
        """
        cmd = f":SOURce{source_num}:VOLTage:LIMit:STATe {state}"
        self._rsrc.write(cmd)

    def get_source_voltage_range_auto(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_voltage_range_auto(self, state: Union[int, SourVoltRangAutoCommandParameter1], source_num: int = 1):
        """
        Disables or enables voltage autoranging for all functions.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (int): Enable/disable the voltage autoranging.
        """
        cmd = f":SOURce{source_num}:VOLTage:RANGe:AUTO {state}"
        self._rsrc.write(cmd)

    def get_source_voltage_unit(self, source_num: int = 1) -> SourVoltLevUnitQueryResponse1:
        """
        Selects the units for output amplitude.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current value of output amplitude units
        """
        cmd = f":SOURce{source_num}:VOLTage:UNIT?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_source_voltage_unit(self, unit: SourVoltLevUnitCommandParameter1, source_num: int = 1):
        """
        Selects the units for output amplitude.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            unit (str): Output amplitude units
        """
        cmd = f":SOURce{source_num}:VOLTage:UNIT {unit}"
        self._rsrc.write(cmd)

    def get_source_voltage_couple_state(self, source_num: int = 1) -> Enum33500bBoolean:
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

    def set_source_voltage_couple_state(self, state: Enum33500bBoolean, source_num: int = 1):
        """
        Enables or disables the maintaining of the same amplitude, offset, range, load, and units on both channels of a two-channel instrument. 

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            state (bool): Enable/disable the maintaining of the same amplitude, offset, range, load, and ns on both channels of a two-channel instrument.
        """
        cmd = f":SOURce{source_num}:VOLTage:COUPle:STATe {state}"
        self._rsrc.write(cmd)

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

    def set_source_voltage_high(self, voltage: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Set the waveform's high voltage levels.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): The desired high voltage level.
        """
        cmd = f":SOURce{source_num}:VOLTage:HIGH {voltage}"
        self._rsrc.write(cmd)

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

    def set_source_voltage_low(self, voltage: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
        """
        Set the waveform's low voltage levels.

        Args:
            source_num (int): The channel number identifier. (Range: 1-2)
            voltage (float): The low voltage level for the specified channel.
        """
        cmd = f":SOURce{source_num}:VOLTage:LOW {voltage}"
        self._rsrc.write(cmd)

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

    def set_source_voltage_offset(self, offset: Union[float, Enum33500bStdNumEnums], source_num: int = 1):
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

    def set_status_operation_enable(self, enable_value: int):
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

    def status_preset(self):
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

    def set_status_questionable_enable(self, enable_value: int):
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



    def system_beeper_immediate(self, system_num: int = 1):
        """
        Issues a single beep.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:BEEPer:IMMediate"
        self._rsrc.write(cmd)

    def get_system_beeper_state(self, system_num: int = 1) -> Enum33500bBoolean:
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

    def set_system_beeper_state(self, state: Enum33500bBoolean, system_num: int = 1):
        """
        Disables or enables the beeper tone heard when an error is generated from the front panel or remote interface. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            state (bool): Enable/disable the beeper state.
        """
        cmd = f":SYSTem{system_num}:BEEPer:STATe {state}"
        self._rsrc.write(cmd)

    def get_system_communicate_enable(self, system_num: int = 1) -> Enum33500bBoolean:
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

    def set_system_communicate_enable(self, state: Enum33500bBoolean, interface: SystCommEnableCommandParameter2clone, system_num: int = 1):
        """
        Disables or enables the GPIB, USB, or LAN remote interface.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            state (bool): Enable/disable the interface state.
            interface (str): Interface
        """
        cmd = f":SYSTem{system_num}:COMMunicate:ENABle {state}, {interface}"
        self._rsrc.write(cmd)

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

    def set_system_communicate_gpib_address(self, address: int, system_num: int = 1):
        """
        Assigns instrument's GPIB (IEEE-488) address, which is displayed at power-on. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            address (int): The instrument's GPIB instrument address.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:GPIB:ADDRess {address}"
        self._rsrc.write(cmd)

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

    def get_system_communicate_lan_dhcp(self, system_num: int = 1) -> Enum33500bBoolean:
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

    def set_system_communicate_lan_dhcp(self, state: Enum33500bBoolean, system_num: int = 1):
        """
        Disables or enables instrument's use of DHCP.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            state (bool): Enable/disable the instrument's use of DHCP.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:DHCP {state}"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_system_communicate_lan_dns(self, address: str, system_num: int = 1, dns_num: int = 1):
        """
        Assigns static IP addresses of Domain Name System (DNS) servers.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            dns_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            address (str): The static IP addresses of Domain Name System (DNS) servers.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:DNS{dns_num} {address}"
        self._rsrc.write(cmd)

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
        return str(response)

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
        return str(response)

    def set_system_communicate_lan_gateway(self, address: str, system_num: int = 1):
        """
        Assigns a default gateway for the instrument.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            address (str): The default gateway which allows the instrument to communicate with systems that are not on the local subnet.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:GATeway {address}"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_system_communicate_lan_hostname(self, name: str, system_num: int = 1):
        """
        Assigns a hostname to the instrument.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            name (str): The hostname.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:HOSTname {name}"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_system_communicate_lan_ipaddress(self, address: str, system_num: int = 1):
        """
        Assigns a static Internet Protocol (IP) address for the instrument. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            address (str): A static Internet Protocol (IP) address.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:IPADdress {address}"
        self._rsrc.write(cmd)

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
        return str(response)

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
        return str(response)

    def set_system_communicate_lan_smask(self, mask: str, system_num: int = 1):
        """
        Assigns a subnet mask for the instrument. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            mask (str): The subnet mask.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:SMASk {mask}"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_system_communicate_lan_telnet_prompt(self, string: str, system_num: int = 1):
        """
        Sets the command prompt seen when communicating with the instrument via Telnet.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            string (str): The command prompt seen when communicating with the instrument via Telnet.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:TELNet:PROMpt {string}"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_system_communicate_lan_telnet_wmessage(self, string: str, system_num: int = 1):
        """
        Sets welcome message seen when communicating with instrument via Telnet.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            string (str): The welcome message.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:TELNet:WMESsage {string}"
        self._rsrc.write(cmd)

    def system_communicate_lan_update(self, system_num: int = 1):
        """
        Stores any changes made to the LAN settings into non-volatile memory and restarts the LAN driver with the updated settings.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:UPDate"
        self._rsrc.write(cmd)

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
        return str(response)

    def set_system_communicate_lan_wins(self, address: str, system_num: int = 1, wins_num: int = 1):
        """
        Assigns the static IP addresses of the Windows Internet Name System (WINS) servers.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            wins_num (int): Windows Internet Name System (WINS) server number. (Range: 1-2)
            address (str): The static IP addresses of the Windows Internet Name System (WINS) servers.
        """
        cmd = f":SYSTem{system_num}:COMMunicate:LAN:WINS{wins_num} {address}"
        self._rsrc.write(cmd)

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

    def set_system_date(self, year: int, month: int, day: int, system_num: int = 1):
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
        return str(response)

    def set_system_license_delete(self, option_name: SystCommEnableCommandParameter2clone2, system_num: int = 1):
        """
        Deletes a license.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            option_name (str): Deletes a license.
        """
        cmd = f":SYSTem{system_num}:LICense:DELete {option_name}"
        self._rsrc.write(cmd)

    def system_license_delete_all(self, system_num: int = 1):
        """
        Deletes all licenses.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:LICense:DELete:ALL"
        self._rsrc.write(cmd)

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
        return str(response)

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

    def get_system_license_install(self, system_num: int = 1) -> Enum33500bBoolean:
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

    def set_system_license_install(self, fileFolder: str, system_num: int = 1):
        """
        This command installs all licenses from a specified file or from all license files in the specified folder. 

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
            fileFolder (str): The file or folder to install licenses from.
        """
        cmd = f":SYSTem{system_num}:LICense:INSTall {fileFolder}"
        self._rsrc.write(cmd)

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
        return str(response)

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
        return str(response)

    def system_lock_release(self, system_num: int = 1):
        """
        Decrements the lock count by 1 and may release the I/O interface from which the command is executed.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:LOCK:RELease"
        self._rsrc.write(cmd)

    def get_system_lock_request(self, system_num: int = 1) -> Enum33500bBoolean:
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

    def system_security_immediate(self, system_num: int = 1):
        """
        Sanitizes all user-accessible instrument memory.

        Args:
            system_num (int): Domain Name System (DNS) server number. (Range: 1-2)
        """
        cmd = f":SYSTem{system_num}:SECurity:IMMediate"
        self._rsrc.write(cmd)

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

    def set_system_time(self, hour: int, minute: int, seconds: float, system_num: int = 1):
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
        return str(response)



    def trigger(self, trigger_num: int = 1):
        """
        Forces immediate trigger to initiate sequence, sweep, list, or burst.

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
        """
        cmd = f":TRIGger{trigger_num}"
        self._rsrc.write(cmd)

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

    def set_trigger_count(self, number: float, trigger_num: int = 1):
        """
        Sets trigger count.

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            number (float): The trigger count.
        """
        cmd = f":TRIGger{trigger_num}:COUNt {number}"
        self._rsrc.write(cmd)

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

    def set_trigger_delay(self, delay: Union[float, Enum33500bStdNumEnums], trigger_num: int = 1):
        """
        Sets trigger delay, (time from assertion of trigger to occurrence of triggered event).

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            delay (float): Trigger delay time.
        """
        cmd = f":TRIGger{trigger_num}:DELay {delay}"
        self._rsrc.write(cmd)

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

    def set_trigger_timer(self, timer: Union[float, Enum33500bStdNumEnums], trigger_num: int = 1):
        """
        Sets timer used when TRIGger[1|2]:SOURce is TIMer.

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            timer (float): The trigger timer.
        """
        cmd = f":TRIGger{trigger_num}:TIMer {timer}"
        self._rsrc.write(cmd)

    def get_trigger_slope(self, trigger_num: int = 1) -> TrigSeqSlopeQueryResponse1:
        """
        Specifies polarity of trigger signal on rear-panel Trig In connector for any externally-triggered mode. 

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current trigger slope.
        """
        cmd = f":TRIGger{trigger_num}:SLOPe?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_trigger_slope(self, edge: TrigSeqSlopeCommandParameter1, trigger_num: int = 1):
        """
        Specifies polarity of trigger signal on rear-panel Trig In connector for any externally-triggered mode. 

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            edge (str): POSitive|NEGative.
        """
        cmd = f":TRIGger{trigger_num}:SLOPe {edge}"
        self._rsrc.write(cmd)

    def get_trigger_source(self, trigger_num: int = 1) -> TrigSeqSourceQueryResponse1:
        """
        Selects the trigger source for sequence, list, burst or sweep. 

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)

        Returns:
            str: Returns the current trigger source.
        """
        cmd = f":TRIGger{trigger_num}:SOURce?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_trigger_source(self, source: TrigSeqSourceCommandParameter1, trigger_num: int = 1):
        """
        Selects the trigger source for sequence, list, burst or sweep. 

        Args:
            trigger_num (int): The channel number identifier. (Range: 1-2)
            source (str): IMMediate|EXTernal|TIMer|BUS.
        """
        cmd = f":TRIGger{trigger_num}:SOURce {source}"
        self._rsrc.write(cmd)



    def get_unit_angle(self) -> UnitAngleCommandParameter1clone:
        """
        Specifies the angle units that displayed on the screen and used for specifying angles.


        Returns:
            str: Returns the current angle units.
        """
        cmd = f":UNIT:ANGLe?"
        response = self._rsrc.query(cmd)
        return str(response)

    def set_unit_angle(self, unit: UnitAngleCommandParameter1clone):
        """
        Specifies the angle units that displayed on the screen and used for specifying angles.

        Args:
            unit (str): DEGree|RADian|SECond|DEFault.
        """
        cmd = f":UNIT:ANGLe {unit}"
        self._rsrc.write(cmd)


