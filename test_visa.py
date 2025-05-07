print("debug 1 ")
from instrumental.drivers.funcgenerators.keysight33500b import Keysight33500B, SourFuncShapeCommandParameter1clone, Enum33500bBoolean
print("debug 2 ")
import instrumental
print("debug 3 ")
import instrumental.drivers # Necessary for list_visa_instruments
print("debug 4 ")

# ks: Keysight33500B = Keysight33500B()

# ks.set_source_function(shape=SourFuncShapeCommandParameter1clone.SINUSOID)
# ks.set_output(state=Enum33500bBoolean.ON)



# rm = pyvisa.ResourceManager()
# waveform_generator = rm.open_resource("USB0::0x0957::0x2807::MY58000523::INSTR")
# print(waveform_generator.query("*IDN?"))

# Make sure you have a VISA backend (like NI-VISA) installed
# and pyvisa can find it.
import pyvisa
import traceback

try:
    # Create a resource manager instance.
    # This automatically finds the installed VISA backend.
    rm = pyvisa.ResourceManager()

    # List all detected VISA resources (USB, TCPIP, GPIB, etc.)
    resources = rm.list_resources()
    print("debug 5 ")
    if not resources:
        print("No VISA resources found by pyvisa.")
        print("Ensure a VISA backend (e.g., NI-VISA, Keysight IO Libraries) is installed and configured.")
    else:
        print("Found VISA resources:")
        for resource_string in resources:
            print(f"- {resource_string}")

except pyvisa.errors.VisaIOError as e:
    print(f"VISA Error: {e}")
    print("Could not initialize VISA. Is the backend library installed correctly?")
    # print(traceback.format_exc()) # Uncomment for more detailed error info
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    print(traceback.format_exc()) # Print detailed traceback

finally:
    # It's good practice to close the resource manager,
    # though often not strictly necessary for just listing.
    if 'rm' in locals() and rm:
        try:
            rm.close()
        except Exception:
            pass # Ignore errors during cleanup