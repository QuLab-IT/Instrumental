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
            raise ValueError("{} is not a valid {} enum".format(arg, enum_type.__name__))
    return convert


class TriggerSource(Enum):
    bus = 'BUS'
    immediate = 'IMMMEDIATE'
    external = 'EXT'
    key = 'KEY'
    timer = 'TIMER'
    manual = 'MAN'
    
    
class TriggerSensing(Enum):
    edge = 'EDGE'
    level = 'LEV'
    
    
class TriggerSlope(Enum):
    positive = 'POS'
    negative = 'NEG'
    either = 'EITH'


class FreqMode(Enum):
    cw = fixed = 'FIXED'
    list = 'LIST'


class AgilentMXG(FunctionGenerator, VisaMixin):
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('Agilent Technologies', ['N5181A'])

    def _initialize(self):
        self._rsrc.read_termination = '\n'

    cw_frequency = SCPI_Facet('FREQ:CW', convert=float, units='Hz')
    sweep_center_frequency = SCPI_Facet('FREQ:CENTER', convert=float, units='Hz')
    sweep_span_frequency = SCPI_Facet('FREQ:SPAN', convert=float, units='Hz')
    sweep_start_frequency = SCPI_Facet('FREQ:START', convert=float, units='Hz')
    sweep_stop_frequency = SCPI_Facet('FREQ:STOP', convert=float, units='Hz')

    freq_mode = SCPI_Facet('FREQ:MODE', convert=_convert_enum(FreqMode))

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
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('Agilent Technologies', ['33250A'])

    def _initialize(self):
        self._rsrc.read_termination = '\n'

    frequency = SCPI_Facet('FREQ', convert=float, units='Hz')
    voltage = SCPI_Facet('VOLT', convert=float, units='V')

class AgilentE4400B(FunctionGenerator, VisaMixin):
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('Hewlett-Packard', ['ESG-1000B'])
    width1 = SCPI_Facet('PULS:WIDTh1 ', convert=float, units='ns')
    width2 = SCPI_Facet('SOURce2:FUNCtion:PULSe:WIDTh', convert=float, units='s')

    def _initialize(self):
        self._rsrc.read_termination = '\n'

    frequency = SCPI_Facet('FREQ:FIXED', convert=float, units='Hz')

class AgilentFuncGenerator(FunctionGenerator, VisaMixin):
    def set_polarity(self, polarity, channel=1):
        """ Set the polarity of a channel.

        Parameters
        ----------
        pol : either "NORM" for normal or "INV" for inverse
        
        channel: int
            The channel number
        """
        self.write('OUTP{:d}:POL {}', channel, polarity)
    
    def get_polarity(self, channel=1):
        return self.query("OUTP{:d}:POL?", channel)
    
    def set_trigger_source(self, source):
        """ Set the trigger source.

        Parameters
        ----------
        source : either "MAN" for manual or "EXT" for external
        """
        self.write('ARM:SOUR ' + source)

    
    def get_trigger_source(self):
        return TriggerSource(self.query("ARM:SOUR?")).name
    
    def set_trigger_sensing(self, sensing):
        """ Set the trigger sensing.
    
        Parameters
        ----------
        sensing : either "EDGE" for edge or "LEV" for level
        """
        self.write('ARM:SENS ' + sensing)
    
    def get_trigger_sensing(self):
        return TriggerSensing(self.query("ARM:SENS?")).name
    
    def set_trigger_slope(self, slope):
        """ Set the trigger slope.
    
        Parameters
        ----------
        slope : either "POS" for positive or "NEG" for negative or "EITH" for either.
        """
        self.write('ARM:SLOP ' + slope)
    
    def get_trigger_slope(self):
        return TriggerSlope(self.query("ARM:SLOP?")).name
    
    def get_errors(self):
        return self.query('SYST:ERR?')

    def set_delay(self, delay, channel=1):
        """ Set the delay of a channel.

        Parameters
        ----------
        delay: pint.Quantity
            The new delay in nanosecond-compatible units
        
        channel: int
            The channel number
        """
        val = Q_(delay)
        mag = val.to('ns').magnitude
        self.write('PULS:DEL{:d} {}NS', channel, mag)

    def set_out_impedance(self, imp, channel=1):
        """ Set the output impedance of a channel.

        Parameters
        ----------
        imp : pint.Quantity
            The impedance value in Ohm
        
        channel: int
            The channel number
        """
        val = Q_(imp)
        mag = val.to('ohm').magnitude
        self.write('OUTP{:d}:IMP:EXT {:f}OHM', channel, mag)

    def set_width(self, width, channel=1):
        """ Set the width.

        Parameters
        ----------
        width : pint.Quantity
            The new width in nanosecond-compatible units
        
        channel: int
            Channel number
        """
        val = Q_(width)
        mag = val.to('ns').magnitude
        self.write('PULS:WIDTh{:d} {:f}NS', channel, mag)

    def set_high(self, high, channel=1):
        """ Set the high voltage level.

        This changes the high level while keeping the low level fixed.
        
        Parameters
        ----------
        high : pint.Quantity
            The new high level in volt-compatible units
        
        channel: int
            Channel number
        """
        high = Q_(high)
        mag = high.to('V').magnitude
        self.write('VOLT{:d}:HIGH {:5.2f}V', channel, mag)

    def set_low(self, low, channel=1):
        """ Set the low voltage level.

        This changes the low level while keeping the high level fixed.

        Parameters
        ----------
        low : pint.Quantity
            The new low level in volt-compatible units
        
        channel: int
            Channel number
        """
        low = Q_(low)
        mag = low.to('V').magnitude
        self.write('VOLT{:d}:LOW {:5.2f}V', channel, mag)

    @property
    def output1(self):
        val = self.query(':OUTP1?')
        return bool(int(val))

    @output1.setter
    def output1(self, val):
        val = int(bool(val))
        self.write('OUTP1 %s' % OnOffState(val).name)

    @property
    def output2(self):
        val = self.query('OUTP2?')
        return bool(int(val))

    @output2.setter
    def output2(self, val):
        val = int(bool(val))
        self.write('OUTP2 %s' % OnOffState(val).name)
    
    @property
    def combined(self):
        val = self.query('CHAN:MATH?')
        if val == "PLUS":
            return True
        else:
            return False
    
    @combined.setter
    def combined(self, val):
        val = int(bool(val))
        self.write('CHAN:MATH ' + CombinedState(val).name)
    
    @property
    def trigger_level(self):
        val = self.query('ARM:LEV?')
        return Q_(val, u.V)
    
    @trigger_level.setter
    def trigger_level(self, val):
        low = Q_(val)
        mag = low.to('V').magnitude
        self.write('ARM:LEV {:5.2f}V', mag)

class Agilent81110A(AgilentFuncGenerator):
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('HEWLETT-PACKARD', ['HP81110A'])

    def _initialize(self):
        self._rsrc.read_termination = '\n'
    
    def set_subsystem(self, subsystem, channel=1):
        """ Switch between substems commands.

        Parameters
        ----------
        subsystem : either "VOLT" for voltage or "CURR" for current.
        
        channel: int
            Channel number
        """
        self.write('HOLD{:d} {}', channel, subsystem)


class Keysight81160A(AgilentFuncGenerator):
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('Agilent Technologies', ['81160A'])
   
    def _initialize(self):
        self._rsrc.read_termination = '\n'

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
    _INST_PARAMS_ = ['visa_address']
    _INST_VISA_INFO_ = ('Keysight Technologies', ['33511B', '33512B', '33521B', '33522B'])

    def _initialize(self):
        """Initialize the instrument."""
        super()._initialize()
        self._rsrc.read_termination = '\n'
        self._rsrc.write_termination = '\n'
        
        # Get model information
        idn = self.query('*IDN?').strip().split(',')
        self.model = idn[1]  # Store model number for feature checking
        
    def _check_arbitrary_capability(self):
        """Check if the model supports arbitrary waveforms.
        
        Returns
        -------
        bool
            True if the model supports arbitrary waveforms (33512B or 33522B)
        """
        return self.model in ['33512B', '33522B']
        
    def _check_dual_channel(self):
        """Check if the model supports dual channel operation.
        
        Returns
        -------
        bool
            True if the model supports dual channel (33521B or 33522B)
        """
        return self.model in ['33521B', '33522B']

    # Basic waveform parameters
    frequency = SCPI_Facet('FREQ', convert=float, units='Hz')
    voltage = SCPI_Facet('VOLT', convert=float, units='V')
    voltage_offset = SCPI_Facet('VOLT:OFFS', convert=float, units='V')
    
    # Function selection
    function = SCPI_Facet('FUNC', convert=str)
    function_shape = SCPI_Facet('FUNC:SHAP', convert=str)
    
    # Burst mode settings
    burst_mode = SCPI_Facet('BURS:MODE', convert=str)
    burst_ncycles = SCPI_Facet('BURS:NCYC', convert=int)
    burst_phase = SCPI_Facet('BURS:PHAS', convert=float, units='deg')
    
    # Modulation settings
    modulation_state = SCPI_Facet('MOD:STAT', convert=bool)
    modulation_type = SCPI_Facet('MOD:TYP', convert=str)
    modulation_depth = SCPI_Facet('MOD:DEPT', convert=float)
    modulation_rate = SCPI_Facet('MOD:RATE', convert=float, units='Hz')
    
    # Sweep settings
    sweep_state = SCPI_Facet('SWE:STAT', convert=bool)
    sweep_time = SCPI_Facet('SWE:TIME', convert=float, units='s')
    sweep_spacing = SCPI_Facet('SWE:SPAC', convert=str)
    
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
            raise ValueError("Arbitrary waveform capability not available on this model")
            
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        # Convert data to string format
        data_str = ','.join(f'{x:.6f}' for x in waveform_data)
        
        # Set sample rate if specified
        if sample_rate is not None:
            self.write(f'FUNC:ARB:SRAT {sample_rate}, (@{channel})')
            
        # Load waveform data
        self.write(f'DATA:ARB:DAC16 {data_str}, (@{channel})')
        
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
            raise ValueError("Arbitrary waveform capability not available on this model")
            
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        data_str = self.query(f'DATA:ARB:DAC16? (@{channel})')
        return [float(x) for x in data_str.split(',')]
    
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
            raise ValueError("Arbitrary waveform capability not available on this model")
            
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        # Convert data to string format
        data_str = ','.join(f'{x:.6f}' for x in waveform_data)
        
        # Set sample rate if specified
        if sample_rate is not None:
            self.write(f'FUNC:ARB:SRAT {sample_rate}, (@{channel})')
            
        # Save waveform data
        self.write(f'DATA:ARB:DAC16 {name},{data_str}, (@{channel})')
        
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
            raise ValueError("Arbitrary waveform capability not available on this model")
            
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        self.write(f'FUNC:ARB {name}, (@{channel})')
        
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
            raise ValueError("Arbitrary waveform capability not available on this model")
            
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        return self.query(f'DATA:ARB:CAT? (@{channel})').strip('"').split(',')
        
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
            raise ValueError("Arbitrary waveform capability not available on this model")
            
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
            
        self.write(f'DATA:ARB:DEL {name}, (@{channel})')
        
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
            
        self.write(f'PHAS {phase}, (@{channel})')
        
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
            
        return float(self.query(f'PHAS? (@{channel})'))
        
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
            
        self.write(f'FUNC:PULS:DCYC {duty_cycle}, (@{channel})')
        
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
            
        return float(self.query(f'FUNC:PULS:DCYC? (@{channel})'))
        
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
            
        self.write(f'FUNC:RAMP:SYMM {symmetry}, (@{channel})')
        
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
            
        return float(self.query(f'FUNC:RAMP:SYMM? (@{channel})'))