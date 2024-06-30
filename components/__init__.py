from microscope_system.components.stage import Stage
from microscope_system.components.lamp import Lamp
from microscope_system.components.camera.base_camera import ICamera
from microscope_system.components.camera.stage_camera import StageCamera
from microscope_system.components.camera.spectral_camera import SpectralCamera

__all__ = ['Stage', 'Lamp', 'ICamera', 'StageCamera', 'SpectralCamera']