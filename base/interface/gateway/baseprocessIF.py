from abc import ABC, abstractmethod
from ...center.crust.baseprocess import Process
from .baseloaderIF import ObjectLoaderIF
from .basestorerIF import BaseStorerIF
from .baseparamIF import BaseParamIF

class BaseProcessIF(ABC):
    """ Base class for Process interface for data. """
    @abstractmethod
    def set_object(self, OBJECT):
        pass
    @abstractmethod
    def set_param(self, OP_PARAM):
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
        
        self.paramIF: BaseParamIF = None        
        self.Loader : ObjectLoaderIF = None
        self.Storer : BaseStorerIF = None
        self.Process: Process = None 

    def set_object(self, OBJECT_PARAM):
        self.Loader.set_param(OBJECT_PARAM)
        self.Object = self.Loader.load()

    def set_param(self, PARAM):
        self.paramIF.set_param(PARAM)
        self.PARAM = self.paramIF.get()

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