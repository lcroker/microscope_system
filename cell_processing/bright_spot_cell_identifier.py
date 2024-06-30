import numpy as np
from scipy import ndimage
from microscope_system.cell_processing.base_cell_identifier import BaseCellIdentifier

class BrightSpotCellIdentifier(BaseCellIdentifier):
    def identify_cells(self, image):
        smoothed = ndimage.gaussian_filter(image, sigma=2)
        local_max = ndimage.maximum_filter(smoothed, size=20) == smoothed
        coordinates = np.column_stack(np.nonzero(local_max))
        return coordinates