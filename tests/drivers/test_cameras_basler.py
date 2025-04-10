"""Tests for the Basler camera driver."""
import pytest
import numpy as np
from instrumental.drivers.cameras.basler import BaslerCamera, list_instruments

def test_list_instruments():
    """Test that we can list available Basler cameras."""
    cameras = list_instruments()
    assert isinstance(cameras, list)
    if cameras:  # If any cameras are connected
        assert all(hasattr(cam, 'serial') for cam in cameras)
        assert all(hasattr(cam, 'model') for cam in cameras)
        assert all(hasattr(cam, 'name') for cam in cameras)

class TestBasler_Camera(object):
    """Test class for Basler camera driver."""
    
    def test_camera_initialization(self, inst):
        """Test that the camera initializes correctly."""
        assert inst._camera is not None
        assert not inst._is_live
        assert inst._latest_frame is None

    def test_camera_properties(self, inst):
        """Test camera properties."""
        assert inst.width > 0
        assert inst.height > 0
        assert inst.max_width >= inst.width
        assert inst.max_height >= inst.height

    def test_exposure_time(self, inst):
        """Test setting and getting exposure time."""
        test_exposure = 0.01  # 10ms
        inst.set_exposure_time(test_exposure)
        # Note: We can't directly get the exposure time from the camera
        # as it's not exposed in the current implementation

    def test_roi(self, inst):
        """Test setting ROI."""
        # Test with half the maximum dimensions
        test_width = inst.max_width // 2
        test_height = inst.max_height // 2
        inst.set_roi(width=test_width, height=test_height)
        assert inst.width == test_width
        assert inst.height == test_height

    def test_binning(self, inst):
        """Test setting binning."""
        test_binning = 2
        inst.set_binning(test_binning)
        # Note: We can't directly verify the binning as it's not exposed in the current implementation

    def test_grab_image(self, inst):
        """Test grabbing a single image."""
        img = inst.grab_image(timeout=1.0)
        assert isinstance(img, np.ndarray)
        assert img.shape == (inst.height, inst.width)

    def test_live_video(self, inst):
        """Test live video functionality."""
        # Start live video
        inst.start_live_video()
        assert inst._is_live
        
        # Get a frame
        frame = inst.get_latest_frame()
        assert isinstance(frame, np.ndarray)
        assert frame.shape == (inst.height, inst.width)
        
        # Stop live video
        inst.stop_live_video()
        assert not inst._is_live

    def test_capture_sequence(self, inst):
        """Test capture sequence functionality."""
        # Start capture
        inst.start_capture(exposure_time=0.01)
        
        # Get captured image
        img = inst.get_captured_image(timeout=1.0)
        assert isinstance(img, np.ndarray)
        assert img.shape == (inst.height, inst.width)

    def test_error_handling(self, inst):
        """Test error handling."""
        # Test invalid exposure time
        with pytest.raises(Exception):
            inst.set_exposure_time(-1)
        
        # Test invalid ROI
        with pytest.raises(Exception):
            inst.set_roi(width=-1)
        
        # Test getting latest frame when not in live mode
        with pytest.raises(Exception):
            inst.get_latest_frame()

    def test_camera_cleanup(self, inst):
        """Test camera cleanup."""
        inst.start_live_video()
        inst.close()
        assert inst._camera is None
        assert not inst._is_live
        assert inst._latest_frame is None 