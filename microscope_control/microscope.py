import numpy as np
from typing import Type
from microscope_system.components.camera.base_camera import ICamera
from microscope_system.components.camera.stage_camera import StageCamera
from microscope_system.components.stage import Stage
from microscope_system.components.lamp import Lamp
from microscope_system.autofocus.base_autofocus import IAutofocus
from microscope_system.microscope_control.controller import Controller, controller
from microscope_system.microscope_control.exceptions import MicroscopeError, CameraError, StageError, LampError

# Main class representing the microscope system.
class Microscope:

    # Initialize the Microscope with a given configuration file.
    def __init__(self, config_file: str):
        self.controller = Controller(config_file)
        global controller
        controller = self.controller  # Update the global controller
        self.camera: ICamera = StageCamera()
        self.stage: Stage = Stage()
        self.lamp: Lamp = Lamp()
        self.autofocus_strategy: IAutofocus = None

    # Perform autofocus using the specified strategy.
    def auto_focus(self, autofocus_strategy: Type[IAutofocus], start: int, end: int, step: float = 1) -> float:
        self.autofocus_strategy = autofocus_strategy(self.camera, self.stage, self.lamp)
        return self.autofocus_strategy.focus(start, end, step)

    # Capture an image using the current camera.
    def capture_image(self) -> np.ndarray:
        return self.camera.capture()

    # Move the stage to the specified position.
    def move_stage(self, x: float = None, y: float = None, z: float = None) -> None:
        self.stage.move(x, y, z)

    # Turn the lamp on or off.
    def set_lamp(self, on: bool) -> None:
        if on:
            self.lamp.set_on()
        else:
            self.lamp.set_off()

    # Update the microscope configuration.
    def update_config(self, new_config_file: str) -> None:
        self.controller.config_file = new_config_file
        # Reinitialize components with the new configuration
        global controller
        controller = self.controller
        self.camera = StageCamera()
        self.stage = Stage()
        self.lamp = Lamp()

    # Get the current stage position.
    def get_stage_position(self) -> tuple[float, float, float]:
        return self.stage.get_position()

    # Get the current lamp state.
    def get_lamp_state(self) -> str:
        return self.lamp.get_state()

    # Set the camera exposure.
    def set_camera_exposure(self, exposure: float) -> None:
        self.camera.set_exposure(exposure)

    # Get the current camera exposure.
    def get_camera_exposure(self) -> float:
        return self.camera.get_exposure()