import numpy as np
from typing import Type
from microscope_system.components.camera.base_camera import ICamera
from microscope_system.components.camera.stage_camera import StageCamera
from microscope_system.components.stage import Stage
from microscope_system.components.lamp import Lamp
from microscope_system.autofocus.base_autofocus import IAutofocus
from microscope_system.microscope_control.controller import Controller, controller
from microscope_system.microscope_control.exceptions import MicroscopeError, CameraError, StageError, LampError
from microscope_system.microscope_control.strategy_registry import strategy_registry

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
        self.strategy_registry = strategy_registry
        self.autofocus = None
        self.cell_identifier = None
        self.cell_selector = None
        self.cell_processor = None

    def set_autofocus(self, strategy_name: str):
        strategy_class = self.strategy_registry.get_autofocus(strategy_name)
        if strategy_class:
            self.autofocus = strategy_class(self.camera, self.stage, self.lamp)
        else:
            raise ValueError(f"Unknown autofocus strategy: {strategy_name}")

    def set_cell_identifier(self, strategy_name: str):
        strategy_class = self.strategy_registry.get_cell_identifier(strategy_name)
        if strategy_class:
            self.cell_identifier = strategy_class()
        else:
            raise ValueError(f"Unknown cell identifier strategy: {strategy_name}")

    def set_cell_selector(self, strategy_name: str):
        strategy_class = self.strategy_registry.get_cell_selector(strategy_name)
        if strategy_class:
            self.cell_selector = strategy_class()
        else:
            raise ValueError(f"Unknown cell selector strategy: {strategy_name}")

    def set_cell_processor(self, strategy_name: str):
        strategy_class = self.strategy_registry.get_cell_processor(strategy_name)
        if strategy_class:
            self.cell_processor = strategy_class()
        else:
            raise ValueError(f"Unknown cell processor strategy: {strategy_name}")

    def run_analysis(self):
        if not all([self.autofocus, self.cell_identifier, self.cell_selector, self.cell_processor]):
            raise ValueError("All strategies must be set before running analysis")

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