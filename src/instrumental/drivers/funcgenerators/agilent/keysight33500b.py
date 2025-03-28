"""Driver for Keysight 33500B Series Waveform Generators."""

from enum import Enum
from typing import List, Tuple, Union, Optional, Any

from .... import u, Q_
from ... import VisaMixin
from .. import FunctionGenerator


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

    TRIGGERED = "TRIG"  # Triggered burst mode (default)
    GATED = "GAT"  # External gated burst mode


class SweepSpacing(Enum):
    """Available sweep spacing modes."""

    LIN = "LIN"
    LOG = "LOG"


class SweepMode(Enum):
    """Available sweep modes."""

    AUTO = "AUTO"
    MANUAL = "MAN"
    STEP = "STEP"


class SweepDirection(Enum):
    """Available sweep directions."""

    UP = "UP"
    DOWN = "DOWN"
    BIDIRECTIONAL = "BID"


class ModulationType(Enum):
    """Available modulation types."""

    AM = "AM"
    FM = "FM"
    PM = "PM"
    FSK = "FSK"
    PWM = "PWM"


class TriggerSource(Enum):
    """Available trigger sources."""

    IMM = "IMM"
    EXT = "EXT"
    BUS = "BUS"
    TIM = "TIM"


class TriggerSlope(Enum):
    """Available trigger slopes."""

    POS = "POS"  # Positive (rising edge)
    NEG = "NEG"  # Negative (falling edge)


class BurstGatePolarity(Enum):
    """Available burst gate polarity values."""

    NORM = "NORM"
    INV = "INV"


class OutputMode(Enum):
    """Available output modes."""

    NORMAL = "NORM"
    GATED = "GAT"


class SyncMode(Enum):
    """Available sync output modes."""

    NORMAL = "NORM"
    CARRIER = "CARR"
    MARKER = "MARK"


class SyncPolarity(Enum):
    """Available sync output polarity values."""

    NORMAL = "NORM"
    INVERTED = "INV"


class TriggerOutputSlope(Enum):
    """Available trigger output slope values."""

    POSITIVE = "POS"
    NEGATIVE = "NEG"


class OutputPolarity(Enum):
    """Available output polarity values."""

    NORMAL = "NORM"
    INVERTED = "INV"


class OnOff(Enum):
    """Available ON/OFF states."""

    ON = 1
    OFF = 0


class AngleUnit(Enum):
    """Available angle units."""

    DEGREES = "DEG"
    RADIANS = "RAD"


class Keysight33500B(FunctionGenerator, VisaMixin):
    """Driver for Keysight 33500B Series Waveform Generators.

    This driver supports the 33500B Series of waveform generators, including:
    - 33509B (1 channel, 20 MHz, no arbitrary waveforms)
    - 33510B (2 channels, 20 MHz, no arbitrary waveforms)
    - 33511B (1 channel, 20 MHz, with arbitrary waveform)
    - 33512B (2 channels, 20 MHz, with arbitrary waveform)
    - 33519B (1 channel, 30 MHz, no arbitrary waveforms)
    - 33520B (2 channels, 30 MHz, no arbitrary waveforms)
    - 33521B (1 channel, 30 MHz, with arbitrary waveform)
    - 33522B (2 channels, 30 MHz, with arbitrary waveform)

    Model-Specific Features:
    -----------------------
    33509B/33519B:
        - Single channel output
        - Standard waveforms (sine, square, triangle, ramp, pulse, noise, DC)
        - Basic modulation (AM, FM, PM, FSK, PWM)
        - Burst mode
        - Sweep mode
        - Triggering capabilities
        - Optional: High-stability OCXO Timebase
        - Optional: NISPOM & File Security

    33510B/33520B:
        - All features of 33509B/33519B
        - Dual channel output
        - Channel synchronization
        - Channel phase control
        - Channel math operations (add, subtract, multiply)
        - Optional: High-stability OCXO Timebase
        - Optional: NISPOM & File Security

    33511B/33521B:
        - All features of 33509B/33519B
        - Arbitrary waveform capability
        - Waveform memory management
        - Waveform editing and downloading
        - Optional: 16MSa Memory
        - Optional: High-stability OCXO Timebase
        - Optional: NISPOM & File Security

    33512B/33522B:
        - All features of 33510B/33520B
        - Arbitrary waveform capability on both channels
        - Waveform memory management
        - Waveform editing and downloading
        - Dual arbitrary waveform playback
        - Optional: 16MSa Memory
        - Optional: High-stability OCXO Timebase
        - Optional: NISPOM & File Security
        - Optional: IQ Baseband signal player

    Common Features:
    --------------
    - Frequency range: 1 µHz to 20/30 MHz (depending on model)
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
        [
            "33509B",
            "33510B",
            "33511B",
            "33512B",
            "33519B",
            "33520B",
            "33521B",
            "33522B",
        ],
    )

    def _initialize(self) -> None:
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

    def clear_error_queue(self) -> None:
        """Clear the error queue by reading all errors until none remain."""
        while True:
            error = self.query("SYST:ERR?")
            if error.startswith("+0"):
                break

    def abort(self) -> None:
        """Abort any ongoing sequence, list, sweep, or burst operation.

        This command:
        - Halts any triggered action (triggered list, sweep, burst, or arbitrary waveform playback)
        - Returns trigger subsystem to idle state
        - If INITiate:CONTinuous is ON, instrument immediately proceeds to wait-for-trigger state
        - Applies to both channels in a two-channel instrument
        - For sweeps, returns to starting sweep frequency
        - For lists, returns to normal mode frequency until first trigger
        """
        self.write("ABOR")

    def get_apply_config(self, channel: int = 1) -> Tuple[str, float, float, float]:
        """Query current output configuration.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        tuple
            (function, frequency, amplitude, offset)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        response = self.query(f"SOURce{channel}:APPLy?").strip()
        # Parse response like "SIN +5.000000000000000E+03,+3.0000000000000E+00,-2.5000000000000E+00"
        parts = response.split()
        func = parts[0]
        values = [float(x) for x in parts[1].split(",")]
        return (func, values[0], values[1], values[2])

    def _check_arbitrary_capability(self) -> bool:
        """Check if the model supports arbitrary waveforms.

        Returns
        -------
        bool
            True if the model supports arbitrary waveforms (33511B, 33512B, 33521B, or 33522B)
        """
        return self.model in ["33511B", "33512B", "33521B", "33522B"]

    def _check_dual_channel(self) -> bool:
        """Check if the model supports dual channel operation.

        Returns
        -------
        bool
            True if the model supports dual channel (33510B, 33512B, 33520B, or 33522B)
        """
        return self.model in ["33510B", "33512B", "33520B", "33522B"]

    @staticmethod
    def _format_float(f: float) -> str:
        """Convert float to string with 6 decimal places."""
        return f"{f:.6f}"

    @staticmethod
    def _format_int(i: int) -> str:
        """Convert int to string."""
        return str(i)

    def get_frequency(self, channel: int = 1) -> float:
        """Get the output frequency.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Frequency in Hz
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:FREQ?"))

    def set_frequency(self, frequency: float, channel: int = 1) -> None:
        """Set the output frequency.

        Parameters
        ----------
        frequency : float
            Frequency in Hz
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FREQ {self._format_float(frequency)}")

    def get_voltage(self, channel: int = 1) -> float:
        """Get the output voltage.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Voltage in V
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:VOLT?"))

    def set_voltage(self, voltage: float, channel: int = 1) -> None:
        """Set the output voltage.

        Parameters
        ----------
        voltage : float
            Voltage in V
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:VOLT {self._format_float(voltage)}")

    def get_voltage_offset(self, channel: int = 1) -> float:
        """Get the DC offset voltage.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            DC offset voltage in V
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:VOLT:OFFS?"))

    def set_voltage_offset(self, offset: float, channel: int = 1) -> None:
        """Set the DC offset voltage.

        Parameters
        ----------
        offset : float
            DC offset voltage in V
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:VOLT:OFFS {self._format_float(offset)}")

    def get_function(self, channel: int = 1) -> WaveformShape:
        """Get the output function.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        WaveformShape
            Current waveform shape
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return WaveformShape(self.query(f"SOURce{channel}:FUNC?"))

    def set_function(self, function: WaveformShape, channel: int = 1) -> None:
        """Set the output function.

        Parameters
        ----------
        function : WaveformShape
            Waveform shape to set
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FUNC {function.value}")

    def get_function_shape(self, channel: int = 1) -> WaveformShape:
        """Get the output function shape.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        WaveformShape
            Current waveform shape
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return WaveformShape(self.query(f"SOURce{channel}:FUNC:SHAP?"))

    def set_function_shape(self, shape: WaveformShape, channel: int = 1) -> None:
        """Set the output function shape.

        Parameters
        ----------
        shape : WaveformShape
            Waveform shape to set
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FUNC:SHAP {shape.value}")

    def get_duty_cycle(self, channel: int = 1) -> float:
        """Get the pulse duty cycle.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Duty cycle in percent
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:FUNC:PULS:DCYC?"))

    def set_duty_cycle(self, duty_cycle: float, channel: int = 1) -> None:
        """Set the pulse duty cycle.

        Parameters
        ----------
        duty_cycle : float
            Duty cycle in percent
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FUNC:PULS:DCYC {self._format_float(duty_cycle)}")

    def get_ramp_symmetry(self, channel: int = 1) -> float:
        """Get the ramp symmetry.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Ramp symmetry in percent
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:FUNC:RAMP:SYMM?"))

    def set_ramp_symmetry(self, symmetry: float, channel: int = 1) -> None:
        """Set the ramp symmetry.

        Parameters
        ----------
        symmetry : float
            Ramp symmetry in percent
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FUNC:RAMP:SYMM {self._format_float(symmetry)}")

    def get_phase(self, channel: int = 1) -> float:
        """Get the output phase.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Phase in degrees
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:PHAS?"))

    def set_phase(self, phase: float, channel: int = 1) -> None:
        """Set the output phase.

        Parameters
        ----------
        phase : float
            Phase in degrees
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:PHAS {self._format_float(phase)}")

    def get_burst_mode(self, channel: int = 1) -> BurstMode:
        """Get the burst mode.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        BurstMode
            Current burst mode
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return BurstMode(self.query(f"SOURce{channel}:BURS:MODE?"))

    def set_burst_mode(self, mode: BurstMode, channel: int = 1) -> None:
        """Set the burst mode.

        Parameters
        ----------
        mode : BurstMode
            Burst mode to set
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:BURS:MODE {mode.value}")

    def get_burst_ncycles(self, channel: int = 1) -> Union[int, str]:
        """Get the number of cycles in burst mode.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        Union[int, str]
            Number of cycles or "INF" for infinite
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        response = self.query(f"SOURce{channel}:BURS:NCYC?").strip()
        if response.upper() == "INF":
            return "INF"
        return int(float(response))

    def set_burst_ncycles(self, ncycles: Union[int, str], channel: int = 1) -> None:
        """Set the number of cycles in burst mode.

        Parameters
        ----------
        ncycles : Union[int, str]
            Number of cycles (1 to 100,000,000) or "INF" for infinite
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        if isinstance(ncycles, str) and ncycles.upper() == "INF":
            self.write(f"SOURce{channel}:BURS:NCYC INF")
        else:
            if not (1 <= ncycles <= 100000000):
                raise ValueError("Number of cycles must be between 1 and 100,000,000")
            self.write(f"SOURce{channel}:BURS:NCYC {self._format_int(ncycles)}")

    def get_burst_phase(self, channel: int = 1) -> float:
        """Get the burst phase.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Phase in degrees
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:BURS:PHAS?"))

    def set_burst_phase(self, phase: float, channel: int = 1) -> None:
        """Set the burst phase.

        Parameters
        ----------
        phase : float
            Phase in degrees
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:BURS:PHAS {self._format_float(phase)}")

    def get_burst_gate_polarity(self, channel: int = 1) -> BurstGatePolarity:
        """Get the burst gate polarity.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        BurstGatePolarity
            Current burst gate polarity
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return BurstGatePolarity(self.query(f"SOURce{channel}:BURS:GATE:POL?"))

    def set_burst_gate_polarity(
        self, polarity: BurstGatePolarity, channel: int = 1
    ) -> None:
        """Set the burst gate polarity.

        Parameters
        ----------
        polarity : BurstGatePolarity
            Burst gate polarity to set
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:BURS:GATE:POL {polarity.value}")

    def get_am_dssc(self, channel: int = 1) -> OnOff:
        """Get the Double Sideband Suppressed Carrier mode for AM.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        OnOff
            Current DSSC mode state (ON or OFF).
            When ON, zero modulation results in zero output signal, and increasing modulation input signal raises the amplitude of the sidebands.
            When OFF, zero modulation results in a half-amplitude carrier wave signal being output.
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return OnOff(int(self.query(f"SOURce{channel}:AM:DSSC?").strip()))

    def set_am_dssc(self, state: OnOff, channel: int = 1) -> None:
        """Set the Double Sideband Suppressed Carrier mode for AM.

        Parameters
        ----------
        state : OnOff
            DSSC mode state to set (ON or OFF).
            When ON, zero modulation results in zero output signal, and increasing modulation input signal raises the amplitude of the sidebands.
            When OFF, zero modulation results in a half-amplitude carrier wave signal being output.
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:AM:DSSC {state.value}")

    def get_am_internal_freq(self, channel: int = 1) -> float:
        """Get the internal modulation frequency.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Internal modulation frequency in Hz.
            Range: 1 µHz to maximum allowed for the internal function (default 100 Hz).
            For TRIangle, UpRamp, or DnRamp: limited to 200 kHz.
            For PRBS: limited to 50 Mbps (refers to bit rate).
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:AM:INT:FREQ?"))

    def set_am_internal_freq(self, frequency: float, channel: int = 1) -> None:
        """Set the internal modulation frequency.

        Parameters
        ----------
        frequency : float
            Internal modulation frequency in Hz.
            Range: 1 µHz to maximum allowed for the internal function (default 100 Hz).
            For TRIangle, UpRamp, or DnRamp: limited to 200 kHz.
            For PRBS: limited to 50 Mbps (refers to bit rate).
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:AM:INT:FREQ {self._format_float(frequency)}")

    def get_am_internal_func(self, channel: int = 1) -> WaveformShape:
        """Get the internal modulation waveform shape.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        WaveformShape
            Current internal modulation waveform shape.
            Available shapes: SINusoid, SQUare, RAMP, NRAMp, TRIangle, NOISe, PRBS, ARB.
            Default: SINusoid.
            Note: Pulse and DC cannot be carrier waveform for AM.
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return WaveformShape(self.query(f"SOURce{channel}:AM:INT:FUNC?"))

    def set_am_internal_func(self, shape: WaveformShape, channel: int = 1) -> None:
        """Set the internal modulation waveform shape.

        Parameters
        ----------
        shape : WaveformShape
            Internal modulation waveform shape to set.
            Available shapes: SINusoid, SQUare, RAMP, NRAMp, TRIangle, NOISe, PRBS, ARB.
            Default: SINusoid.
            Note: Pulse and DC cannot be carrier waveform for AM.
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:AM:INT:FUNC {shape.value}")

    def get_sweep_state(self, channel: int = 1) -> OnOff:
        """Get the sweep state.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        OnOff
            Current sweep state (ON or OFF)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return OnOff(int(self.query(f"SOURce{channel}:SWE:STAT?").strip()))

    def set_sweep_state(self, state: OnOff, channel: int = 1) -> None:
        """Set the sweep state.

        Parameters
        ----------
        state : OnOff
            Sweep state to set (ON or OFF)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:SWE:STAT {state.value}")

    def get_sweep_time(self, channel: int = 1) -> float:
        """Get the sweep time.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Sweep time in seconds
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:SWE:TIME?"))

    def set_sweep_time(self, time: float, channel: int = 1) -> None:
        """Set the sweep time.

        Parameters
        ----------
        time : float
            Sweep time in seconds
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:SWE:TIME {self._format_float(time)}")

    def get_sweep_spacing(self, channel: int = 1) -> SweepSpacing:
        """Get the sweep spacing mode.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        SweepSpacing
            Current sweep spacing mode (LINear or LOGarithmic)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return SweepSpacing(self.query(f"SOURce{channel}:SWE:SPAC?"))

    def set_sweep_spacing(self, spacing: SweepSpacing, channel: int = 1) -> None:
        """Set the sweep spacing mode.

        Parameters
        ----------
        spacing : SweepSpacing
            Sweep spacing mode to set (LINear or LOGarithmic)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:SWE:SPAC {spacing.value}")

    def get_sweep_return_time(self, channel: int = 1) -> float:
        """Get the sweep return time.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Sweep return time in seconds
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:SWE:RTIM?"))

    def set_sweep_return_time(self, time: float, channel: int = 1) -> None:
        """Set the sweep return time.

        Parameters
        ----------
        time : float
            Sweep return time in seconds
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:SWE:RTIM {self._format_float(time)}")

    def get_trigger_source(self) -> TriggerSource:
        """Get the trigger source.

        Returns
        -------
        TriggerSource
            Current trigger source (IMMediate, EXTernal, BUS, or TIMer)
        """
        return TriggerSource(self.query("TRIG:SOUR?"))

    def set_trigger_source(self, source: TriggerSource) -> None:
        """Set the trigger source.

        Parameters
        ----------
        source : TriggerSource
            Trigger source to set (IMMediate, EXTernal, BUS, or TIMer)
        """
        self.write(f"TRIG:SOUR {source.value}")

    def get_trigger_slope(self) -> TriggerSlope:
        """Get the trigger slope.

        Returns
        -------
        TriggerSlope
            Current trigger slope (POSitive or NEGative)
        """
        return TriggerSlope(self.query("TRIG:SLOP?"))

    def set_trigger_slope(self, slope: TriggerSlope) -> None:
        """Set the trigger slope.

        Parameters
        ----------
        slope : TriggerSlope
            Trigger slope to set (POSitive or NEGative)
        """
        self.write(f"TRIG:SLOP {slope.value}")

    def get_trigger_delay(self) -> float:
        """Get the trigger delay.

        Returns
        -------
        float
            Trigger delay in seconds
        """
        return float(self.query("TRIG:DEL?"))

    def set_trigger_delay(self, delay: float) -> None:
        """Set the trigger delay.

        Parameters
        ----------
        delay : float
            Trigger delay in seconds
        """
        self.write(f"TRIG:DEL {self._format_float(delay)}")

    def get_trigger_count(self) -> int:
        """Get the trigger count.

        Returns
        -------
        int
            Number of triggers to generate
        """
        response = self.query("TRIG:COUN?")
        if response.upper() == "INF":
            return "INF"
        return int(float(response))

    def set_trigger_count(self, count: int) -> None:
        """Set the trigger count.

        Parameters
        ----------
        count : int
            Number of triggers to generate
        """
        self.write(f"TRIG:COUN {self._format_int(count)}")

    def get_output_state(self, channel: int = 1) -> OnOff:
        """Get the output state.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        OnOff
            Current output state (ON or OFF)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return OnOff(int(self.query(f"OUTP{channel}?").strip()))

    def set_output_state(self, state: OnOff, channel: int = 1) -> None:
        """Set the output state.

        Parameters
        ----------
        state : OnOff
            Output state to set (ON or OFF)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"OUTP{channel} {state.value}")

    def get_output_impedance(self, channel: int = 1) -> float:
        """Get the output impedance.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Output impedance in ohms
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"OUTP{channel}:LOAD?"))

    def set_output_impedance(self, impedance: float, channel: int = 1) -> None:
        """Set the output impedance.

        Parameters
        ----------
        impedance : float
            Output impedance in ohms
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"OUTP{channel}:LOAD {self._format_float(impedance)}")

    def get_output_polarity(self, channel: int = 1) -> OutputPolarity:
        """Get the output polarity.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        OutputPolarity
            Output polarity (NORMAL or INVERTED)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return OutputPolarity(self.query(f"OUTP{channel}:POL?").strip())

    def set_output_polarity(self, polarity: OutputPolarity, channel: int = 1) -> None:
        """Set the output polarity.

        Parameters
        ----------
        polarity : OutputPolarity
            Output polarity (NORMAL or INVERTED)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"OUTP{channel}:POL {polarity.value}")

    def get_output_mode(self, channel: int = 1) -> OutputMode:
        """Get the output mode.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        OutputMode
            Output mode (NORMAL or GATED)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return OutputMode(self.query(f"OUTP{channel}:MODE?").strip())

    def set_output_mode(self, mode: OutputMode, channel: int = 1) -> None:
        """Set the output mode.

        Parameters
        ----------
        mode : OutputMode
            Output mode (NORMAL or GATED)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"OUTP{channel}:MODE {mode.value}")

    def get_sync_output(self) -> OnOff:
        """Get the sync output state.

        Returns
        -------
        OnOff
            Current sync output state (ON or OFF)
        """
        return OnOff(int(self.query("OUTP:SYNC?").strip()))

    def set_sync_output(self, state: OnOff) -> None:
        """Set the sync output state.

        Parameters
        ----------
        state : OnOff
            Sync output state to set (ON or OFF)
        """
        self.write(f"OUTP:SYNC {state.value}")

    def get_sync_mode(self, channel: int = 1) -> SyncMode:
        """Get the sync output mode.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        SyncMode
            Sync output mode (NORMAL, CARRIER, or MARKER)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return SyncMode(self.query(f"OUTP{channel}:SYNC:MODE?").strip())

    def set_sync_mode(self, mode: SyncMode, channel: int = 1) -> None:
        """Set the sync output mode.

        Parameters
        ----------
        mode : SyncMode
            Sync output mode (NORMAL, CARRIER, or MARKER)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"OUTP{channel}:SYNC:MODE {mode.value}")

    def get_sync_polarity(self, channel: int = 1) -> SyncPolarity:
        """Get the sync output polarity.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        SyncPolarity
            Sync output polarity (NORMAL or INVERTED)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return SyncPolarity(self.query(f"OUTP{channel}:SYNC:POL?").strip())

    def set_sync_polarity(self, polarity: SyncPolarity, channel: int = 1) -> None:
        """Set the sync output polarity.

        Parameters
        ----------
        polarity : SyncPolarity
            Sync output polarity (NORMAL or INVERTED)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"OUTP{channel}:SYNC:POL {polarity.value}")

    def get_sync_source(self) -> str:
        """Get the sync output source.

        Returns
        -------
        str
            Sync output source ("CH1" or "CH2")
        """
        return self.query("OUTP:SYNC:SOUR?").strip()

    def set_sync_source(self, source: str) -> None:
        """Set the sync output source.

        Parameters
        ----------
        source : str
            Sync output source ("CH1" or "CH2")
        """
        if source not in ["CH1", "CH2"]:
            raise ValueError("Source must be either 'CH1' or 'CH2'")
        self.write(f"OUTP:SYNC:SOUR {source}")

    def get_trigger_output(self) -> OnOff:
        """Get the trigger output state.

        Returns
        -------
        OnOff
            Current trigger output state (ON or OFF)
        """
        return OnOff(int(self.query("OUTP:TRIG?").strip()))

    def set_trigger_output(self, state: OnOff) -> None:
        """Set the trigger output state.

        Parameters
        ----------
        state : OnOff
            Trigger output state to set (ON or OFF)
        """
        self.write(f"OUTP:TRIG {state.value}")

    def get_trigger_output_slope(self) -> TriggerOutputSlope:
        """Get the trigger output slope.

        Returns
        -------
        TriggerOutputSlope
            Trigger output slope (POSITIVE or NEGATIVE)
        """
        return TriggerOutputSlope(self.query("OUTP:TRIG:SLOP?").strip())

    def set_trigger_output_slope(self, slope: TriggerOutputSlope) -> None:
        """Set the trigger output slope.

        Parameters
        ----------
        slope : TriggerOutputSlope
            Trigger output slope (POSITIVE or NEGATIVE)
        """
        self.write(f"OUTP:TRIG:SLOP {slope.value}")

    def get_trigger_output_source(self) -> str:
        """Get the trigger output source.

        Returns
        -------
        str
            Trigger output source ("CH1" or "CH2")
        """
        return self.query("OUTP:TRIG:SOUR?").strip()

    def set_trigger_output_source(self, source: str) -> None:
        """Set the trigger output source.

        Parameters
        ----------
        source : str
            Trigger output source ("CH1" or "CH2")
        """
        if source not in ["CH1", "CH2"]:
            raise ValueError("Source must be either 'CH1' or 'CH2'")
        self.write(f"OUTP:TRIG:SOUR {source}")

    @property
    def combined(self) -> bool:
        """Get the combined output state.

        Returns
        -------
        bool
            True if channels are combined, False otherwise
        """
        if not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return self.query("COMBine:FEED?") == "CH2"

    @combined.setter
    def combined(self, val: bool) -> None:
        """Set the combined output state.

        Parameters
        ----------
        val : bool
            True to combine channels (combines channel 2 into channel 1), False to separate
        """
        if not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"COMBine:FEED {'CH2' if val else 'NONE'}")

    def set_sweep_frequency(
        self, start_freq: float, stop_freq: float, channel: int = 1
    ) -> None:
        """Set sweep frequency range (convenience method).

        This is a convenience method that combines setting start and stop frequencies.
        For more control, use set_sweep_start_frequency() and set_sweep_stop_frequency().

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

        # Get max frequency based on model
        max_freq = (
            30e6 if self.model in ["33519B", "33520B", "33521B", "33522B"] else 20e6
        )

        # Validate frequency range (1 µHz to 20/30 MHz)
        if not (1e-6 <= start_freq <= max_freq) or not (1e-6 <= stop_freq <= max_freq):
            raise ValueError(f"Frequency must be between 1 µHz and {max_freq/1e6} MHz")

        self.set_sweep_start_frequency(start_freq, channel)
        self.set_sweep_stop_frequency(stop_freq, channel)

    def get_burst_state(self, channel: int = 1) -> OnOff:
        """Get the burst state.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        OnOff
            Current burst state (ON or OFF)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return OnOff(int(self.query(f"SOURce{channel}:BURS:STAT?").strip()))

    def set_burst_state(self, state: OnOff, channel: int = 1) -> None:
        """Set the burst state.

        Parameters
        ----------
        state : OnOff
            Burst state to set (ON or OFF)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:BURS:STAT {state.value}")

    def get_burst_internal_period(self, channel: int = 1) -> float:
        """Get the burst period for internally-triggered bursts.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Burst period in seconds (1 µs to 8000 s)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:BURS:INT:PER?"))

    def set_burst_internal_period(self, period: float, channel: int = 1) -> None:
        """Set the burst period for internally-triggered bursts.

        Parameters
        ----------
        period : float
            Burst period in seconds (1 µs to 8000 s)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        if not (1e-6 <= period <= 8000):
            raise ValueError("Burst period must be between 1 µs and 8000 s")
        self.write(f"SOURce{channel}:BURS:INT:PER {self._format_float(period)}")

    def get_burst_ncycles(self, channel: int = 1) -> Union[int, str]:
        """Get the number of cycles in burst mode.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        Union[int, str]
            Number of cycles or "INF" for infinite
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        response = self.query(f"SOURce{channel}:BURS:NCYC?").strip()
        if response.upper() == "INF":
            return "INF"
        return int(float(response))

    def set_burst_ncycles(self, ncycles: Union[int, str], channel: int = 1) -> None:
        """Set the number of cycles in burst mode.

        Parameters
        ----------
        ncycles : Union[int, str]
            Number of cycles (1 to 100,000,000) or "INF" for infinite
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        if isinstance(ncycles, str) and ncycles.upper() == "INF":
            self.write(f"SOURce{channel}:BURS:NCYC INF")
        else:
            if not (1 <= ncycles <= 100000000):
                raise ValueError("Number of cycles must be between 1 and 100,000,000")
            self.write(f"SOURce{channel}:BURS:NCYC {self._format_int(ncycles)}")

    def set_arbitrary_waveform(
        self,
        waveform_data: List[float],
        sample_rate: Optional[float] = None,
        channel: int = 1,
    ) -> None:
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

    def get_arbitrary_waveform(self, channel: int = 1) -> List[float]:
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

    def save_arbitrary_waveform(
        self,
        name: str,
        waveform_data: List[float],
        sample_rate: Optional[float] = None,
        channel: int = 1,
    ) -> None:
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

    def load_arbitrary_waveform(self, name: str, channel: int = 1) -> None:
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

    def get_available_waveforms(self, channel: int = 1) -> List[str]:
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

    def delete_arbitrary_waveform(self, name: str, channel: int = 1) -> None:
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

    def get_all_errors(self) -> List[Tuple[int, str]]:
        """Get all errors from the error queue.

        Returns
        -------
        list of tuples
            List of (error_code, error_message) tuples
        """
        errors = []
        while True:
            error = self.query("SYST:ERR?")
            if error.startswith("+0"):
                break
            # Parse error string into code and message
            try:
                code, message = error.split(",", 1)
                errors.append((int(code), message.strip('"')))
            except ValueError:
                errors.append((0, error.strip()))
        return errors

    def apply_sine(
        self, frequency: float, amplitude: float, offset: float = 0, channel: int = 1
    ) -> None:
        """Configure and output a sine wave.

        Parameters
        ----------
        frequency : float
            Frequency in Hz
        amplitude : float
            Amplitude in Vpp (or other units as specified by VOLTage:UNIT)
        offset : float, optional
            DC offset voltage (default 0)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:APPLy:SINusoid {frequency},{amplitude},{offset}")

    def apply_square(
        self, frequency: float, amplitude: float, offset: float = 0, channel: int = 1
    ) -> None:
        """Configure and output a square wave.

        Parameters
        ----------
        frequency : float
            Frequency in Hz
        amplitude : float
            Amplitude in Vpp (or other units as specified by VOLTage:UNIT)
        offset : float, optional
            DC offset voltage (default 0)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:APPLy:SQUare {frequency},{amplitude},{offset}")

    def apply_triangle(
        self, frequency: float, amplitude: float, offset: float = 0, channel: int = 1
    ) -> None:
        """Configure and output a triangle wave.

        Parameters
        ----------
        frequency : float
            Frequency in Hz
        amplitude : float
            Amplitude in Vpp (or other units as specified by VOLTage:UNIT)
        offset : float, optional
            DC offset voltage (default 0)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:APPLy:TRIangle {frequency},{amplitude},{offset}")

    def apply_ramp(
        self, frequency: float, amplitude: float, offset: float = 0, channel: int = 1
    ) -> None:
        """Configure and output a ramp wave.

        Parameters
        ----------
        frequency : float
            Frequency in Hz
        amplitude : float
            Amplitude in Vpp (or other units as specified by VOLTage:UNIT)
        offset : float, optional
            DC offset voltage (default 0)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:APPLy:RAMP {frequency},{amplitude},{offset}")

    def apply_pulse(
        self, frequency: float, amplitude: float, offset: float = 0, channel: int = 1
    ) -> None:
        """Configure and output a pulse wave.

        Parameters
        ----------
        frequency : float
            Frequency in Hz
        amplitude : float
            Amplitude in Vpp (or other units as specified by VOLTage:UNIT)
        offset : float, optional
            DC offset voltage (default 0)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:APPLy:PULSe {frequency},{amplitude},{offset}")

    def apply_noise(
        self, amplitude: float, offset: float = 0, channel: int = 1
    ) -> None:
        """Configure and output gaussian noise.

        Parameters
        ----------
        amplitude : float
            Amplitude in Vpp (or other units as specified by VOLTage:UNIT)
        offset : float, optional
            DC offset voltage (default 0)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:APPLy:NOISe DEF,{amplitude},{offset}")

    def apply_prbs(
        self, frequency: float, amplitude: float, offset: float = 0, channel: int = 1
    ) -> None:
        """Configure and output a pseudo-random binary sequence.

        Parameters
        ----------
        frequency : float
            Bit rate in bits/s
        amplitude : float
            Amplitude in Vpp (or other units as specified by VOLTage:UNIT)
        offset : float, optional
            DC offset voltage (default 0)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:APPLy:PRBS {frequency},{amplitude},{offset}")

    def apply_dc(self, offset: float, channel: int = 1) -> None:
        """Configure and output a DC voltage.

        Parameters
        ----------
        offset : float
            DC offset voltage
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:APPLy:DC DEF,DEF,{offset}")

    def apply_arbitrary(
        self, sample_rate: float, amplitude: float, offset: float = 0, channel: int = 1
    ) -> None:
        """Configure and output an arbitrary waveform.

        Parameters
        ----------
        sample_rate : float
            Sample rate in Sa/s (1 Sa/s to 250 MSa/s)
        amplitude : float
            Amplitude in Vpp (or other units as specified by VOLTage:UNIT)
        offset : float, optional
            DC offset voltage (default 0)
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        if not self._check_arbitrary_capability():
            raise ValueError(
                "Arbitrary waveform capability not available on this model"
            )
        self.write(
            f"SOURce{channel}:APPLy:ARBitrary {sample_rate},{amplitude},{offset}"
        )

    def get_sweep_start_frequency(self, channel: int = 1) -> float:
        """Get the sweep start frequency.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Start frequency in Hz
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:FREQ:STAR?"))

    def set_sweep_start_frequency(self, frequency: float, channel: int = 1) -> None:
        """Set the sweep start frequency.

        Parameters
        ----------
        frequency : float
            Start frequency in Hz
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FREQ:STAR {self._format_float(frequency)}")

    def get_sweep_stop_frequency(self, channel: int = 1) -> float:
        """Get the sweep stop frequency.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Stop frequency in Hz
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:FREQ:STOP?"))

    def set_sweep_stop_frequency(self, frequency: float, channel: int = 1) -> None:
        """Set the sweep stop frequency.

        Parameters
        ----------
        frequency : float
            Stop frequency in Hz
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FREQ:STOP {self._format_float(frequency)}")

    def get_sweep_center_frequency(self, channel: int = 1) -> float:
        """Get the sweep center frequency.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Center frequency in Hz
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:FREQ:CENT?"))

    def set_sweep_center_frequency(self, frequency: float, channel: int = 1) -> None:
        """Set the sweep center frequency.

        Parameters
        ----------
        frequency : float
            Center frequency in Hz
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FREQ:CENT {self._format_float(frequency)}")

    def get_sweep_span_frequency(self, channel: int = 1) -> float:
        """Get the sweep frequency span.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Frequency span in Hz
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:FREQ:SPAN?"))

    def set_sweep_span_frequency(self, span: float, channel: int = 1) -> None:
        """Set the sweep frequency span.

        Parameters
        ----------
        span : float
            Frequency span in Hz
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:FREQ:SPAN {self._format_float(span)}")

    def get_sweep_hold_time(self, channel: int = 1) -> float:
        """Get the sweep hold time.

        Parameters
        ----------
        channel : int, optional
            Channel number (1 or 2)

        Returns
        -------
        float
            Hold time in seconds
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        return float(self.query(f"SOURce{channel}:SWE:HTIM?"))

    def set_sweep_hold_time(self, time: float, channel: int = 1) -> None:
        """Set the sweep hold time.

        Parameters
        ----------
        time : float
            Hold time in seconds
        channel : int, optional
            Channel number (1 or 2)
        """
        if channel == 2 and not self._check_dual_channel():
            raise ValueError("Dual channel operation not available on this model")
        self.write(f"SOURce{channel}:SWE:HTIM {self._format_float(time)}")

    def get_angle_unit(self) -> AngleUnit:
        """Get the current angle unit setting.

        Returns
        -------
        AngleUnit
            Current angle unit (DEGREES or RADIANS)
        """
        return AngleUnit(self.query("UNIT:ANGLe?").strip())

    def set_angle_unit(self, unit: AngleUnit) -> None:
        """Set the angle unit.

        Parameters
        ----------
        unit : AngleUnit
            Angle unit to set (DEGREES or RADIANS)
        """
        self.write(f"UNIT:ANGLe {unit.value}")
