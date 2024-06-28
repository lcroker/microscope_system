from pycromanager import Core, start_headless, stop_headless
from typing import Optional, Any

# Singleton class for controlling the microscope.
class Controller(Core):
    _instance: Optional['Controller'] = None

    # Ensure only one instance of Controller is created (Singleton pattern).
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Controller, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    # Initialize the Controller.
    def __init__(self, config_file: str, app_path: str = "C:\\Program Files\\Micro-Manager-2.0", headless: bool = True):
        if self._initialized:
            return
        super().__init__()
        self._app_path = app_path
        self._config_file = config_file
        self.headless = headless
        self._initialize_core()
        self._initialized = True

    # Initialize the core functionality of the controller.
    def _initialize_core(self) -> None:
        if self.headless:
            start_headless(self._app_path, self._config_file, debug=False)
        self.load_system_configuration(self._config_file)

    # Clean up resources when the Controller is deleted.
    def __del__(self) -> None:
        if self.headless:
            stop_headless()

    # Get the current application path.
    @property
    def app_path(self) -> str:
        return self._app_path

    # Set a new application path and reinitialize the core.
    @app_path.setter
    def app_path(self, value: str) -> None:
        self._app_path = value
        self._reinitialize()

    # Get the current configuration file path.
    @property
    def config_file(self) -> str:
        return self._config_file

    # Set a new configuration file and reinitialize the core.
    @config_file.setter
    def config_file(self, value: str) -> None:
        self._config_file = value
        self._reinitialize()

    # Reinitialize the core with new settings.
    def _reinitialize(self) -> None:
        if self.headless:
            stop_headless()
            start_headless(self._app_path, self._config_file, debug=False)
        self.load_system_configuration(self._config_file)

    # Set the current camera device.
    def set_camera_device(self, camera: str) -> None:
        self.set_property("Core", "Camera", camera)

    # Set a property for a specific device.
    def set_property(self, device: str, property_name: str, value: Any) -> None:
        super().set_property(device, property_name, value)

    # Get the width of the image from the current camera.
    def get_image_width(self) -> int:
        return self.get_image_width()

    # Get the height of the image from the current camera.
    def get_image_height(self) -> int:
        return self.get_image_height()

    # Capture an image using the current camera.
    def snap_image(self) -> None:
        super().snap_image()

    # Get the last captured image.
    def get_image(self) -> Any:
        return super().get_image()

    # Get the number of bytes per pixel for the current image format.
    def get_bytes_per_pixel(self) -> int:
        return self.get_image_depth()

    # Set the exposure time for the current camera.
    def set_exposure(self, exposure_ms: float) -> None:
        self.set_exposure(exposure_ms)

    # Get the current exposure time for the camera.
    def get_exposure(self) -> float:
        return self.get_exposure()

    # Move the XY stage to a specified position.
    def set_xy_position(self, x: float, y: float) -> None:
        self.set_xy_position(x, y)

    # Move the Z stage to a specified position.
    def set_position(self, z: float) -> None:
        self.set_position(z)

    # Get the current X position of the XY stage.
    def get_x_position(self) -> float:
        return self.get_x_position()

    # Get the current Y position of the XY stage.
    def get_y_position(self) -> float:
        return self.get_y_position()

    # Get the current Z position of the focus device.
    def get_position(self) -> float:
        return self.get_position()

    # Get the name of the current XY stage device.
    def get_xy_stage_device(self) -> str:
        return self.get_xy_stage_device()

    # Get the name of the current focus (Z) device.
    def get_focus_device(self) -> str:
        return self.get_focus_device()

# To be used throughout the program
controller = Controller(config_file="default_config.cfg")

__all__ = ['controller']