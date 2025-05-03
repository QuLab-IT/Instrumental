from instrumental.drivers.vacuum.ngc import NGC2D

ngc = NGC2D(port='USB0')
ngc.poll()
print(ngc._ser)