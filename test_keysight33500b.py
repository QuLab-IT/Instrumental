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
    print(f"Frequency: {generator.frequency}")
    print(f"Voltage: {generator.voltage}")
    print(f"Voltage Offset: {generator.voltage_offset}")
    print(f"Function: {generator.function}")
    print(f"Function Shape: {generator.function_shape}")

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
        print(f"Setting frequency to {test_freq}")
        generator.frequency = test_freq
        print_errors(generator)
        
        # Test voltage
        test_voltage = 1.0 * u.V
        print(f"Setting voltage to {test_voltage}")
        generator.voltage = test_voltage
        print_errors(generator)
        
        # Test voltage offset
        test_offset = 0.5 * u.V
        print(f"Setting voltage offset to {test_offset}")
        generator.voltage_offset = test_offset
        print_errors(generator)
        
        # Test function selection
        test_function = "SIN"
        print(f"Setting function to {test_function}")
        generator.function = test_function
        print_errors(generator)
        
        # Test function shape
        test_shape = "SIN"
        print(f"Setting function shape to {test_shape}")
        generator.function_shape = test_shape
        print_errors(generator)
        
        # Test burst mode
        print("\nTesting burst mode...")
        print("Setting burst mode parameters...")
        generator.burst_mode = "GAT"
        generator.burst_ncycles = 5
        generator.burst_phase = 0.0
        print_errors(generator)
        
        # Test modulation
        print("\nTesting modulation...")
        print("Setting modulation parameters...")
        generator.modulation_state = True
        generator.modulation_type = "AM"
        generator.modulation_depth = 50.0
        generator.modulation_rate = 1.0 * u.kHz
        print_errors(generator)
        
        # Test sweep
        print("\nTesting sweep...")
        print("Setting sweep parameters...")
        generator.sweep_state = True
        generator.sweep_time = 1.0 * u.s
        generator.sweep_spacing = "LIN"
        print_errors(generator)
        
        # Test arbitrary waveform (if supported)
        if generator._check_arbitrary_capability():
            print("\nTesting arbitrary waveform...")
            # Create a simple sine wave
            t = np.linspace(0, 2*np.pi, 1000)
            waveform = np.sin(t)
            print("Loading arbitrary waveform...")
            generator.set_arbitrary_waveform(waveform, sample_rate=1000)
            print_errors(generator)
            
            # Test saving and loading arbitrary waveform
            print("Saving arbitrary waveform...")
            generator.save_arbitrary_waveform("TEST_WAVE", waveform)
            print_errors(generator)
            
            print("Loading arbitrary waveform...")
            generator.load_arbitrary_waveform("TEST_WAVE")
            print_errors(generator)
            
            print("Getting available waveforms...")
            waveforms = generator.get_available_waveforms()
            print(f"Available waveforms: {waveforms}")
            print_errors(generator)
            
            print("Deleting test waveform...")
            generator.delete_arbitrary_waveform("TEST_WAVE")
            print_errors(generator)
        
        # Test dual channel features (if supported)
        if generator._check_dual_channel():
            print("\nTesting dual channel features...")
            
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
            generator.frequency = -1.0 * u.Hz
        except Exception as e:
            print(f"Expected error: {e}")
            
        print("Testing invalid voltage...")
        try:
            generator.voltage = 11.0 * u.V  # Should be out of range
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
                generator.set_arbitrary_waveform([1.1])  # Value out of range
            except Exception as e:
                print(f"Expected error: {e}")
            
    finally:
        # Cleanup
        print("\nCleaning up...")
        generator.close()
        print("Generator closed successfully")

if __name__ == "__main__":
    main() 