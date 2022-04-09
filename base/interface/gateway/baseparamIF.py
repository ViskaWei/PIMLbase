from abc import ABC, abstractmethod

class BaseParamIF(ABC):
    @abstractmethod
    def set_param(self, PARAM):
        pass

    @abstractmethod
    def get(self, PARAM):
        pass