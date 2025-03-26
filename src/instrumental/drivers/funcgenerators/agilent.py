# -*- coding: utf-8 -*-
# Copyright 2018-2019 Nate Bogdanowicz
"""
Driver module for Agilent signal generators.

MXG driver was initially developed for and tested on the N5181A.
"""
from enum import Enum
from . import FunctionGenerator
from .. import VisaMixin, SCPI_Facet
from ... import u, Q_


def _convert_enum(enum_type):
    """Check if arg is an instance or key of enum_type, and return that enum

    Strings are converted to lowercase first, so enum fields must be lowercase.
    """

    def convert(arg):
        if isinstance(arg, enum_type):
            return arg
        try:
            return enum_type[arg.lower()]
        except (KeyError, AttributeError):
            raise ValueError(
                "{} is not a valid {} enum".format(arg, enum_type.__name__)
            )

    return convert


class TriggerSource(Enum):
    bus = "BUS"
    immediate = "IMMMEDIATE"
    external = "EXT"
    key = "KEY"
    timer = "TIMER"
    manual = "MAN"


class TriggerSensing(Enum):
    edge = "EDGE"
    level = "LEV"


class TriggerSlope(Enum):
    positive = "POS"
    negative = "NEG"
    either = "EITH"


class FreqMode(Enum):
    cw = fixed = "FIXED"
    list = "LIST"


class AgilentMXG(FunctionGenerator, VisaMixin):
    _INST_PARAMS_ = ["visa_address"]
    _INST_VISA_INFO_ = ("Agilent Technologies", ["N5181A"])

    def _initialize(self):
        self._rsrc.read_termination = "\n"

    cw_frequency = SCPI_Facet("FREQ:CW", convert=float, units="Hz")
    sweep_center_frequency = SCPI_Facet("FREQ:CENTER", convert=float, units="Hz")
    sweep_span_frequency = SCPI_Facet("FREQ:SPAN", convert=float, units="Hz")
    sweep_start_frequency = SCPI_Facet("FREQ:START", convert=float, units="Hz")
    sweep_stop_frequency = SCPI_Facet("FREQ:STOP", convert=float, units="Hz")

    freq_mode = SCPI_Facet("FREQ:MODE", convert=_convert_enum(FreqMode))

    # enabling freq and/or amplitude sweep
    # sweep triggering
    # load a list sweep file


class OnOffState(Enum):
    ON = True
    OFF = False


class CombinedState(Enum):
    PLUS = True
    OFF = False


class Agilent33250A(FunctionGenerator, VisaMixin):
    _INST_PARAMS_ = ["visa_address"]
    _INST_VISA_INFO_ = ("Agilent Technologies", ["33250A"])

    def _initialize(self):
        self._rsrc.read_termination = "\n"

    frequency = SCPI_Facet("FREQ", convert=float, units="Hz")
    voltage = SCPI_Facet("VOLT", convert=float, units="V")


class AgilentE4400B(FunctionGenerator, VisaMixin):
    _INST_PARAMS_ = ["visa_address"]
    _INST_VISA_INFO_ = ("Hewlett-Packard", ["ESG-1000B"])
    width1 = SCPI_Facet("PULS:WIDTh1 ", convert=float, units="ns")
    width2 = SCPI_Facet("SOURce2:FUNCtion:PULSe:WIDTh", convert=float, units="s")

    def _initialize(self):
        self._rsrc.read_termination = "\n"

    frequency = SCPI_Facet("FREQ:FIXED", convert=float, units="Hz")


class AgilentFuncGenerator(FunctionGenerator, VisaMixin):
    def set_polarity(self, polarity, channel=1):
        """Set the polarity of a channel.

        Parameters
        ----------
        pol : either "NORM" for normal or "INV" for inverse

        channel: int
            The channel number
        """
        self.write("OUTP{:d}:POL {}", channel, polarity)

    def get_polarity(self, channel=1):
        return self.query("OUTP{:d}:POL?", channel)

    def set_trigger_source(self, source):
        """Set the trigger source.

        Parameters
        ----------
        source : either "MAN" for manual or "EXT" for external
        """
        self.write("ARM:SOUR " + source)

    def get_trigger_source(self):
        return TriggerSource(self.query("ARM:SOUR?")).name

    def set_trigger_sensing(self, sensing):
        """Set the trigger sensing.

        Parameters
        ----------
        sensing : either "EDGE" for edge or "LEV" for level
        """
        self.write("ARM:SENS " + sensing)

    def get_trigger_sensing(self):
        return TriggerSensing(self.query("ARM:SENS?")).name

    def set_trigger_slope(self, slope):
        """Set the trigger slope.

        Parameters
        ----------
        slope : either "POS" for positive or "NEG" for negative or "EITH" for either.
        """
        self.write("ARM:SLOP " + slope)

    def get_trigger_slope(self):
        return TriggerSlope(self.query("ARM:SLOP?")).name

    def get_errors(self):
        return self.query("SYST:ERR?")

    def set_delay(self, delay, channel=1):
        """Set the delay of a channel.

        Parameters
        ----------
        delay: pint.Quantity
            The new delay in nanosecond-compatible units

        channel: int
            The channel number
        """
        val = Q_(delay)
        mag = val.to("ns").magnitude
        self.write("PULS:DEL{:d} {}NS", channel, mag)

    def set_out_impedance(self, imp, channel=1):
        """Set the output impedance of a channel.

        Parameters
        ----------
        imp : pint.Quantity
            The impedance value in Ohm

        channel: int
            The channel number
        """
        val = Q_(imp)
        mag = val.to("ohm").magnitude
        self.write("OUTP{:d}:IMP:EXT {:f}OHM", channel, mag)

    def set_width(self, width, channel=1):
        """Set the width.

        Parameters
        ----------
        width : pint.Quantity
            The new width in nanosecond-compatible units

        channel: int
            Channel number
        """
        val = Q_(width)
        mag = val.to("ns").magnitude
        self.write("PULS:WIDTh{:d} {:f}NS", channel, mag)

    def set_high(self, high, channel=1):
        """Set the high voltage level.

        This changes the high level while keeping the low level fixed.

        Parameters
        ----------
        high : pint.Quantity
            The new high level in volt-compatible units

        channel: int
            Channel number
        """
        high = Q_(high)
        mag = high.to("V").magnitude
        self.write("VOLT{:d}:HIGH {:5.2f}V", channel, mag)

    def set_low(self, low, channel=1):
        """Set the low voltage level.

        This changes the low level while keeping the high level fixed.

        Parameters
        ----------
        low : pint.Quantity
            The new low level in volt-compatible units

        channel: int
            Channel number
        """
        low = Q_(low)
        mag = low.to("V").magnitude
        self.write("VOLT{:d}:LOW {:5.2f}V", channel, mag)

    @property
    def output1(self):
        val = self.query(":OUTP1?")
        return bool(int(val))

    @output1.setter
    def output1(self, val):
        val = int(bool(val))
        self.write("OUTP1 %s" % OnOffState(val).name)

    @property
    def output2(self):
        val = self.query("OUTP2?")
        return bool(int(val))

    @output2.setter
    def output2(self, val):
        val = int(bool(val))
        self.write("OUTP2 %s" % OnOffState(val).name)

    @property
    def combined(self):
        val = self.query("CHAN:MATH?")
        if val == "PLUS":
            return True
        else:
            return False

    @combined.setter
    def combined(self, val):
        val = int(bool(val))
        self.write("CHAN:MATH " + CombinedState(val).name)

    @property
    def trigger_level(self):
        val = self.query("ARM:LEV?")
        return Q_(val, u.V)

    @trigger_level.setter
    def trigger_level(self, val):
        low = Q_(val)
        mag = low.to("V").magnitude
        self.write("ARM:LEV {:5.2f}V", mag)

    def get_all_errors(self):
        """Get all errors from the error queue.

        Returns
        -------
        list
            List of (error_code, error_message) tuples
        """
        errors = []
        while True:
            error = self.query("SYST:ERR?")
            code, message = error.split(",")
            code = int(code)
            message = message.strip('"')
            if code == 0:  # No error
                break
            errors.append((code, message))
        return errors

    def clear_error_queue(self):
        """Clear the error queue by reading all errors."""
        while True:
            error = self.query("SYST:ERR?")
            code = int(error.split(",")[0])
            if code == 0:  # No error
                break


class Agilent81110A(AgilentFuncGenerator):
    _INST_PARAMS_ = ["visa_address"]
    _INST_VISA_INFO_ = ("HEWLETT-PACKARD", ["HP81110A"])

    def _initialize(self):
        self._rsrc.read_termination = "\n"

    def set_subsystem(self, subsystem, channel=1):
        """Switch between substems commands.

        Parameters
        ----------
        subsystem : either "VOLT" for voltage or "CURR" for current.

        channel: int
            Channel number
        """
        self.write("HOLD{:d} {}", channel, subsystem)


class Keysight81160A(AgilentFuncGenerator):
    _INST_PARAMS_ = ["visa_address"]
    _INST_VISA_INFO_ = ("Agilent Technologies", ["81160A"])

    def _initialize(self):
        self._rsrc.read_termination = "\n"


class WaveformShape(Enum):
    """Available waveform shapes."""
    SIN = "SIN"
    SQU = "SQU"
    TRI = "TRI"
    RAMP = "RAMP"
    PULS = "PULS"
    NOIS = "NOIS"
    DC = "DC"
    ARB = "ARB"


class BurstMode(Enum):
    """Available burst modes."""
    GAT = "GAT"
    N_CYC = "N_CYC"
    INF = "INF"


class SweepSpacing(Enum):
    """Available sweep spacing modes."""
    LIN = "LIN"
    LOG = "LOG"


class ModulationType(Enum):
    """Available modulation types."""
    AM = "AM"
    FM = "FM"
    PM = "PM"
    FSK = "FSK"
    PWM = "PWM"


class Keysight33500B(AgilentFuncGenerator):
    """Driver for Keysight 33500B Series Waveform Generators.

    This driver supports the 33500B Series of waveform generators, including:
    - 33511B (1 channel, 20 MHz)
    - 33512B (1 channel, 20 MHz, with arbitrary waveform)
    - 33521B (2 channels, 20 MHz)
    - 33522B (2 channels, 20 MHz, with arbitrary waveform)

    Model-Specific Features:
    -----------------------
    33511B:
        - Single channel output
        - Standard waveforms (sine, square, triangle, ramp, pulse, noise, DC)
        - Basic modulation (AM, FM, PM, FSK, PWM)
        - Burst mode
        - Sweep mode
        - Triggering capabilities

    33512B:
        - All features of 33511B
        - Arbitrary waveform capability
        - Waveform memory management
        - Waveform editing and downloading

    33521B:
        - All features of 33511B
        - Dual channel output
        - Channel synchronization
        - Channel phase control
        - Channel math operations (add, subtract, multiply)

    33522B:
        - All features of 33521B
        - Arbitrary waveform capability on both channels
        - Waveform memory management
        - Waveform editing and downloading
        - Dual arbitrary waveform playback

    Common Features:
    --------------
    - Frequency range: 1 µHz to 20 MHz
    - Amplitude range: 1 mVpp to 10 Vpp into 50 Ω
    - DC offset range: ±5 V into 50 Ω
    - Output impedance: 50 Ω
    - Modulation capabilities
    - Sweep capabilities
    - Trigger capabilities
    - Remote control via SCPI
    """

    _INST_PARAMS_ = ["visa_address"]
    _INST_VISA_INFO_ = (
        "Agilent Technologies",
        ["33511B", "33512B", "33521B", "33522B"],
    )

    def _initialize(self):
        """Initialize the instrument."""
        super()._initialize()
        self._rsrc.read_termination = "\n"
        self._rsrc.write_termination = "\n"
        self._rsrc.timeout = 10000  # Set timeout to 10 seconds

        # Clear any pending errors
        self.clear_error_queue()

        # Get model information
        idn = self.query("*IDN?").strip().split(",")
        self.model = idn[1]  # Store model number for feature checking

        # Set default channel to 1
        self.write("SOURce1")

    def _check_arbitrary_capability(self):
        """Check if the model supports arbitrary waveforms.

        Returns
        -------
        bool
            True if the model supports arbitrary waveforms (33512B or 33522B)
        """
        return self.model in ["33512B", "33522B"]

    def _check_dual_channel(self):
        """Check if the model supports dual channel operation.

        Returns
        -------
        bool
            True if the model supports dual channel (33521B or 33522B)
        """
        return self.model in ["33521B", "33522B"]

    # Basic waveform parameters for channel 1
    frequency1 = SCPI_Facet('SOURce1:FREQ', convert=float, units='Hz')
    voltage1 = SCPI_Facet('SOURce1:VOLT', convert=float, units='V')
    voltage_offset1 = SCPI_Facet('SOURce1:VOLT:OFFS', convert=float, units='V')
    function1 = SCPI_Facet('SOURce1:FUNC', convert=str)
    function_shape1 = SCPI_Facet('SOURce1:FUNC:SHAP', convert=str)
    duty_cycle1 = SCPI_Facet('SOURce1:FUNC:PULS:DCYC', convert=float, units='%')
    ramp_symmetry1 = SCPI_Facet('SOURce1:FUNC:RAMP:SYMM', convert=float, units='%')
    phase1 = SCPI_Facet('SOURce1:PHAS', convert=float, units='deg')
    
    # Basic waveform parameters for channel 2
    frequency2 = SCPI_Facet('SOURce2:FREQ', convert=float, units='Hz')
    voltage2 = SCPI_Facet('SOURce2:VOLT', convert=float, units='V')
    voltage_offset2 = SCPI_Facet('SOURce2:VOLT:OFFS', convert=float, units='V')
    function2 = SCPI_Facet('SOURce2:FUNC', convert=str)
    function_shape2 = SCPI_Facet('SOURce2:FUNC:SHAP', convert=str)
    duty_cycle2 = SCPI_Facet('SOURce2:FUNC:PULS:DCYC', convert=float, units='%')
    ramp_symmetry2 = SCPI_Facet('SOURce2:FUNC:RAMP:SYMM', convert=float, units='%')
    phase2 = SCPI_Facet('SOURce2:PHAS', convert=float, units='deg')
    
    # Burst mode settings for channel 1
    burst_mode1 = SCPI_Facet('SOURce1:BURS:MODE', convert=str)
    burst_ncycles1 = SCPI_Facet('SOURce1:BURS:NCYC', convert=int)
    burst_phase1 = SCPI_Facet('SOURce1:BURS:PHAS', convert=float, units='deg')
    burst_delay1 = SCPI_Facet('SOURce1:BURS:TDEL', convert=float, units='s')
    burst_gate_polarity1 = SCPI_Facet('SOURce1:BURS:GATE:POL', convert=str)
    
    # Burst mode settings for channel 2
    burst_mode2 = SCPI_Facet('SOURce2:BURS:MODE', convert=str)
    burst_ncycles2 = SCPI_Facet('SOURce2:BURS:NCYC', convert=int)
    burst_phase2 = SCPI_Facet('SOURce2:BURS:PHAS', convert=float, units='deg')
    burst_delay2 = SCPI_Facet('SOURce2:BURS:TDEL', convert=float, units='s')
    burst_gate_polarity2 = SCPI_Facet('SOURce2:BURS:GATE:POL', convert=str)
    
    # Modulation settings for channel 1
    modulation_state1 = SCPI_Facet('SOURce1:MOD:STAT', convert=bool)
    modulation_type1 = SCPI_Facet('SOURce1:MOD:TYP', convert=str)
    modulation_depth1 = SCPI_Facet('SOURce1:MOD:DEPT', convert=float)
    modulation_rate1 = SCPI_Facet('SOURce1:MOD:RATE', convert=float, units='Hz')
    modulation_source1 = SCPI_Facet('SOURce1:MOD:SOUR', convert=str)
    modulation_freq_dev1 = SCPI_Facet('SOURce1:MOD:FM:DEV', convert=float, units='Hz')
    modulation_phase_dev1 = SCPI_Facet('SOURce1:MOD:PM:DEV', convert=float, units='deg')
    modulation_pulse_width1 = SCPI_Facet('SOURce1:MOD:PWM:WIDT', convert=float, units='%')
    
    # Modulation settings for channel 2
    modulation_state2 = SCPI_Facet('SOURce2:MOD:STAT', convert=bool)
    modulation_type2 = SCPI_Facet('SOURce2:MOD:TYP', convert=str)
    modulation_depth2 = SCPI_Facet('SOURce2:MOD:DEPT', convert=float)
    modulation_rate2 = SCPI_Facet('SOURce2:MOD:RATE', convert=float, units='Hz')
    modulation_source2 = SCPI_Facet('SOURce2:MOD:SOUR', convert=str)
    modulation_freq_dev2 = SCPI_Facet('SOURce2:MOD:FM:DEV', convert=float, units='Hz')
    modulation_phase_dev2 = SCPI_Facet('SOURce2:MOD:PM:DEV', convert=float, units='deg')
    modulation_pulse_width2 = SCPI_Facet('SOURce2:MOD:PWM:WIDT', convert=float, units='%')
    
    # Sweep settings for channel 1
    sweep_state1 = SCPI_Facet('SOURce1:SWE:STAT', convert=bool)
    sweep_time1 = SCPI_Facet('SOURce1:SWE:TIME', convert=float, units='s')
    sweep_spacing1 = SCPI_Facet('SOURce1:SWE:SPAC', convert=str)
    sweep_mode1 = SCPI_Facet('SOURce1:SWE:MODE', convert=str)
    sweep_return1 = SCPI_Facet('SOURce1:SWE:RTIM', convert=float, units='s')
    
    # Sweep settings for channel 2
    sweep_state2 = SCPI_Facet('SOURce2:SWE:STAT', convert=bool)
    sweep_time2 = SCPI_Facet('SOURce2:SWE:TIME', convert=float, units='s')
    sweep_spacing2 = SCPI_Facet('SOURce2:SWE:SPAC', convert=str)
    sweep_mode2 = SCPI_Facet('SOURce2:SWE:MODE', convert=str)
    sweep_return2 = SCPI_Facet('SOURce2:SWE:RTIM', convert=float, units='s')
    
    # Trigger settings
    trigger_source = SCPI_Facet('TRIG:SOUR', convert=str)
    trigger_slope = SCPI_Facet('TRIG:SLOP', convert=str)
    trigger_delay = SCPI_Facet('TRIG:DEL', convert=float, units='s')
    trigger_count = SCPI_Facet('TRIG:COUN', convert=int)
    
    # Output settings
    output1 = SCPI_Facet('OUTP1', convert=bool)
    output2 = SCPI_Facet('OUTP2', convert=bool)
    output_impedance1 = SCPI_Facet('OUTP1:IMP', convert=float, units='ohm')
    output_impedance2 = SCPI_Facet('OUTP2:IMP', convert=float, units='ohm')
    output_polarity1 = SCPI_Facet('OUTP1:POL', convert=str)
    output_polarity2 = SCPI_Facet('OUTP2:POL', convert=str)
    
    # System settings
    system_error = SCPI_Facet('SYST:ERR', convert=str)
    system_version = SCPI_Facet('SYST:VERS', convert=str)
    system_date = SCPI_Facet('SYST:DATE', convert=str)
    system_time = SCPI_Facet('SYST:TIME', convert=str)

    def set_sweep_frequency(self, start_freq, stop_freq, channel=1):
        """Set sweep frequency range.

        Parameters
        ----------
        start_freq : float
            Start frequency in Hz
        stop_freq : float
            Stop frequency in Hz
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        # Validate frequency range (1 µHz to 20 MHz)
        if not (1e-6 <= start_freq <= 20e6) or not (1e-6 <= stop_freq <= 20e6):
            raise ValueError("Frequency must be between 1 µHz and 20 MHz")

        self.write(f"SOURce{channel}:FREQ:STAR {start_freq}")
        self.write(f"SOURce{channel}:FREQ:STOP {stop_freq}")

    def set_arbitrary_waveform(self, waveform_data, sample_rate=None, channel=1):
        """Load arbitrary waveform data.

        This feature is only available on 33512B and 33522B models.

        Parameters
        ----------
        waveform_data : array-like
            Array of waveform points (normalized to ±1)
        sample_rate : float, optional
            Sample rate in Hz. If None, uses current sample rate.
        channel : int, optional
            Channel number (1 or 2). For 33522B, can be either channel.

        Raises
        ------
        ValueError
            If the model doesn't support arbitrary waveforms
        """
        if not self._check_arbitrary_capability():
            raise ValueError(
                "Arbitrary waveform capability not available on this model"
            )

        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        # Convert data to string format
        data_str = ",".join(f"{x:.6f}" for x in waveform_data)

        # Set sample rate if specified
        if sample_rate is not None:
            self.write(f"SOURce{channel}:FUNC:ARB:SRAT {sample_rate}")

        # Load waveform data
        self.write(f"SOURce{channel}:DATA:ARB:DAC16 {data_str}")

    def get_arbitrary_waveform(self, channel=1):
        """Retrieve current arbitrary waveform data.

        This feature is only available on 33512B and 33522B models.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2). For 33522B, can be either channel.

        Returns
        -------
        array-like
            Array of waveform points (normalized to ±1)

        Raises
        ------
        ValueError
            If the model doesn't support arbitrary waveforms
        """
        if not self._check_arbitrary_capability():
            raise ValueError(
                "Arbitrary waveform capability not available on this model"
            )

        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        data_str = self.query(f"SOURce{channel}:DATA:ARB:DAC16?")
        return [float(x) for x in data_str.split(",")]

    def save_arbitrary_waveform(self, name, waveform_data, sample_rate=None, channel=1):
        """Save arbitrary waveform to internal memory.

        This feature is only available on 33512B and 33522B models.

        Parameters
        ----------
        name : str
            Name to save waveform as
        waveform_data : array-like
            Array of waveform points (normalized to ±1)
        sample_rate : float, optional
            Sample rate in Hz. If None, uses current sample rate.
        channel : int, optional
            Channel number (1 or 2). For 33522B, can be either channel.

        Raises
        ------
        ValueError
            If the model doesn't support arbitrary waveforms
        """
        if not self._check_arbitrary_capability():
            raise ValueError(
                "Arbitrary waveform capability not available on this model"
            )

        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        # Convert data to string format
        data_str = ",".join(f"{x:.6f}" for x in waveform_data)

        # Set sample rate if specified
        if sample_rate is not None:
            self.write(f"SOURce{channel}:FUNC:ARB:SRAT {sample_rate}")

        # Save waveform data
        self.write(f"SOURce{channel}:DATA:ARB:DAC16 {name},{data_str}")

    def load_arbitrary_waveform(self, name, channel=1):
        """Load arbitrary waveform from internal memory.

        This feature is only available on 33512B and 33522B models.

        Parameters
        ----------
        name : str
            Name of waveform to load
        channel : int, optional
            Channel number (1 or 2). For 33522B, can be either channel.

        Raises
        ------
        ValueError
            If the model doesn't support arbitrary waveforms
        """
        if not self._check_arbitrary_capability():
            raise ValueError(
                "Arbitrary waveform capability not available on this model"
            )

        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        self.write(f"SOURce{channel}:FUNC:ARB {name}")

    def get_available_waveforms(self, channel=1):
        """Get list of available arbitrary waveforms.

        This feature is only available on 33512B and 33522B models.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2). For 33522B, can be either channel.

        Returns
        -------
        list
            List of waveform names

        Raises
        ------
        ValueError
            If the model doesn't support arbitrary waveforms
        """
        if not self._check_arbitrary_capability():
            raise ValueError(
                "Arbitrary waveform capability not available on this model"
            )

        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        return self.query(f"SOURce{channel}:DATA:ARB:CAT?").strip('"').split(",")

    def delete_arbitrary_waveform(self, name, channel=1):
        """Delete arbitrary waveform from internal memory.

        This feature is only available on 33512B and 33522B models.

        Parameters
        ----------
        name : str
            Name of waveform to delete
        channel : int, optional
            Channel number (1 or 2). For 33522B, can be either channel.

        Raises
        ------
        ValueError
            If the model doesn't support arbitrary waveforms
        """
        if not self._check_arbitrary_capability():
            raise ValueError(
                "Arbitrary waveform capability not available on this model"
            )

        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        self.write(f"SOURce{channel}:DATA:ARB:DEL {name}")

    def set_phase(self, phase, channel=1):
        """Set the phase of the waveform.

        Parameters
        ----------
        phase : float
            Phase in degrees
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        self.write(f"SOURce{channel}:PHAS {phase}")

    def get_phase(self, channel=1):
        """Get the phase of the waveform.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Returns
        -------
        float
            Phase in degrees

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        return float(self.query(f"SOURce{channel}:PHAS?"))

    def set_duty_cycle(self, duty_cycle, channel=1):
        """Set the duty cycle of the waveform.

        Parameters
        ----------
        duty_cycle : float
            Duty cycle in percent (0-100)
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        self.write(f"SOURce{channel}:FUNC:PULS:DCYC {duty_cycle}")

    def get_duty_cycle(self, channel=1):
        """Get the duty cycle of the waveform.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Returns
        -------
        float
            Duty cycle in percent (0-100)

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        return float(self.query(f"SOURce{channel}:FUNC:PULS:DCYC?"))

    def set_ramp_symmetry(self, symmetry, channel=1):
        """Set the ramp symmetry.

        Parameters
        ----------
        symmetry : float
            Symmetry in percent (0-100)
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        self.write(f"SOURce{channel}:FUNC:RAMP:SYMM {symmetry}")

    def get_ramp_symmetry(self, channel=1):
        """Get the ramp symmetry.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Returns
        -------
        float
            Symmetry in percent (0-100)

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        return float(self.query(f"SOURce{channel}:FUNC:RAMP:SYMM?"))

    def set_trigger_source(self, source):
        """Set the trigger source.

        Parameters
        ----------
        source : str
            Trigger source (IMM, EXT, BUS, KEY, TIM, MAN)
        """
        if source not in [s.value for s in TriggerSource]:
            raise ValueError(f"Invalid trigger source. Must be one of {[s.value for s in TriggerSource]}")
        self.write(f"TRIG:SOUR {source}")

    def get_trigger_source(self):
        """Get the current trigger source.

        Returns
        -------
        str
            Current trigger source
        """
        return self.query("TRIG:SOUR?")

    def set_trigger_slope(self, slope):
        """Set the trigger slope.

        Parameters
        ----------
        slope : str
            Trigger slope (POS, NEG, EITH)
        """
        if slope not in [s.value for s in TriggerSlope]:
            raise ValueError(f"Invalid trigger slope. Must be one of {[s.value for s in TriggerSlope]}")
        self.write(f"TRIG:SLOP {slope}")

    def get_trigger_slope(self):
        """Get the current trigger slope.

        Returns
        -------
        str
            Current trigger slope
        """
        return self.query("TRIG:SLOP?")

    def set_trigger_delay(self, delay):
        """Set the trigger delay.

        Parameters
        ----------
        delay : float
            Trigger delay in seconds
        """
        self.write(f"TRIG:DEL {delay}")

    def get_trigger_delay(self):
        """Get the current trigger delay.

        Returns
        -------
        float
            Current trigger delay in seconds
        """
        return float(self.query("TRIG:DEL?"))

    def set_trigger_count(self, count):
        """Set the trigger count.

        Parameters
        ----------
        count : int
            Number of triggers (1-65535 or INF)
        """
        if count != "INF" and not (1 <= count <= 65535):
            raise ValueError("Trigger count must be between 1 and 65535 or INF")
        self.write(f"TRIG:COUN {count}")

    def get_trigger_count(self):
        """Get the current trigger count.

        Returns
        -------
        str or int
            Current trigger count (INF or integer)
        """
        return self.query("TRIG:COUN?")

    def set_output_impedance(self, impedance, channel=1):
        """Set the output impedance.

        Parameters
        ----------
        impedance : float
            Output impedance in ohms
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        self.write(f"OUTP{channel}:IMP {impedance}")

    def get_output_impedance(self, channel=1):
        """Get the output impedance.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Returns
        -------
        float
            Output impedance in ohms

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        return float(self.query(f"OUTP{channel}:IMP?"))

    def set_output_polarity(self, polarity, channel=1):
        """Set the output polarity.

        Parameters
        ----------
        polarity : str
            Output polarity (NORM or INV)
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        if polarity not in ["NORM", "INV"]:
            raise ValueError("Polarity must be either NORM or INV")
        self.write(f"OUTP{channel}:POL {polarity}")

    def get_output_polarity(self, channel=1):
        """Get the output polarity.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2). For 33521B and 33522B only.

        Returns
        -------
        str
            Current output polarity (NORM or INV)

        Raises
        ------
        ValueError
            If dual channel operation is not available and channel=2
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")

        return self.query(f"OUTP{channel}:POL?")

    def get_system_error(self):
        """Get the most recent system error.

        Returns
        -------
        str
            Error message
        """
        return self.query("SYST:ERR?")

    def get_system_version(self):
        """Get the system version.

        Returns
        -------
        str
            System version
        """
        return self.query("SYST:VERS?")

    def get_system_date(self):
        """Get the system date.

        Returns
        -------
        str
            System date
        """
        return self.query("SYST:DATE?")

    def get_system_time(self):
        """Get the system time.

        Returns
        -------
        str
            System time
        """
        return self.query("SYST:TIME?")

    # Override incorrect inherited methods with correct SCPI commands
    def set_polarity(self, polarity, channel=1):
        """Set the polarity of a channel.

        Parameters
        ----------
        polarity : str
            Either "NORM" for normal or "INV" for inverse
        channel : int
            The channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        if polarity not in ["NORM", "INV"]:
            raise ValueError("Polarity must be either NORM or INV")
            
        self.write(f"OUTP{channel}:POL {polarity}")

    def get_polarity(self, channel=1):
        """Get the polarity of a channel.

        Parameters
        ----------
        channel : int
            The channel number (1 or 2)

        Returns
        -------
        str
            Current polarity (NORM or INV)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        return self.query(f"OUTP{channel}:POL?")

    def set_trigger_source(self, source):
        """Set the trigger source.

        Parameters
        ----------
        source : str
            Trigger source (IMM, EXT, BUS, KEY, TIM, MAN)
        """
        if source not in [s.value for s in TriggerSource]:
            raise ValueError(f"Invalid trigger source. Must be one of {[s.value for s in TriggerSource]}")
        self.write(f"TRIG:SOUR {source}")

    def get_trigger_source(self):
        """Get the current trigger source.

        Returns
        -------
        str
            Current trigger source
        """
        return self.query("TRIG:SOUR?")

    def set_trigger_slope(self, slope):
        """Set the trigger slope.

        Parameters
        ----------
        slope : str
            Trigger slope (POS, NEG, EITH)
        """
        if slope not in [s.value for s in TriggerSlope]:
            raise ValueError(f"Invalid trigger slope. Must be one of {[s.value for s in TriggerSlope]}")
        self.write(f"TRIG:SLOP {slope}")

    def get_trigger_slope(self):
        """Get the current trigger slope.

        Returns
        -------
        str
            Current trigger slope
        """
        return self.query("TRIG:SLOP?")

    def set_delay(self, delay, channel=1):
        """Set the delay of a channel.

        Parameters
        ----------
        delay : float
            The delay in seconds
        channel : int
            The channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        self.write(f"SOURce{channel}:BURS:TDEL {delay}")

    def set_out_impedance(self, imp, channel=1):
        """Set the output impedance of a channel.

        Parameters
        ----------
        imp : float
            The impedance value in ohms
        channel : int
            The channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        self.write(f"OUTP{channel}:IMP {imp}")

    def get_out_impedance(self, channel=1):
        """Get the output impedance of a channel.

        Parameters
        ----------
        channel : int
            The channel number (1 or 2)

        Returns
        -------
        float
            The impedance value in ohms
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        return float(self.query(f"OUTP{channel}:IMP?"))

    def set_width(self, width, channel=1):
        """Set the pulse width.

        Parameters
        ----------
        width : float
            The pulse width in seconds
        channel : int
            The channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        self.write(f"SOURce{channel}:FUNC:PULS:WIDT {width}")

    def set_high(self, high, channel=1):
        """Set the high voltage level.

        Parameters
        ----------
        high : float
            The high voltage level in volts
        channel : int
            The channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        self.write(f"SOURce{channel}:VOLT:HIGH {high}")

    def set_low(self, low, channel=1):
        """Set the low voltage level.

        Parameters
        ----------
        low : float
            The low voltage level in volts
        channel : int
            The channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        self.write(f"SOURce{channel}:VOLT:LOW {low}")

    @property
    def output1(self):
        """Get the output state of channel 1.

        Returns
        -------
        bool
            True if output is enabled, False otherwise
        """
        return bool(int(self.query("OUTP1?")))

    @output1.setter
    def output1(self, val):
        """Set the output state of channel 1.

        Parameters
        ----------
        val : bool
            True to enable output, False to disable
        """
        self.write(f"OUTP1 {'ON' if val else 'OFF'}")

    @property
    def output2(self):
        """Get the output state of channel 2.

        Returns
        -------
        bool
            True if output is enabled, False otherwise
        """
        if not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return bool(int(self.query("OUTP2?")))

    @output2.setter
    def output2(self, val):
        """Set the output state of channel 2.

        Parameters
        ----------
        val : bool
            True to enable output, False to disable
        """
        if not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"OUTP2 {'ON' if val else 'OFF'}")

    @property
    def combined(self):
        """Get the combined output state.

        Returns
        -------
        bool
            True if channels are combined, False otherwise
        """
        if not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return self.query("CHAN:MATH?") == "PLUS"

    @combined.setter
    def combined(self, val):
        """Set the combined output state.

        Parameters
        ----------
        val : bool
            True to combine channels, False to separate
        """
        if not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"CHAN:MATH {'PLUS' if val else 'OFF'}")

    @property
    def trigger_level(self):
        """Get the trigger level.

        Returns
        -------
        float
            Trigger level in volts
        """
        return float(self.query("TRIG:LEV?"))

    @trigger_level.setter
    def trigger_level(self, val):
        """Set the trigger level.

        Parameters
        ----------
        val : float
            Trigger level in volts
        """
        self.write(f"TRIG:LEV {val}")

    def get_all_errors(self):
        """Get all errors from the error queue.

        Returns
        -------
        list
            List of (error_code, error_message) tuples
        """
        errors = []
        while True:
            error = self.query("SYST:ERR?")
            code, message = error.split(",")
            code = int(code)
            message = message.strip('"')
            if code == 0:  # No error
                break
            errors.append((code, message))
        return errors

    def clear_error_queue(self):
        """Clear the error queue by reading all errors."""
        while True:
            error = self.query("SYST:ERR?")
            code = int(error.split(",")[0])
            if code == 0:  # No error
                break
