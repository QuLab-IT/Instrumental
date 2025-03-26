#!/usr/bin/env python
"""Interactive test script for Keysight 33500B Series Waveform Generator."""

from instrumental.drivers.funcgenerators.agilent import Keysight33500B
from instrumental import list_instruments, u  # Import the units module
import numpy as np
import time

def print_generator_info(generator):
    """Print basic information about the function generator.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to get information from.
    """
    print("\nGenerator Information:")
    print(f"Model: {generator.model}")
    print(f"Channel 1:")
    print(f"  Frequency: {generator.frequency1}")
    print(f"  Voltage: {generator.voltage1}")
    print(f"  Voltage Offset: {generator.voltage_offset1}")
    print(f"  Function: {generator.function1}")
    print(f"  Function Shape: {generator.function_shape1}")
    
    if generator._check_dual_channel():
        print(f"\nChannel 2:")
        print(f"  Frequency: {generator.frequency2}")
        print(f"  Voltage: {generator.voltage2}")
        print(f"  Voltage Offset: {generator.voltage_offset2}")
        print(f"  Function: {generator.function2}")
        print(f"  Function Shape: {generator.function_shape2}")

def print_errors(generator):
    """Print all errors from the generator's error queue.
    
    Parameters
    ----------
    generator : Keysight33500B
        The generator instance to get errors from.
    """
    errors = generator.get_all_errors()
    if errors:
        print("\nGenerator Errors:")
        for code, message in errors:
            print(f"Error {code}: {message}")
    else:
        print("\nNo errors in queue")

def main():
    """Run the interactive test suite for the Keysight 33500B generator."""
    print("Searching for Keysight 33500B generators...")
    generators = list_instruments()
    
    if not generators:
        print("No Keysight 33500B generators found")
        return
        
    print(f"\nFound {len(generators)} Keysight 33500B generator(s):")
    for i, generator in enumerate(generators, 1):
        print(f"\nGenerator {i}:")
        print(f"  VISA Address: {generator['visa_address']}")
    
    # Connect to the first available generator
    print("\nConnecting to the first available generator...")
    generator = Keysight33500B(visa_address=generators[0]['visa_address'])
    
    try:
        # Print generator information
        print_generator_info(generator)
        print_errors(generator)  # Check for any initial errors
        
        # Test basic waveform parameters
        print("\nTesting basic waveform parameters...")
        
        # Test frequency
        test_freq = 1.0 * u.kHz
        print(f"Setting frequency to {test_freq} on channel 1")
        generator.frequency1 = test_freq
        print_errors(generator)
        
        # Test voltage
        test_voltage = 1.0 * u.V
        print(f"Setting voltage to {test_voltage} on channel 1")
        generator.voltage1 = test_voltage
        print_errors(generator)
        
        # Test voltage offset
        test_offset = 0.5 * u.V
        print(f"Setting voltage offset to {test_offset} on channel 1")
        generator.voltage_offset1 = test_offset
        print_errors(generator)
        
        # Test function selection
        test_function = "SIN"
        print(f"Setting function to {test_function} on channel 1")
        generator.function1 = test_function
        print_errors(generator)
        
        # Test function shape
        test_shape = "SIN"
        print(f"Setting function shape to {test_shape} on channel 1")
        generator.function_shape1 = test_shape
        print_errors(generator)
        
        # Test burst mode
        print("\nTesting burst mode...")
        print("Setting burst mode parameters on channel 1...")
        generator.burst_mode1 = "GAT"
        generator.burst_ncycles1 = 5
        generator.burst_phase1 = 0.0
        print_errors(generator)
        
        # Test modulation
        print("\nTesting modulation...")
        print("Setting modulation parameters on channel 1...")
        generator.modulation_state1 = True
        generator.modulation_type1 = "AM"
        generator.modulation_depth1 = 50.0
        generator.modulation_rate1 = 1.0 * u.kHz
        print_errors(generator)
        
        # Test sweep
        print("\nTesting sweep...")
        print("Setting sweep parameters on channel 1...")
        generator.sweep_state1 = True
        generator.sweep_time1 = 1.0 * u.s
        generator.sweep_spacing1 = "LIN"
        print_errors(generator)
        
        # Test arbitrary waveform (if supported)
        if generator._check_arbitrary_capability():
            print("\nTesting arbitrary waveform...")
            # Create a simple sine wave
            t = np.linspace(0, 2*np.pi, 1000)
            waveform = np.sin(t)
            print("Loading arbitrary waveform on channel 1...")
            generator.set_arbitrary_waveform(waveform, sample_rate=1000, channel=1)
            print_errors(generator)
            
            # Test saving and loading arbitrary waveform
            print("Saving arbitrary waveform...")
            generator.save_arbitrary_waveform("TEST_WAVE", waveform, channel=1)
            print_errors(generator)
            
            print("Loading arbitrary waveform...")
            generator.load_arbitrary_waveform("TEST_WAVE", channel=1)
            print_errors(generator)
            
            print("Getting available waveforms...")
            waveforms = generator.get_available_waveforms(channel=1)
            print(f"Available waveforms: {waveforms}")
            print_errors(generator)
            
            print("Deleting test waveform...")
            generator.delete_arbitrary_waveform("TEST_WAVE", channel=1)
            print_errors(generator)
        
        # Test dual channel features (if supported)
        if generator._check_dual_channel():
            print("\nTesting dual channel features...")
            
            # Test channel 2 basic parameters
            print("\nTesting channel 2 basic parameters...")
            test_freq2 = 2.0 * u.kHz
            print(f"Setting frequency to {test_freq2} on channel 2")
            generator.frequency2 = test_freq2
            print_errors(generator)
            
            test_voltage2 = 2.0 * u.V
            print(f"Setting voltage to {test_voltage2} on channel 2")
            generator.voltage2 = test_voltage2
            print_errors(generator)
            
            # Test channel 2 burst mode
            print("\nTesting channel 2 burst mode...")
            generator.burst_mode2 = "GAT"
            generator.burst_ncycles2 = 5
            generator.burst_phase2 = 0.0
            print_errors(generator)
            
            # Test channel 2 modulation
            print("\nTesting channel 2 modulation...")
            generator.modulation_state2 = True
            generator.modulation_type2 = "AM"
            generator.modulation_depth2 = 50.0
            generator.modulation_rate2 = 1.0 * u.kHz
            print_errors(generator)
            
            # Test channel 2 sweep
            print("\nTesting channel 2 sweep...")
            generator.sweep_state2 = True
            generator.sweep_time2 = 1.0 * u.s
            generator.sweep_spacing2 = "LIN"
            print_errors(generator)
            
            # Test phase control
            test_phase = 90.0
            print(f"Setting phase to {test_phase} degrees on channel 2")
            generator.set_phase(test_phase, channel=2)
            
            # Test duty cycle
            test_duty = 50.0
            print(f"Setting duty cycle to {test_duty}% on channel 2")
            generator.set_duty_cycle(test_duty, channel=2)
            
            # Test ramp symmetry
            test_symmetry = 50.0
            print(f"Setting ramp symmetry to {test_symmetry}% on channel 2")
            generator.set_ramp_symmetry(test_symmetry, channel=2)
        
        # Test error handling
        print("\nTesting error handling...")
        
        print("Testing invalid frequency...")
        try:
            generator.frequency1 = -1.0 * u.Hz
        except Exception as e:
            print(f"Expected error: {e}")
            
        print("Testing invalid voltage...")
        try:
            generator.voltage1 = 11.0 * u.V  # Should be out of range
        except Exception as e:
            print(f"Expected error: {e}")
            
        if generator._check_dual_channel():
            print("Testing invalid channel...")
            try:
                generator.set_phase(0.0, channel=3)  # Invalid channel
            except Exception as e:
                print(f"Expected error: {e}")
                
        if generator._check_arbitrary_capability():
            print("Testing invalid arbitrary waveform...")
            try:
                generator.set_arbitrary_waveform([1.1], channel=1)  # Value out of range
            except Exception as e:
                print(f"Expected error: {e}")
            
    finally:
        # Cleanup
        print("\nCleaning up...")
        generator.close()
        print("Generator closed successfully")

if __name__ == "__main__":
    main() 