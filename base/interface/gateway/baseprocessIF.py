from abc import ABC, abstractmethod
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

class ProcessIF(BaseProcessIF):
    def __init__(self) -> None:
        self.OP_PARAM: dict = {}
        self.OP_MODEL: dict = {}
        self.OP_DATA : dict = {}
        self.OP_OUT  : dict = {}
        
        self.Loader : ObjectLoaderIF = None
        self.Storer : BaseStorerIF = None
        self.Process = None 

    def set_object(self, OBJECT_PARAM):
        self.Loader.set_param(OBJECT_PARAM)
        self.Object = self.Loader.load()

    def setup(self, PARAM):
        self.set_data(PARAM["data"])
        self.set_param(PARAM["op"])
        self.set_model(PARAM["model"])
        if "out" in PARAM:
            self.set_out(PARAM["out"])

    def interact(self, PARAM):
        self.set_object(PARAM["object"])
        self.setup(PARAM)
        self.interact_on_Object(self.Object)

    @abstractmethod
    def interact_on_Object(self, Object):
        pass

    def set_out(self, PARAM):
        self.OP_OUT = PARAM

    def finish(self, store_path):
        # store
        pass