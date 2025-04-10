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
from instrumental.drivers.vacuum.ngc2d import NGC2D


def main():
    # Create NGC2D instance (replace 'COM1' with your actual port)
    ngc = NGC2D(port="COM1")

    try:
        # Set remote control
        print("Setting remote control...")
        ngc.control()

        # Select ion gauge 1
        print("Selecting ion gauge 1...")
        ngc.select_ion_gauge("1")

        # Turn on the gauge with 0.5mA emission current
        print("Turning on ion gauge...")
        ngc.gauge_on("0")  # '0' for 0.5mA emission current

        # Read and print status
        print("\nReading status...")
        status = ngc.get_status()
        for gauge_id, gauge_info in status.items():
            print(f"\nGauge {gauge_id}:")
            print(f"  Type: {gauge_info['type']}")
            print(f"  Status: {gauge_info['status']}")
            print(f"  Error: {gauge_info['error']}")
            print(f"  Pressure: {gauge_info['pressure']}")

    finally:
        # Always close the connection
        print("\nClosing connection...")
        ngc.close()


if __name__ == "__main__":
    main()
