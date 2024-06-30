from abc import ABC, abstractmethod

class BaseCellIdentifier(ABC):
    @abstractmethod
    def identify_cells(self, image):
        pass