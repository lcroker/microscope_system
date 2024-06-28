from abc import ABC, abstractmethod
from typing import List, Tuple
import numpy as np
import pandas as pd
import tifffile as tiff
from microscope_system.components.camera.base_camera import ICamera
from microscope_system.components.camera.stage_camera import StageCamera
from microscope_system.components.camera.spectral_camera import SpectralCamera
from microscope_system.components.lamp import Lamp
from microscope_system.components.stage import Stage

# Abstract base class for autofocus algorithms.
class IAutofocus(ABC):
    def __init__(self, camera: ICamera, stage: Stage, lamp: Lamp, image_dir: str = "Autofocus"):
        self.camera = camera
        self.lamp = lamp
        self.stage = stage
        self.image_dir = image_dir
        self.captures: List[str] = []
        self.start: int = 0
        self.end: int = 0
        self.step: float = 0

    # Perform a Z-scan, capturing images at different Z positions.
    def zscan(self, start: int, end: int, step: float = 1) -> None:
        self.start = start
        self.end = end
        self.step = step

        self.lamp.set_on()

        for i, z_val in enumerate(np.arange(start, end, step)):
            try:
                img = self.camera.capture()
                if isinstance(self.camera, StageCamera):
                    pre_path = f"{self.image_dir}/images/capture_{i}.tif"
                    tiff.imwrite(pre_path, img)
                    self.captures.append(pre_path)
                elif isinstance(self.camera, SpectralCamera):
                    pre_path = f"{self.image_dir}/spectra/capture_{i}.csv"
                    pd.DataFrame(img).to_csv(pre_path, index=False)
                    self.captures.append(pre_path)
            except Exception as e:
                print(f"Error capturing at z={z_val}: {e}")
            self.stage.move(z=z_val)

        self.stage.move(z=start)
        self.lamp.set_off()

    # Perform autofocus and return the best focus position.
    @abstractmethod
    def focus(self, start: int, end: int, step: float) -> float:
        pass





