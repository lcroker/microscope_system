import numpy as np
import tifffile as tiff
from microscope_system.autofocus.base_autofocus import IAutofocus
from microscope_system.utils.image_processing import calculate_image_variance

class BrightSpotAutofocus(IAutofocus):
    def focus(self, start: int, end: int, step: float) -> float:
        self.zscan(start, end, step)
        max_var, max_index = -1, -1

        for i, capture_path in enumerate(self.captures):
            try:
                image = tiff.imread(capture_path)
                variance = calculate_image_variance(image)
                if variance > max_var:
                    max_var, max_index = variance, i
            except Exception as e:
                print(f"Error processing capture {i}: {e}")

        return self.start + self.step * max_index

    def zscan(self, start: int, end: int, step: float = 1) -> None:
        super().zscan(start, end, step)
        self.camera.set_option("Binning", "1x1")
        self.camera.set_option("PixelType", "GRAY8")
        self.camera.set_exposure(25)  # 25ms exposure time
        self.controller.set_property("Condenser", "Aperture", 0)  # Assuming 0 is fully closed