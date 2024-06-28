from microscope_system.autofocus.base_autofocus import IAutofocus
import numpy as np
import tifffile as tiff

# Phase-based autofocus algorithm.
class PhaseAutofocus(IAutofocus):

    def focus(self, start: int, end: int, step: float) -> float:
        self.zscan(start, end, step)
        min_var, min_index, variances = 1e10, -1, []

        for i, capture_path in enumerate(self.captures):
            try:
                image = tiff.imread(capture_path)
                mean = np.mean(image)
                if mean == 0:
                    continue
                std = np.std(image)
                norm_var = std * std / mean
                variances.append(norm_var)
                if norm_var < min_var:
                    min_var, min_index = norm_var, i
            except Exception as e:
                print(f"Error processing capture {i}: {e}")

        return self.start + self.step * min_index