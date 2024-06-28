from microscope_system.components.camera.base_camera import ICamera
import numpy as np

# Concrete implementation of ICamera for standard cameras.
class StageCamera(ICamera):
    def __init__(self):
        super().__init__()
        self.width = self.controller.get_image_width()
        self.height = self.controller.get_image_height()
        # self.set_exposure()

    # Capture an image from the camera.
    def capture(self) -> np.ndarray:
        self.controller.snap_image()
        img = self.controller.get_image()

        byte_depth = self.controller.get_bytes_per_pixel()

        if byte_depth == 1:
            img = np.reshape(img, (self.height, self.width)).astype(np.uint8)
        elif byte_depth == 2:
            img = np.reshape(img, (self.height, self.width)).astype(np.uint16)
        else:
            raise ValueError(f'Invalid byte depth: {byte_depth}')
        
        self.snapped_image = img
        return self.snapped_image