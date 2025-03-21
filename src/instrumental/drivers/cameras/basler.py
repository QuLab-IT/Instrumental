"""Driver for Basler cameras using the pypylon SDK.

This driver supports all Basler cameras compatible with the pypylon SDK.
It has been specifically tested with the acA2000-165umNIR model.
"""
from __future__ import unicode_literals

from pypylon import pylon
from . import Camera
from ..util import check_units
from ...errors import Error, TimeoutError
from ...log import get_logger

log = get_logger(__name__)

def list_instruments():
    """List all available Basler cameras.
    
    Returns
    -------
    list of ParamSet
        List of ParamSets containing information about each available camera.
        Each ParamSet will contain 'serial', 'model', and 'name' parameters.
    """
    from .. import ParamSet
    
    # Get the transport layer factory
    tl_factory = pylon.TlFactory.GetInstance()
    
    # Enumerate all devices
    devices = tl_factory.EnumerateDevices()
    
    # Create ParamSets for each device
    paramsets = []
    for device in devices:
        params = ParamSet(BaslerCamera,
                         serial=device.GetSerialNumber(),
                         model=device.GetModelName(),
                         name=device.GetUserDefinedName())
        # Set the module path explicitly
        params['module'] = 'cameras.basler'
        paramsets.append(params)
        
    return paramsets

class BaslerCamera(Camera):
    """Driver for Basler cameras using the pypylon SDK.
    
    This driver supports all Basler cameras compatible with the pypylon SDK.
    It has been specifically tested with the acA2000-165umNIR model.
    
    Parameters
    ----------
    serial : str, optional
        Serial number of the camera to connect to.
    model : str, optional
        Model name of the camera to connect to.
    name : str, optional
        User-defined name of the camera to connect to.
    """
    
    # Special class variables for Instrumental integration
    _INST_PARAMS_ = ['serial', 'model', 'name']
    _INST_PRIORITY_ = 5  # Lower number = higher priority
    _INST_VISA_INFO_ = ('BASLER', ['acA2000-165umNIR', 'acA2000-165um', 'acA2000-340kmNIR', 'acA2000-340km'])  # (manufacturer, [model names])
    
    def _initialize(self, serial=None, model=None, name=None):
        """Initialize the camera connection.
        
        Parameters
        ----------
        serial : str, optional
            Serial number of the camera to connect to.
        model : str, optional
            Model name of the camera to connect to.
        name : str, optional
            User-defined name of the camera to connect to.
            
        Raises
        ------
        Error
            If no camera is found or if camera creation fails.
        """
        # Get the transport layer factory
        tl_factory = pylon.TlFactory.GetInstance()
        
        # Enumerate all devices
        devices = tl_factory.EnumerateDevices()
        
        # Find the matching device
        matching_device = None
        for device in devices:
            if serial and device.GetSerialNumber() == serial:
                matching_device = device
                break
            elif model and device.GetModelName() == model:
                matching_device = device
                break
            elif name and device.GetUserDefinedName() == name:
                matching_device = device
                break
                
        if not matching_device:
            # If no specific device requested, use the first one
            if not devices:
                raise Error("No Basler cameras found")
            matching_device = devices[0]
            
        # Create and open the camera
        self._camera = pylon.InstantCamera(tl_factory.CreateDevice(matching_device))
        if not self._camera:
            raise Error("Failed to create camera instance")
            
        # Open the camera
        self._camera.Open()
        
        # Set default parameters
        self._camera.ExposureTime.SetValue(10000)  # 10ms default exposure
        self._camera.Gain.SetValue(0)  # Default gain
        self._camera.AcquisitionMode.SetValue("Continuous")  # Continuous acquisition mode
        
        # Initialize live video state
        self._is_live = False
        self._latest_frame = None
        
    @property
    def width(self):
        """Get the current width of the image.
        
        Returns
        -------
        int
            The current width of the image in pixels.
        """
        return self._camera.Width.GetValue()
        
    @property
    def height(self):
        """Get the current height of the image.
        
        Returns
        -------
        int
            The current height of the image in pixels.
        """
        return self._camera.Height.GetValue()
        
    @property
    def max_width(self):
        """Get the maximum width supported by the camera.
        
        Returns
        -------
        int
            The maximum width supported by the camera in pixels.
        """
        return self._camera.Width.GetMax()
        
    @property
    def max_height(self):
        """Get the maximum height supported by the camera.
        
        Returns
        -------
        int
            The maximum height supported by the camera in pixels.
        """
        return self._camera.Height.GetMax()
        
    def start_live_video(self):
        """Start live video acquisition."""
        if not self._is_live:
            self._camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
            self._is_live = True
            
    def stop_live_video(self):
        """Stop live video acquisition."""
        if self._is_live:
            self._camera.StopGrabbing()
            self._is_live = False
            
    def wait_for_frame(self, timeout=None):
        """Wait for and retrieve the next frame.
        
        Parameters
        ----------
        timeout : float, optional
            Timeout in seconds. If None, wait indefinitely.
            
        Returns
        -------
        numpy.ndarray
            The captured frame as a numpy array.
            
        Raises
        ------
        TimeoutError
            If the timeout is reached before a frame is captured.
        Error
            If frame capture fails.
        """
        try:
            # Ensure we're grabbing
            if not self._is_live:
                self._camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
                
            if timeout is not None:
                timeout_ms = int(timeout * 1000)  # Convert to milliseconds
                grab_result = self._camera.RetrieveResult(timeout_ms, pylon.TimeoutHandling_ThrowException)
            else:
                # Use a very large timeout value (1 hour) instead of infinity
                grab_result = self._camera.RetrieveResult(3600000, pylon.TimeoutHandling_ThrowException)
                
            if grab_result is None:
                raise Error("Failed to grab image - no result returned")
                
            if not grab_result.GrabSucceeded():
                grab_result.Release()
                raise Error("Failed to grab image")
                
            # Convert the grabbed image to a numpy array
            img = grab_result.Array
            grab_result.Release()
            
            # Stop grabbing if we weren't in live mode
            if not self._is_live:
                self._camera.StopGrabbing()
                
            return img
            
        except pylon.TimeoutException:
            if not self._is_live:
                self._camera.StopGrabbing()
            raise TimeoutError("Timeout while waiting for frame")
        except Exception as e:
            if not self._is_live:
                self._camera.StopGrabbing()
            if 'grab_result' in locals():
                grab_result.Release()
            raise Error(f"Error while grabbing image: {str(e)}")
            
    def get_latest_frame(self):
        """Get the latest frame from the camera.
        
        Returns
        -------
        numpy.ndarray
            The latest frame as a numpy array.
            
        Raises
        ------
        Error
            If camera is not in live mode or frame capture fails.
        TimeoutError
            If timeout occurs while getting the frame.
        """
        if not self._is_live:
            raise Error("Camera is not in live mode")
            
        try:
            grab_result = self._camera.RetrieveResult(100, pylon.TimeoutHandling_ThrowException)
            
            if grab_result is None:
                raise Error("Failed to grab image - no result returned")
                
            if not grab_result.GrabSucceeded():
                grab_result.Release()
                raise Error("Failed to grab image")
                
            img = grab_result.Array
            grab_result.Release()
            return img
            
        except pylon.TimeoutException:
            raise TimeoutError("Timeout while getting latest frame")
        except Exception as e:
            if 'grab_result' in locals():
                grab_result.Release()
            raise Error(f"Error while grabbing image: {str(e)}")
            
    def grab_image(self, timeout=None):
        """Grab a single image from the camera.
        
        Parameters
        ----------
        timeout : float, optional
            Timeout in seconds. If None, wait indefinitely.
            
        Returns
        -------
        numpy.ndarray
            The captured image as a numpy array.
        """
        if self._is_live:
            return self.get_latest_frame()
        else:
            return self.wait_for_frame(timeout)
            
    def start_capture(self, **kwds):
        """Start a capture sequence and return immediately.
        
        Parameters
        ----------
        **kwds : dict
            Additional keyword arguments for capture settings.
            See grab_image() for available options.
            
        Raises
        ------
        Error
            If camera is in live mode.
        """
        if self._is_live:
            raise Error("Camera is in live mode. Call stop_live_video() first.")
            
        # Set any provided parameters
        if 'exposure_time' in kwds:
            self.set_exposure_time(kwds['exposure_time'])
        if 'gain' in kwds:
            self.set_gain(kwds['gain'])
        if 'width' in kwds or 'height' in kwds:
            self.set_roi(width=kwds.get('width'), height=kwds.get('height'))
        if 'vbin' in kwds or 'hbin' in kwds:
            binning = max(kwds.get('vbin', 1), kwds.get('hbin', 1))
            self.set_binning(binning)
            
        # Start the capture
        self._camera.StartGrabbing(pylon.GrabStrategy_OneByOne)
        
    def get_captured_image(self, timeout='1s', copy=True):
        """Get the image from the last capture sequence.
        
        Parameters
        ----------
        timeout : str or float, optional
            Max time to wait for the image data to be ready.
            If None, will block forever.
        copy : bool, optional
            Whether to return a copy of the image array.
            
        Returns
        -------
        numpy.ndarray
            The captured image as a numpy array.
            
        Raises
        ------
        TimeoutError
            If timeout occurs while waiting for the image.
        Error
            If image capture fails.
        """
        try:
            if isinstance(timeout, str):
                timeout = float(timeout.split()[0])  # Convert '1s' to 1.0
            timeout_ms = int(timeout * 1000) if timeout is not None else 3600000  # 1 hour timeout
            
            grab_result = self._camera.RetrieveResult(timeout_ms, pylon.TimeoutHandling_ThrowException)
            
            if grab_result is None:
                raise Error("Failed to grab image - no result returned")
                
            if not grab_result.GrabSucceeded():
                grab_result.Release()
                raise Error("Failed to grab image")
                
            img = grab_result.Array
            grab_result.Release()
            return img.copy() if copy else img
            
        except pylon.TimeoutException:
            raise TimeoutError("Timeout while waiting for captured image")
        except Exception as e:
            if 'grab_result' in locals():
                grab_result.Release()
            raise Error(f"Error while grabbing image: {str(e)}")
            
    @property
    def latest_frame(self):
        """Get the latest frame from the camera.
        
        Returns
        -------
        numpy.ndarray
            The latest frame as a numpy array.
            
        Raises
        ------
        Error
            If camera is not in live mode or frame capture fails.
        TimeoutError
            If timeout occurs while getting the frame.
        """
        if not self._is_live:
            raise Error("Camera is not in live mode")
            
        try:
            grab_result = self._camera.RetrieveResult(100, pylon.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                img = grab_result.Array
                grab_result.Release()
                return img
            else:
                grab_result.Release()
                raise Error("Failed to grab image")
        except pylon.TimeoutException:
            raise TimeoutError("Timeout while getting latest frame")
            
    @check_units(exposure_time='s')
    def set_exposure_time(self, exposure_time):
        """Set the camera exposure time.
        
        Parameters
        ----------
        exposure_time : float or Quantity
            Exposure time in seconds.
        """
        exposure_us = int(exposure_time.magnitude * 1e6)  # Convert to microseconds
        self._camera.ExposureTime.SetValue(exposure_us)
        
    def set_gain(self, gain):
        """Set the camera gain.
        
        Parameters
        ----------
        gain : float
            Camera gain value.
        """
        self._camera.Gain.SetValue(gain)
        
    def set_roi(self, x=None, y=None, width=None, height=None):
        """Set the region of interest.
        
        Parameters
        ----------
        x : int, optional
            X coordinate of the ROI.
        y : int, optional
            Y coordinate of the ROI.
        width : int, optional
            Width of the ROI.
        height : int, optional
            Height of the ROI.
        """
        if x is not None:
            self._camera.OffsetX.SetValue(x)
        if y is not None:
            self._camera.OffsetY.SetValue(y)
        if width is not None:
            self._camera.Width.SetValue(width)
        if height is not None:
            self._camera.Height.SetValue(height)
            
    def set_binning(self, binning):
        """Set the camera binning.
        
        Parameters
        ----------
        binning : int
            Binning factor (1, 2, 4, etc.).
        """
        self._camera.BinningHorizontal.SetValue(binning)
        self._camera.BinningVertical.SetValue(binning)
        
    def close(self):
        """Close the camera connection."""
        if self._is_live:
            self.stop_live_video()
        if self._camera:
            self._camera.Close()
            self._camera = None