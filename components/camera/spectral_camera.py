from microscope_system.components.camera.base_camera import ICamera
import numpy as np

# Concrete implementation of ICamera for spectral cameras.
class SpectralCamera(ICamera):
    def __init__(self):
        super().__init__()
    
    # Capture a spectral image. (Placeholder implementation)
    def capture(self) -> np.ndarray:
        # TODO Implement actual spectral image capture
        return np.array([])