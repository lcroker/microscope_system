import numpy as np
from scipy.spatial.distance import pdist, squareform
from microscope_system.cell_processing.base_cell_selector import BaseCellSelector

class IsolatedCellSelector(BaseCellSelector):
    def select_cells(self, cell_positions, n_cells):
        distances = pdist(cell_positions)
        dist_matrix = squareform(distances)
        isolation_scores = np.sum(dist_matrix, axis=1)
        most_isolated = np.argsort(isolation_scores)[-n_cells:]
        return cell_positions[most_isolated]