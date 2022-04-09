from abc import ABC, abstractmethod


class LoaderPipeline(ABC):
    """ Base class for all objects. """
    @abstractmethod
    def run(self):
        pass
    