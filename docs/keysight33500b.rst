Keysight 33500B Series Waveform Generator
=======================================

.. contents::
    :local:
    :depth: 2

Overview
--------

The Keysight33500B driver provides a comprehensive interface to the Keysight 33500B Series Waveform Generator. This driver supports all major functionality of the instrument, including basic waveform generation, burst mode, sweep mode, modulation, and various output settings.

Features
~~~~~~~~

- Basic waveform settings (frequency, voltage, offset, shape, phase)
- Burst mode with configurable cycles, internal period, and gate settings
- Sweep mode with linear/logarithmic spacing and configurable timing
- AM/FM modulation capabilities
- Trigger settings for external control
- Output settings including impedance, polarity, and mode
- Dual-channel support (for applicable models)
- Comprehensive error handling and status reporting

Installation
-----------

Requirements
~~~~~~~~~~~

1. A Keysight 33500B Series Waveform Generator
2. VISA interface (USB, GPIB, or LAN)
3. PyVISA package installed
4. NI-VISA or Keysight IO Libraries Suite installed

Setup
~~~~~

1. Install the required Python packages:
   ::

       pip install pyvisa pyvisa-py

2. Install either NI-VISA or Keysight IO Libraries Suite for your operating system
3. Connect your waveform generator via USB, GPIB, or LAN
4. Verify the connection using the VISA address (default: "USB0::0x0957::0x2807::MY58000523::INSTR")

Basic Usage
----------

Here's a simple example of how to use the waveform generator:

::

    from instrumental.drivers.funcgenerators.keysight33500b import Keysight33500B

    # Create generator instance
    generator = Keysight33500B(visa_address="USB0::0x0957::0x2807::MY58000523::INSTR")

    # Set up basic waveform
    generator.set_frequency(1000.0)  # 1 kHz
    generator.set_voltage(1.0)       # 1 Vpp
    generator.set_function_shape(WaveformShape.SIN)  # Sine wave
    generator.set_output_state(OnOff.ON)

    # Clean up
    generator.close()

Advanced Features
---------------

Burst Mode
~~~~~~~~~

The burst mode allows you to generate a specific number of waveform cycles:

::

    # Set up burst mode
    generator.set_burst_mode(BurstMode.TRIGGERED)
    generator.set_burst_cycles(5)  # 5 cycles per burst
    generator.set_burst_internal_period(0.01)  # 10 ms between bursts

Sweep Mode
~~~~~~~~~

Configure frequency sweeps with various parameters:

::

    # Set up sweep mode
    generator.set_sweep_mode(SweepMode.LINEAR)
    generator.set_sweep_start_frequency(100.0)  # 100 Hz
    generator.set_sweep_stop_frequency(1000.0)  # 1 kHz
    generator.set_sweep_time(1.0)  # 1 second sweep time
    generator.set_sweep_return_time(0.1)  # 100 ms return time

Modulation
~~~~~~~~~

Set up amplitude or frequency modulation:

::

    # Set up AM modulation
    generator.set_modulation_type(ModulationType.AM)
    generator.set_modulation_depth(50.0)  # 50% depth
    generator.set_modulation_frequency(100.0)  # 100 Hz modulation

Dual Channel Operation
~~~~~~~~~~~~~~~~~~~~

For dual-channel models, you can control both channels and use combined output:

::

    if generator.supports_dual_channel:
        # Configure both channels
        generator.set_frequency(1000.0, channel=1)
        generator.set_frequency(2000.0, channel=2)
        
        # Enable combined output
        generator.set_combined_output(OnOff.ON)

Error Handling
-------------

The driver includes comprehensive error handling:

::

    try:
        generator.set_frequency(1000.0)
    except Exception as e:
        print(f"Error: {str(e)}")
        print("\nDevice errors:")
        for code, message in generator.get_all_errors():
            print(f"Error {code}: {message}")

Module Reference
--------------

.. automodule:: instrumental.drivers.funcgenerators.keysight33500b
    :members:
    :undoc-members:

Changelog
--------

Unreleased
~~~~~~~~~

- Initial driver release
- Comprehensive test suite implementation
- Full support for all major instrument features
- Dual-channel support for applicable models 