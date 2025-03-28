Basler Cameras
=============

.. module:: instrumental.drivers.cameras.basler

Driver for Basler cameras using the pypylon SDK. This driver supports all Basler cameras
that are compatible with the pypylon SDK, including the acA2000-165umNIR model.

Requirements
-----------

- pypylon (Basler's Python SDK)
- numpy

Installation
-----------

1. Install the pypylon SDK from Basler's website: https://www.baslerweb.com/en/downloads/software-downloads/
2. Install the Python package::

   pip install pypylon

Usage
-----

Basic usage::

    from instrumental import list_instruments
    from instrumental.drivers.cameras import BaslerCamera
    from instrumental import u  # For unitful values

    # List available Basler cameras
    cameras = list_instruments(module='cameras.basler')
    
    # Connect to a specific camera by serial number
    camera = BaslerCamera(serial='12345678')
    
    # Or by model name
    camera = BaslerCamera(model='acA2000-165umNIR')
    
    # Or by user-defined name
    camera = BaslerCamera(name='My Camera')

    # Grab a single image with unitful exposure time
    img = camera.grab_image(exposure_time=0.01 * u.s, gain=1.0)
    
    # Start live video
    camera.start_live_video(exposure_time=0.01 * u.s, gain=1.0)
    
    # Wait for a frame
    if camera.wait_for_frame(timeout=1.0):
        frame = camera.latest_frame
    
    # Stop live video
    camera.stop_live_video()

Supported Parameters
------------------

The following parameters are supported in the camera configuration:

- exposure_time: Camera exposure time (as a Quantity with units, e.g. 0.01 * u.s)
- gain: Camera gain value (dimensionless float)
- vbin: Vertical binning factor
- hbin: Horizontal binning factor
- left, top, right, bot: ROI coordinates

Pixel Formats
------------

The driver supports the following pixel formats:
- Mono8 (8-bit grayscale)
- Mono12 (12-bit grayscale)
- RGB8 (24-bit color)

Troubleshooting
--------------

1. If no cameras are found:
   - Ensure the pypylon SDK is properly installed
   - Check if the camera is properly connected and powered
   - Verify the camera is recognized by the system

2. If connection fails:
   - Check if the camera is already in use by another application
   - Verify the camera's serial number, model name, or user-defined name
   - Ensure proper permissions to access the camera

3. If image capture fails:
   - Check if the exposure time is within the camera's supported range
   - Verify the gain value is valid
   - Ensure the ROI coordinates are within the camera's maximum dimensions

Known Limitations
---------------

1. The driver currently only supports basic camera operations. Advanced features like:
   - Trigger modes
   - Multiple ROI
   - Custom pixel formats
   may require additional implementation.

2. Some camera models may have specific features or limitations not covered by this driver.

Contributing
-----------

If you encounter any issues or have suggestions for improvements, please report them on the
Instrumental GitHub repository. 