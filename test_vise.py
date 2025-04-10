import pyvisa
import time

def test_visa_connection():
    """Test basic VISA connection and communication with the device."""
    try:
        # Create a resource manager
        rm = pyvisa.ResourceManager()
        
        # Open connection to the device (replace with your device's address)
        device_address = 'USB0::0x0957::0x2807::MY58000523::INSTR'
        
        print(f"\nAttempting to connect to device at: {device_address}")
        inst = rm.open_resource(device_address)
        
        # Set timeout and termination characters
        inst.timeout = 10000  # 10 seconds timeout
        inst.write_termination = '\r\n'  # Changed to \r\n
        inst.read_termination = '\r\n'   # Changed to \r\n
        
        # Print device settings
        print("\nDevice settings:")
        print(f"Timeout: {inst.timeout}ms")
        print(f"Write termination: {repr(inst.write_termination)}")  # Using repr to see actual characters
        print(f"Read termination: {repr(inst.read_termination)}")    # Using repr to see actual characters
        
        # Try to clear the device first
        print("\nSending *CLS command...")
        try:
            inst.write('*CLS')
            print("Clear command sent successfully")
        except Exception as e:
            print(f"Error during *CLS command: {str(e)}")
            # Try without termination characters
            print("\nTrying without termination characters...")
            inst.write_termination = ''
            inst.read_termination = ''
            inst.write('*CLS')
            print("Clear command sent successfully without termination characters")
        
        # Try to get device identification
        print("\nQuerying device identification...")
        try:
            idn = inst.query('*IDN?')
            print(f"Device response: {idn}")
        except Exception as e:
            print(f"Error during *IDN? query: {str(e)}")
            # Try without termination characters
            print("\nTrying without termination characters...")
            inst.write_termination = ''
            inst.read_termination = ''
            idn = inst.query('*IDN?')
            print(f"Device response: {idn}")
        
        # Try a simple write command
        print("\nSending *RST command...")
        try:
            inst.write('*RST')
            print("Reset command sent successfully")
        except Exception as e:
            print(f"Error during *RST command: {str(e)}")
        
        # Try to read any error messages
        print("\nChecking for error messages...")
        try:
            errors = inst.query(':SYST:ERR?')
            print(f"Error messages: {errors}")
        except Exception as e:
            print(f"Error checking error messages: {str(e)}")
        
        # Close the connection
        print("\nClosing connection...")
        inst.close()
        rm.close()
        
        print("Test completed!")
        
    except Exception as e:
        print(f"Error occurred: {str(e)}")
        if 'inst' in locals():
            inst.close()
        if 'rm' in locals():
            rm.close()

if __name__ == "__main__":
    test_visa_connection() 