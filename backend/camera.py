"""Camera device management with cross-platform backend support."""

import sys
import cv2
from typing import Optional, Tuple
import numpy as np
from config import DEFAULT_CAMERA_WIDTH, DEFAULT_CAMERA_HEIGHT, DEFAULT_CAMERA_BUFFER_SIZE


class CameraManager:
    """Manages OpenCV VideoCapture with platform-adaptive backends."""

    def __init__(
        self,
        camera_index: int = 0,
        width: int = DEFAULT_CAMERA_WIDTH,
        height: int = DEFAULT_CAMERA_HEIGHT,
        buffer_size: int = DEFAULT_CAMERA_BUFFER_SIZE
    ):
        self.camera_index = camera_index
        self.width = width
        self.height = height
        self.buffer_size = buffer_size
        self.cap: Optional[cv2.VideoCapture] = None

    def start(self) -> bool:
        """Initializes the video capture device."""
        self.release()

        # DirectShow is Windows-specific; macOS and Linux use default capture (AVFoundation/V4L)
        if sys.platform.startswith("win"):
            self.cap = cv2.VideoCapture(self.camera_index, cv2.CAP_DSHOW)
        else:
            self.cap = cv2.VideoCapture(self.camera_index)

        if not self.cap or not self.cap.isOpened():
            return False

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, self.buffer_size)
        return True

    def read(self) -> Tuple[bool, Optional[np.ndarray]]:
        """Reads a frame from the camera."""
        if self.cap is None or not self.cap.isOpened():
            return False, None
        return self.cap.read()

    def is_opened(self) -> bool:
        """Returns True if the camera stream is currently open."""
        return self.cap is not None and self.cap.isOpened()

    def release(self):
        """Releases the camera device safely."""
        if self.cap is not None:
            self.cap.release()
            self.cap = None
