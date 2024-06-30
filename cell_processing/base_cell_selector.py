from abc import ABC, abstractmethod

class BaseCellSelector(ABC):
    @abstractmethod
    def select_cells(self, cell_positions, n_cells):
        pass