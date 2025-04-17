#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Example script demonstrating basic usage of the NGC2D pressure gauge controller.
This script:
1. Connects to the NGC2D
2. Sets remote control
3. Selects ion gauge 1
4. Turns on the gauge
5. Reads the status
6. Closes the connection
"""
from instrumental.drivers.vacuum.ngc2d import NGC2_D, IonGaugeSelection, EmissionCurrent

def main():
    # Create NGC2D instance (replace 'COM1' with your actual port)
    ngc: NGC2_D = NGC2_D()
    
    try:
        # Set remote control
        print("Setting remote control...")
        ngc.control()
        
        # Select ion gauge 1
        print("Selecting ion gauge 1...")
        ngc.select_ion_gauge(IonGaugeSelection.ION_GAUGE_1)
        
        # Turn on the gauge with 0.5mA emission current
        print("Turning on ion gauge...")
        ngc.gauge_on(EmissionCurrent.mA_0_5)
        
        # Read and print status
        print("\nReading status...")
        status = ngc.get_status()
        for gauge in status.gauges:
            print(f"\nGauge {gauge.id}:")
            print(f"  Type: {gauge.type}")
            print(f"  Status: {gauge.status}")
            print(f"  Error: {gauge.error}")
            print(f"  Pressure: {gauge.pressure}")
            
    finally:
        # Always close the connection
        print("\nClosing connection...")
        ngc.close()

if __name__ == '__main__':
    main() 