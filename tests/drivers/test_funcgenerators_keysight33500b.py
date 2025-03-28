"""Test script for Keysight33500B waveform generator driver.

This script provides comprehensive testing of the Keysight33500B waveform generator driver.
It tests all major functionality including basic waveform settings, burst mode, sweep mode,
trigger settings, output settings, and various additional features.

Important Notes:
---------------
1. This is NOT a unit test suite using a testing framework (like pytest). It is a manual
   integration test script that requires a physical device to be connected.

2. A Keysight 33500B Series Waveform Generator must be connected to the system and
   accessible via VISA. The default VISA address is:
   "USB0::0x0957::0x2807::MY58000523::INSTR"
   Modify the address in the main() function if your device has a different address.

3. The script performs actual hardware operations and will modify the device's settings.
   Make sure no other applications are controlling the device while running this script.

4. The script includes appropriate delays between operations to allow the device to
   process commands. These delays may need to be adjusted based on your specific device
   and system performance.

Test Coverage:
-------------
The script tests the following functionality:

1. Basic Waveform Settings:
   - Frequency, voltage, and offset
   - Function shape selection
   - Phase control
   - Angle unit settings

2. Burst Mode:
   - Burst mode selection
   - Number of cycles
   - Internal period
   - Burst phase
   - Gate polarity
   - Error handling for invalid values

3. Sweep Mode:
   - Sweep time and spacing
   - Frequency range settings
   - Return and hold times
   - Error handling for invalid values

4. Trigger Settings:
   - Trigger source and slope
   - Trigger delay and count
   - Trigger output settings

5. Output Settings:
   - Output state control
   - Output impedance
   - Output polarity
   - Output mode

6. Additional Settings:
   - Ramp symmetry
   - AM DSSC mode
   - Sync settings
   - Various apply methods
   - Combined output (for dual-channel models)

7. Error Handling:
   - Error queue management
   - Invalid value detection
   - Device-specific feature checking

Usage:
------
1. Connect your Keysight 33500B Series Waveform Generator
2. Modify the VISA address in main() if needed
3. Run the script: python test_funcgenerators_keysight33500b.py

The script will:
- Run each test suite in sequence
- Reset the device between tests
- Print detailed information about each operation
- Handle and report any errors
- Clean up and close the connection properly

Error Handling:
--------------
The script includes comprehensive error handling:
- Catches and reports device errors
- Validates input parameters
- Checks for device-specific capabilities
- Provides detailed error messages
- Ensures proper cleanup in case of failures

Dependencies:
------------
- instrumental (for the Keysight33500B driver)
- time (for operation delays)
- typing (for type hints)
"""

import time
from typing import NoReturn
from instrumental.drivers.funcgenerators.keysight33500b import (
    Keysight33500B,
    WaveformShape,
    BurstMode,
    SweepSpacing,
    SweepMode,
    SweepDirection,
    ModulationType,
    TriggerSource,
    TriggerSlope,
    BurstGatePolarity,
    OutputMode,
    SyncMode,
    SyncPolarity,
    TriggerOutputSlope,
    OutputPolarity,
    OnOff,
    AngleUnit,
)
import pytest

def test_basic_waveform_settings(generator: Keysight33500B) -> None:
    """Test basic waveform settings."""
    print("\nTesting basic waveform settings...")

    # First set up basic waveform parameters
    print("Setting up basic waveform parameters...")
    generator.set_frequency(1000.0)  # 1 kHz
    generator.set_voltage(1.0)  # 1 Vpp
    generator.set_function_shape(WaveformShape.SIN)  # Sine wave

    # Set angle unit to degrees
    print("Setting angle unit to degrees...")
    generator.set_angle_unit(AngleUnit.DEGREES)

    # Test phase
    test_phase = 45.0
    print(f"Setting phase to {test_phase} degrees")
    generator.set_phase(test_phase)
    time.sleep(0.1)  # Give the instrument time to apply the setting
    actual_phase = generator.get_phase()
    print(f"Actual phase: {actual_phase} degrees")
    assert abs(actual_phase - test_phase) < 0.1

    # Test voltage settings
    test_voltage = 1.0
    print(f"Setting voltage to {test_voltage} V")
    generator.set_voltage(test_voltage)
    actual_voltage = generator.get_voltage()
    print(f"Actual voltage: {actual_voltage} V")
    assert abs(actual_voltage - test_voltage) < 0.01

    # Test voltage offset
    test_offset = 0.5
    print(f"Setting voltage offset to {test_offset} V")
    generator.set_voltage_offset(test_offset)
    actual_offset = generator.get_voltage_offset()
    print(f"Actual offset: {actual_offset} V")
    assert abs(actual_offset - test_offset) < 0.01

    # Test function shape
    test_shape = WaveformShape.SIN
    print(f"Setting function shape to {test_shape.value}")
    generator.set_function_shape(test_shape)
    actual_shape = generator.get_function_shape()
    print(f"Actual shape: {actual_shape.value}")
    assert actual_shape == test_shape

def main() -> NoReturn:
    """Main test function."""
    # Create generator instance
    generator = Keysight33500B(visa_address="USB0::0x0957::0x2807::MY58000523::INSTR")

    try:
        # Run all tests with resets between each
        print("\nRunning basic waveform settings test...")
        test_basic_waveform_settings(generator)
        reset_instrument(generator)

        print("\nRunning burst settings test...")
        test_burst_settings(generator)
        reset_instrument(generator)

        print("\nRunning modulation settings test...")
        test_modulation_settings(generator)
        reset_instrument(generator)

        print("\nRunning sweep settings test...")
        test_sweep_settings(generator)
        reset_instrument(generator)

        print("\nRunning trigger settings test...")
        test_trigger_settings(generator)
        reset_instrument(generator)

        print("\nRunning output settings test...")
        test_output_settings(generator)
        reset_instrument(generator)

        print("\nRunning additional settings test...")
        test_additional_settings(generator)
        reset_instrument(generator)

        print("\nRunning abort test...")
        test_abort(generator)
        reset_instrument(generator)

        print("\nAll tests completed successfully!")

    except Exception as e:
        print(f"\nError during testing: {str(e)}")
        print("\nDevice errors:")
        for code, message in generator.get_all_errors():
            print(f"Error {code}: {message}")
        raise

    finally:
        print("\nDevice errors:")
        for code, message in generator.get_all_errors():
            print(f"Error {code}: {message}")
        # Reset instrument to default settings
        reset_instrument(generator)

        # Close connection
        generator.close()


if __name__ == "__main__":
    main() 