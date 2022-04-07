from abc import ABC, abstractmethod
from ...center.crust.baseprocess import Process
from .baseloaderIF import ObjectLoaderIF
from .basestorerIF import BaseStorerIF


class BaseProcessIF(ABC):
    """ Base class for Process interface for data. """
    @abstractmethod
    def set_data(self, DATA_PARAM):
        pass
    @abstractmethod
    def set_param(self, OP_PARAM):
        pass
    @abstractmethod
    def set_model(self, MODEL_TYPES):
        pass
    @abstractmethod
    def set_out(self, out):
        pass
    @abstractmethod
    def interact(self, param, data):
        pass
    @abstractmethod
    def interact_on_Object(self, Object):
        pass

class ProcessIF(BaseProcessIF):
    def __init__(self) -> None:
        self.OP_PARAM: dict = {}
        self.OP_MODEL: dict = {}
        self.OP_DATA : dict = {}
        self.OP_OUT  : dict = {}
        
        self.Loader : ObjectLoaderIF = None
        self.Storer : BaseStorerIF = None
        self.Process: Process = None 

    def set_object(self, OBJECT_PARAM):
        self.Loader.set_param(OBJECT_PARAM)
        self.Object = self.Loader.load()

    def setup(self, PARAM):
        if "DATA" in PARAM: self.set_data(PARAM["DATA"])
        if "OP"   in PARAM: self.set_param(PARAM["OP"])
        if "MODEL"in PARAM: self.set_model(PARAM["MODEL"])
        if "OUT"  in PARAM: self.set_out(PARAM["OUT"])

    def interact(self, PARAM):
        self.set_object(PARAM["OBJECT"])
        self.setup(PARAM)
        self.interact_on_Object(self.Object)
    
    def interact_on_Object(self, Object):
        self.Process.set_process(self.OP_PARAM, self.OP_MODEL, self.OP_DATA)
        self.Process.start(Object)

    def set_out(self, PARAM):
        self.OP_OUT = PARAM

    def finish(self, store_path):
        # store
        pass