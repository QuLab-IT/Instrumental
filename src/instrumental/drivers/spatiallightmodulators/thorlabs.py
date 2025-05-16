""" SLM (Spatial light modulator) controller

    Controls a SLM as if it was an external monitor
"""

from typing import Final, Literal, TypedDict
import time
import cv2
import screeninfo
import mss
import numpy as np
from .. import colorLog as log

_INST_PARAMS = ['port']
_INST_CLASSES = ['ExulusHD']

class SLMConfig(TypedDict, total=True):
    """SLM config class

    Args:
        screen (int): screen id.
        force_single_monitor (bool): forces the SLM controller to start
            even if there is only one screen. Defaults to False.
        delay (int): Minimum delay, in milliseconds, after updating the SLM
    """

    type: Literal["SLMConfig"]
    screen_id: int
    force_single_monitor: bool
    delay: int


    @staticmethod
    @classmethod
    def default_config(cls) -> "SLMConfig":
        """Creates a default SLMConfig

        Returns:
            SLMConfig: Default configuration for the SLM
        """
        return {
            "type": "SLMConfig",
            "screen_id": 0,
            "force_single_monitor": False,
            "delay": 120,
        }


class ExulusHD:
    """SLM (Spatial light modulator) controller

    Args:
        config (SLMConfig | None, optional): SLM config. Defaults to None.

    Raises:
        ValueError: Invalid screen id (No external screen were found)
        IndexError: Invalid screen id (Screen id is invalid or does not exist)
        RuntimeError: There is a problem with the SLM display
    """

    WINDOW_NAME: Final[str] = "projector"

    def __init__(self, config: SLMConfig | None = None):
        # Obtain config
        if config is None:
            self.config = ExulusHD.default_config()
        else:
            self.config = config

        self.screen_id = self.config["screen_id"]
        self.delay = self.config["delay"]

        # Get monitors
        monitors = screeninfo.get_monitors()

        if len(monitors) < 2 and not self.config["force_single_monitor"]:
            raise ValueError("No external monitor detected")

        if self.screen_id < 0 or self.screen_id >= len(monitors):
            raise IndexError(f"No external monitor detected, with id: {self.screen_id}")

        log.debug("Found " + str(len(monitors)) + " monitors.")
        # log.debug(screeninfo.get_monitors())

        # Select screen by id or principal if not stated.
        self.screen = monitors[self.screen_id]

        # get the size of the screen
        self.width, self.height = self.screen.width, self.screen.height

        # Checks if the SLM is ready to use
        self.self_check()

    def update_array(self, image: cv2.typing.MatLike):
        """Updates the BGR image projected onto the SLM

        Args:
            image (MatLike): The BGR image to be projected
        """
        cv2.namedWindow(self.WINDOW_NAME, cv2.WND_PROP_FULLSCREEN)
        cv2.moveWindow(self.WINDOW_NAME, self.screen.x - 1, self.screen.y - 1)
        cv2.setWindowProperty(
            self.WINDOW_NAME, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN
        )
        cv2.setWindowProperty(self.WINDOW_NAME, cv2.WND_PROP_TOPMOST, 1)
        cv2.imshow(self.WINDOW_NAME, image)

        # Screen update  + delay
        # It updates the screen and waits for
        # an input during x miliseconds before
        # resuming. "0" causes it to stop indefinitely
        cv2.waitKey(self.delay)

    @property
    def size(self) -> tuple[int, int]:
        """Screen dimensions

        Returns:
            tuple: Screen dimensions with:
            (int) Screen width
            (int) Screen height
        """
        return self.width, self.height

    def capture_screen(self) -> np.ndarray:
        """Captures a screenshot of the screen used by the SLM

        Returns:
            np.ndarray: RGB screenshot
        """
        time.sleep(0.2)  # Wait for the screen to update
        with mss.mss() as sct:
            # Get information of monitor 2
            monitor_number = self.screen_id + 1
            mon = sct.monitors[monitor_number]

            # Part of the screen to capture
            monitor = {
                "top": mon["top"],
                "left": mon["left"],
                "width": mon["width"],
                "height": mon["height"],
                "mon": monitor_number,
            }

            # Get raw pixels from the screen, save it to a Numpy array
            screenshot = sct.grab(monitor)
            return cv2.cvtColor(np.array(screenshot), cv2.COLOR_BGRA2RGB)

    def self_check(self):
        """
        The SLM checks if a displayed image is being correctly shown on the SLM display
            This can happen when there is another window or device occupying the SLM display
        Raises:
            RuntimeError: When the image is not shown as intended on the SLM
        """
        rand_img = (np.random.standard_normal([3, 3, 3]) * 255).astype("uint8")
        rand_img = cv2.resize(
            rand_img, [self.width, self.height], interpolation=cv2.INTER_NEAREST
        )
        self.update_array(rand_img)
        screenshot = self.capture_screen()
        self.close()
        rand_img_rgb = cv2.cvtColor(rand_img, cv2.COLOR_RGB2BGR)

        absolute_diferrence = np.abs(np.sum(screenshot - rand_img_rgb))
        if absolute_diferrence > 1:
            raise RuntimeError(
                f"The image is not shown as itended on the SLM | diff:{absolute_diferrence}"
            )

    def close(self):
        """Stops projecting an image onto the SLM"""
        try:
            cv2.destroyWindow(self.WINDOW_NAME)
        except cv2.error:
            pass

    @staticmethod
    def default_config() -> SLMConfig:
        """Default config

        Returns:
            SLMConfig: Default SLM config
        """
        return default()
