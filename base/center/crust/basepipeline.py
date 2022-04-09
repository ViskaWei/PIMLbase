
from abc import ABC, abstractmethod

class BasePipeline(ABC):
    """ Base class for Pipeline. """
    @abstractmethod
    def run(self):
        pass