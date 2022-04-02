
from abc import ABC, abstractmethod

class BaseData(ABC):
    @abstractmethod
    def set_data(self, data):
        pass