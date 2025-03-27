#!/usr/bin/env python
"""Interactive test script for Keysight 33500B Series Waveform Generator."""

from instrumental.drivers.funcgenerators.agilent import Keysight33500B
from instrumental import list_instruments, u  # Import the units module
import numpy as np
import time
import sys
from instrumental.log import log_to_screen

def print_generator_info(generator):
    """Print basic information about the function generator.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to get information from.
    """
    print("\nGenerator Information:")
    print(f"Model: {generator.model}")
    print_errors(generator, "Getting model information")
    
    print(f"System Date: {generator.get_system_date()}")
    print_errors(generator, "Getting system date")
    
    print(f"System Time: {generator.get_system_time()}")
    print_errors(generator, "Getting system time")
    
    print(f"Channel 1:")
    print(f"  Frequency: {generator.frequency1}")
    print_errors(generator, "Getting frequency on channel 1")
    
    print(f"  Voltage: {generator.voltage1}")
    print_errors(generator, "Getting voltage on channel 1")
    
    print(f"  Voltage Offset: {generator.voltage_offset1}")
    print_errors(generator, "Getting voltage offset on channel 1")
    
    print(f"  Function: {generator.function1}")
    print_errors(generator, "Getting function on channel 1")
    
    print(f"  Function Shape: {generator.function_shape1}")
    print_errors(generator, "Getting function shape on channel 1")
    
    print(f"  Polarity: {generator.get_polarity(1)}")
    print_errors(generator, "Getting polarity on channel 1")
    
    print(f"  Output Impedance: {generator.output_impedance1}")
    print_errors(generator, "Getting output impedance on channel 1")
    
    print(f"  Output State: {'ON' if generator.output1 else 'OFF'}")
    print_errors(generator, "Getting output state on channel 1")
    
    if generator._check_dual_channel():
        print(f"\nChannel 2:")
        print(f"  Frequency: {generator.frequency2}")
        print_errors(generator, "Getting frequency on channel 2")
        
        print(f"  Voltage: {generator.voltage2}")
        print_errors(generator, "Getting voltage on channel 2")
        
        print(f"  Voltage Offset: {generator.voltage_offset2}")
        print_errors(generator, "Getting voltage offset on channel 2")
        
        print(f"  Function: {generator.function2}")
        print_errors(generator, "Getting function on channel 2")
        
        print(f"  Function Shape: {generator.function_shape2}")
        print_errors(generator, "Getting function shape on channel 2")
        
        print(f"  Polarity: {generator.get_polarity(2)}")
        print_errors(generator, "Getting polarity on channel 2")
        
        print(f"  Output Impedance: {generator.output_impedance2}")
        print_errors(generator, "Getting output impedance on channel 2")
        
        print(f"  Output State: {'ON' if generator.output2 else 'OFF'}")
        print_errors(generator, "Getting output state on channel 2")
        
        print(f"  Combined Output: {'ON' if generator.combined else 'OFF'}")
        print_errors(generator, "Getting combined output state")

def print_errors(generator, context=None):
    """Print all errors from the generator's error queue.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to get errors from.
    context : str, optional
        Description of the command or step being executed when the error occurred.
    """
    errors = generator.get_all_errors()
    if errors:
        print("\nGenerator Errors:")
        if context:
            print(f"Context: {context}")
        for code, message in errors:
            print(f"Error {code}: {message}")
    else:
        print("\nNo errors in queue")

def test_basic_parameters(generator):
    """Test basic waveform parameters.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to test.
    """
    print("\nTesting basic waveform parameters...")
    
    # Test frequency
    test_freq = 1.0 * u.kHz
    print(f"Setting frequency to {test_freq} on channel 1")
    generator.frequency1 = test_freq
    print_errors(generator, "Setting frequency on channel 1")
    
    # Test voltage
    test_voltage = 1.0 * u.V
    print(f"Setting voltage to {test_voltage} on channel 1")
    generator.voltage1 = test_voltage
    print_errors(generator, "Setting voltage on channel 1")
    
    # Test voltage offset
    test_offset = 0.5 * u.V
    print(f"Setting voltage offset to {test_offset} on channel 1")
    generator.voltage_offset1 = test_offset
    print_errors(generator, "Setting voltage offset on channel 1")
    
    # Test function selection
    test_function = "SIN"
    print(f"Setting function to {test_function} on channel 1")
    generator.function1 = test_function
    print_errors(generator, "Setting function on channel 1")
    
    # Test function shape
    test_shape = "SIN"
    print(f"Setting function shape to {test_shape} on channel 1")
    generator.function_shape1 = test_shape
    print_errors(generator, "Setting function shape on channel 1")
    
    input("\nPress Enter to continue to next test phase...")

def test_trigger_settings(generator):
    """Test trigger settings.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to test.
    """
    print("\nTesting trigger settings...")
    
    # Test trigger source
    test_source = "IMM"
    print(f"Setting trigger source to {test_source}")
    generator.set_trigger_source(test_source)
    print(f"Current trigger source: {generator.get_trigger_source()}")
    print_errors(generator, "Setting trigger source")
    
    # Test trigger slope
    test_slope = "POS"
    print(f"Setting trigger slope to {test_slope}")
    generator.set_trigger_slope(test_slope)
    print(f"Current trigger slope: {generator.get_trigger_slope()}")
    print_errors(generator, "Setting trigger slope")
    
    # Test trigger level
    test_level = 1.0
    print(f"Setting trigger level to {test_level}V")
    generator.trigger_level = test_level
    print(f"Current trigger level: {generator.trigger_level}V")
    print_errors(generator, "Setting trigger level")
    
    input("\nPress Enter to continue to next test phase...")

def test_output_settings(generator):
    """Test output settings.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to test.
    """
    print("\nTesting output settings...")
    
    # Test polarity
    test_polarity = "NORM"
    print(f"Setting polarity to {test_polarity} on channel 1")
    generator.set_polarity(test_polarity, 1)
    print(f"Current polarity: {generator.get_polarity(1)}")
    print_errors(generator, "Setting polarity on channel 1")
    
    # Test output impedance
    test_imp = 50.0
    print(f"Setting output impedance to {test_imp} ohms on channel 1")
    generator.output_impedance1 = test_imp
    print(f"Current output impedance: {generator.output_impedance1} ohms")
    print_errors(generator, "Setting output impedance on channel 1")
    
    # Test output state
    print("Testing output state on channel 1")
    generator.output1 = True
    print(f"Output 1 state: {'ON' if generator.output1 else 'OFF'}")
    time.sleep(1)  # Wait a second
    generator.output1 = False
    print(f"Output 1 state: {'ON' if generator.output1 else 'OFF'}")
    print_errors(generator, "Testing output state on channel 1")
    
    if generator._check_dual_channel():
        # Test channel 2 output settings
        print("\nTesting channel 2 output settings...")
        test_polarity2 = "INV"
        print(f"Setting polarity to {test_polarity2} on channel 2")
        generator.set_polarity(test_polarity2, 2)
        print(f"Current polarity: {generator.get_polarity(2)}")
        print_errors(generator, "Setting polarity on channel 2")
        
        test_imp2 = 75.0
        print(f"Setting output impedance to {test_imp2} ohms on channel 2")
        generator.output_impedance2 = test_imp2
        print(f"Current output impedance: {generator.output_impedance2} ohms")
        print_errors(generator, "Setting output impedance on channel 2")
        
        print("Testing output state on channel 2")
        generator.output2 = True
        print(f"Output 2 state: {'ON' if generator.output2 else 'OFF'}")
        time.sleep(1)  # Wait a second
        generator.output2 = False
        print(f"Output 2 state: {'ON' if generator.output2 else 'OFF'}")
        print_errors(generator, "Testing output state on channel 2")
        
        # Test combined output
        print("\nTesting combined output...")
        print("Combining channel 2 into channel 1...")
        generator.write("COMBine:FEED CH2")
        print(f"Combined output state: {generator.query('COMBine:FEED?')}")
        print_errors(generator, "Combining channel 2 into channel 1")
        time.sleep(1)  # Wait a second
        print("Disabling combined output...")
        generator.write("COMBine:FEED NONE")
        print(f"Combined output state: {generator.query('COMBine:FEED?')}")
        print_errors(generator, "Disabling combined output")
    
    input("\nPress Enter to continue to next test phase...")

def test_pulse_settings(generator):
    """Test pulse settings.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to test.
    """
    print("\nTesting pulse settings...")
    
    # Set function to pulse
    print("Setting function to pulse on channel 1")
    generator.function1 = "PULS"
    print_errors(generator, "Setting function to pulse on channel 1")
    
    # Test pulse width
    test_width = 1e-6  # 1 microsecond
    print(f"Setting pulse width to {test_width}s on channel 1")
    generator.set_width(test_width, 1)
    print_errors(generator, "Setting pulse width on channel 1")
    
    # Test delay
    test_delay = 1e-6  # 1 microsecond
    print(f"Setting delay to {test_delay}s on channel 1")
    generator.set_delay(test_delay, 1)
    print_errors(generator, "Setting delay on channel 1")
    
    # Test high/low voltage levels
    test_high = 2.0
    test_low = 0.0
    print(f"Setting high voltage to {test_high}V on channel 1")
    generator.set_high(test_high, 1)
    print(f"Setting low voltage to {test_low}V on channel 1")
    generator.set_low(test_low, 1)
    print_errors(generator, "Setting high/low voltage levels on channel 1")
    
    input("\nPress Enter to continue to next test phase...")

def test_error_handling(generator):
    """Test error handling.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to test.
    """
    print("\nTesting error handling...")
    
    # Test invalid polarity
    print("Testing invalid polarity...")
    try:
        generator.set_polarity("INVALID", 1)
    except ValueError as e:
        print(f"Expected error: {e}")
    print_errors(generator, "Testing invalid polarity")
    
    # Test invalid trigger source
    print("Testing invalid trigger source...")
    try:
        generator.set_trigger_source("INVALID")
    except ValueError as e:
        print(f"Expected error: {e}")
    print_errors(generator, "Testing invalid trigger source")
    
    # Test invalid trigger slope
    print("Testing invalid trigger slope...")
    try:
        generator.set_trigger_slope("INVALID")
    except ValueError as e:
        print(f"Expected error: {e}")
    print_errors(generator, "Testing invalid trigger slope")
    
    # Test invalid channel
    if generator._check_dual_channel():
        print("Testing invalid channel...")
        try:
            generator.set_polarity("NORM", 3)
        except ValueError as e:
            print(f"Expected error: {e}")
        print_errors(generator, "Testing invalid channel")
    
    # Test invalid impedance
    print("Testing invalid impedance...")
    try:
        generator.output_impedance1 = -1.0
    except ValueError as e:
        print(f"Expected error: {e}")
    print_errors(generator, "Testing invalid impedance")
    
    # Test invalid pulse width
    print("Testing invalid pulse width...")
    try:
        generator.set_width(-1.0, 1)
    except ValueError as e:
        print(f"Expected error: {e}")
    print_errors(generator, "Testing invalid pulse width")
    
    # Test invalid delay
    print("Testing invalid delay...")
    try:
        generator.set_delay(-1.0, 1)
    except ValueError as e:
        print(f"Expected error: {e}")
    print_errors(generator, "Testing invalid delay")
    
    input("\nPress Enter to continue to next test phase...")

def main():
    """Run the interactive test suite for the Keysight 33500B generator."""
    # Enable logging to see what's happening during device discovery
    log_to_screen()
    
    print("Searching for Keysight 33500B generators...")
    try:
        # Connect directly to the generator
        visa_address = 'USB0::0x0957::0x2807::MY58000523::INSTR'
        print(f"Connecting to {visa_address}...")
        
        # Connect to the generator
        generator = Keysight33500B(visa_address=visa_address)
        
        try:
            # Print generator information
            print_generator_info(generator)
            print_errors(generator, "Initial connection and information retrieval")  # Check for any initial errors
            
            # Run all test suites
            test_basic_parameters(generator)
            test_trigger_settings(generator)
            test_output_settings(generator)
            test_pulse_settings(generator)
            
            # Test burst mode
            print("\nTesting burst mode...")
            print("Setting burst mode parameters on channel 1...")
            generator.burst_mode1 = "GAT"
            generator.burst_ncycles1 = 5
            generator.burst_phase1 = 0.0
            print_errors(generator, "Setting burst mode parameters on channel 1")
            
            # Test modulation
            print("\nTesting modulation...")
            print("Setting modulation parameters on channel 1...")
            generator.modulation_state1 = True
            generator.modulation_type1 = "AM"
            generator.modulation_depth1 = 50.0
            generator.modulation_rate1 = 1.0 * u.kHz
            print_errors(generator, "Setting modulation parameters on channel 1")
            
            # Test sweep
            print("\nTesting sweep...")
            print("Setting sweep parameters on channel 1...")
            generator.sweep_state1 = True
            generator.sweep_time1 = 1.0 * u.s
            generator.sweep_spacing1 = "LIN"
            print_errors(generator, "Setting sweep parameters on channel 1")
            
            # Test arbitrary waveform (if supported)
            if generator._check_arbitrary_capability():
                print("\nTesting arbitrary waveform...")
                # Create a simple sine wave
                t = np.linspace(0, 2*np.pi, 1000)
                waveform = np.sin(t)
                print("Loading arbitrary waveform on channel 1...")
                generator.set_arbitrary_waveform(waveform, sample_rate=1000, channel=1)
                print_errors(generator, "Loading arbitrary waveform on channel 1")
                
                # Test saving and loading arbitrary waveform
                print("Saving arbitrary waveform...")
                generator.save_arbitrary_waveform("TEST_WAVE", waveform, channel=1)
                print_errors(generator, "Saving arbitrary waveform to memory")
                
                print("Loading arbitrary waveform...")
                generator.load_arbitrary_waveform("TEST_WAVE", channel=1)
                print_errors(generator, "Loading arbitrary waveform from memory")
                
                print("Getting available waveforms...")
                waveforms = generator.get_available_waveforms(channel=1)
                print(f"Available waveforms: {waveforms}")
                print_errors(generator, "Retrieving list of available waveforms")
                
                print("Deleting test waveform...")
                generator.delete_arbitrary_waveform("TEST_WAVE", channel=1)
                print_errors(generator, "Deleting test waveform from memory")
            
            # Test dual channel features (if supported)
            if generator._check_dual_channel():
                print("\nTesting dual channel features...")
                
                # Test channel 2 basic parameters
                print("\nTesting channel 2 basic parameters...")
                test_freq2 = 2.0 * u.kHz
                print(f"Setting frequency to {test_freq2} on channel 2")
                generator.frequency2 = test_freq2
                print_errors(generator, "Setting frequency on channel 2")
                
                test_voltage2 = 2.0 * u.V
                print(f"Setting voltage to {test_voltage2} on channel 2")
                generator.voltage2 = test_voltage2
                print_errors(generator, "Setting voltage on channel 2")
                
                # Test channel 2 burst mode
                print("\nTesting channel 2 burst mode...")
                generator.burst_mode2 = "GAT"
                generator.burst_ncycles2 = 5
                generator.burst_phase2 = 0.0
                print_errors(generator, "Setting burst mode parameters on channel 2")
                
                # Test channel 2 modulation
                print("\nTesting channel 2 modulation...")
                generator.modulation_state2 = True
                generator.modulation_type2 = "AM"
                generator.modulation_depth2 = 50.0
                generator.modulation_rate2 = 1.0 * u.kHz
                print_errors(generator, "Setting modulation parameters on channel 2")
                
                # Test channel 2 sweep
                print("\nTesting channel 2 sweep...")
                generator.sweep_state2 = True
                generator.sweep_time2 = 1.0 * u.s
                generator.sweep_spacing2 = "LIN"
                print_errors(generator, "Setting sweep parameters on channel 2")
                
                # Test phase control
                test_phase = 90.0
                print(f"Setting phase to {test_phase} degrees on channel 2")
                generator.set_phase(test_phase, channel=2)
                print_errors(generator, "Setting phase on channel 2")
                
                # Test duty cycle
                test_duty = 50.0
                print(f"Setting duty cycle to {test_duty}% on channel 2")
                generator.set_duty_cycle(test_duty, channel=2)
                print_errors(generator, "Setting duty cycle on channel 2")
                
                # Test ramp symmetry
                test_symmetry = 50.0
                print(f"Setting ramp symmetry to {test_symmetry}% on channel 2")
                generator.set_ramp_symmetry(test_symmetry, channel=2)
                print_errors(generator, "Setting ramp symmetry on channel 2")
            
            # Test error handling
            test_error_handling(generator)
                
        finally:
            # Cleanup
            print_errors(generator, "Final cleanup before closing")
            print("\nCleaning up...")
            generator.close()
            print("Generator closed successfully")
            
    except Exception as e:
        print(f"Connection failed: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure the device is properly connected via USB")
        print("2. Check if the device is recognized by your system")
        print("3. Try unplugging and replugging the device")
        print("4. Check if you have the necessary VISA drivers installed")
        print("5. Try running the script with administrator privileges")
        sys.exit(1)

if __name__ == "__main__":
    main() 