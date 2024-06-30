from abc import ABC, abstractmethod

class BaseCellProcessor(ABC):
    @abstractmethod
    def process_cell(self, microscope, cell_position):
        pass