import pyvisa

rm = pyvisa.ResourceManager()
waveform_generator = rm.open_resource("USB0::0x0957::0x2807::MY58000523::INSTR")
print(waveform_generator.query("*IDN?"))