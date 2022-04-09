from abc import ABC, abstractmethod
from .basedata import BaseData
from .baseoperation import BaseOperation

class BaseProcess(ABC):
    """ Base class for Process. """
    @abstractmethod
    def set_process(self):
        pass
    
    @abstractmethod
    def start(self, data):
        pass

class Process(BaseProcess):
    def __init__(self) -> None:
        self.operation_list: list[BaseOperation] = None

    def set_process(self, OP, MODEL, DATA):
        self.operation_list = []

    def start(self, BaseData: BaseData):
        for operation in self.operation_list:
            operation.perform(BaseData)