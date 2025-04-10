#!/usr/bin/env python
"""Interactive test script for Basler camera."""

from instrumental.drivers.cameras.basler import BaslerCamera, list_instruments
from instrumental import u  # Import the units module
import matplotlib.pyplot as plt
import time

def print_camera_info(camera):
    """Print basic information about the camera.
    
    Parameters
    ----------
    camera : BaslerCamera
        The camera instance to get information from.
    """
    print("\nCamera Information:")
    print(f"Width: {camera.width}")
    print(f"Height: {camera.height}")
    print(f"Max Width: {camera.max_width}")
    print(f"Max Height: {camera.max_height}")

def display_image(img, title="Camera Image"):
    """Display an image using matplotlib.
    
    Parameters
    ----------
    img : numpy.ndarray
        The image array to display.
    title : str, optional
        The title for the plot.
    """
    plt.figure(figsize=(10, 8))
    plt.imshow(img, cmap='gray')
    plt.title(title)
    plt.colorbar()
    plt.show()

def main():
    """Run the interactive test suite for the Basler camera."""
    print("Searching for Basler cameras...")
    cameras = list_instruments()
    
    if not cameras:
        print("No Basler cameras found")
        return
        
    print(f"\nFound {len(cameras)} Basler camera(s):")
    for i, camera in enumerate(cameras, 1):
        print(f"\nCamera {i}:")
        print(f"  Serial: {camera['serial']}")
        print(f"  Model: {camera['model']}")
        print(f"  Name: {camera['name']}")
    
    # Connect to the first available camera
    print("\nConnecting to the first available camera...")
    camera = BaslerCamera(serial=cameras[0]['serial'])
    
    try:
        # Print camera information
        print_camera_info(camera)
        
        # Test exposure time
        print("\nTesting exposure time...")
        test_exposure = 0.01 * u.s  # 10ms with units
        print(f"Setting exposure time to {test_exposure}")
        camera.set_exposure_time(test_exposure)
        
        # Test gain
        print("\nTesting gain...")
        test_gain = 5.0  # Test with a gain value of 5
        print(f"Setting gain to {test_gain}")
        camera.set_gain(test_gain)
        
        # Test ROI
        print("\nTesting ROI...")
        test_width = camera.max_width // 2
        test_height = camera.max_height // 2
        print(f"Setting ROI to {test_width}x{test_height}")
        camera.set_roi(width=test_width, height=test_height)
        print_camera_info(camera)
        
        # Test binning
        print("\nTesting binning...")
        test_binning = 2
        print(f"Setting binning to {test_binning}")
        camera.set_binning(test_binning)
        
        # Test single image grab
        print("\nTesting single image grab...")
        print("Grabbing image (timeout: 1s)...")
        img = camera.grab_image(timeout=1.0)
        print(f"Image shape: {img.shape}")
        display_image(img, "Single Image Grab")
        
        # Test live video
        print("\nTesting live video...")
        print("Starting live video...")
        camera.start_live_video()
        
        print("Grabbing 5 frames...")
        for i in range(5):
            frame = camera.get_latest_frame()
            display_image(frame, f"Live Frame {i+1}")
            time.sleep(0.5)  # Wait 0.5 seconds between frames
            
        print("Stopping live video...")
        camera.stop_live_video()
        
        # Test latest_frame property
        print("\nTesting latest_frame property...")
        print("Starting live video...")
        camera.start_live_video()
        time.sleep(0.5)  # Wait for a frame
        print("Getting latest frame...")
        frame = camera.latest_frame
        display_image(frame, "Latest Frame Property")
        print("Stopping live video...")
        camera.stop_live_video()
        
        # Test capture sequence
        print("\nTesting capture sequence...")
        print("Starting capture sequence...")
        camera.start_capture(exposure_time=0.01 * u.s)  # Use unitful value here too
        
        print("Getting captured image...")
        img = camera.get_captured_image(timeout=1.0)
        display_image(img, "Captured Image")
        
        # Test error handling
        print("\nTesting error handling...")
        print("Testing invalid exposure time...")
        try:
            camera.set_exposure_time(-1 * u.s)  # Use unitful value for error test too
        except Exception as e:
            print(f"Expected error: {e}")
            
        print("\nTesting invalid ROI...")
        try:
            camera.set_roi(width=-1)
        except Exception as e:
            print(f"Expected error: {e}")
            
        print("\nTesting getting latest frame when not in live mode...")
        try:
            camera.get_latest_frame()
        except Exception as e:
            print(f"Expected error: {e}")
            
        print("\nTesting latest_frame property when not in live mode...")
        try:
            _ = camera.latest_frame
        except Exception as e:
            print(f"Expected error: {e}")
            
    finally:
        # Cleanup
        print("\nCleaning up...")
        camera.close()
        print("Camera closed successfully")

if __name__ == "__main__":
    main() 