from abc import ABC, abstractmethod
from typing import Any, Optional
import numpy as np
from microscope_system.microscope_control.controller import controller

# Abstract base class for camera interfaces.
class ICamera(ABC):
    def __init__(self, camera: str):
        self.controller = controller
        self.camera = camera
        self.snapped_image: Optional[np.ndarray] = None
        self.controller.set_camera_device(self.camera)

    # Set a camera option.
    def set_option(self, option: str, value: Any) -> None:
        
        self.controller.set_property(self.camera, option, value)

    # Set the camera exposure.
    def set_exposure(self, val: int = 15) -> None:
        self.controller.set_exposure(val)

    # Capture an image. This method must be implemented by subclasses.
    @abstractmethod
    def capture(self) -> np.ndarray:
        pass



