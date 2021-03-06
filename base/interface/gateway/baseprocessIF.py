from abc import ABC, abstractmethod
from ...center.crust.baseprocess import Process
from .baseloaderIF import ObjectLoaderIF
from .basestorerIF import ObjectStorerIF
from .baseparamIF import ParamIF

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
        self.Param: ParamIF = None        
        self.Loader : ObjectLoaderIF = None
        self.Storer : ObjectStorerIF = None
        self.Process: Process = None 

    def set_object(self, OBJECT_PARAM):
        self.Loader.set_param(OBJECT_PARAM)
        self.Object = self.Loader.load()

    def set_param(self, PARAM):
        self.Param.set_param(PARAM)
        self.PARAM = self.Param.get()

    def interact(self, PARAM={}):
        self.set_param(PARAM)
        self.set_object(self.PARAM["OBJECT"])
        self.interact_on_Object(self.Object)
    
    def interact_on_Object(self, Object):
        self.Process.set_process(self.PARAM["OP"], self.PARAM["MODEL"], self.PARAM["DATA"])
        self.Process.start(Object)

    def store_out(self, PARAM=None):
        if PARAM is None : PARAM = self.PARAM["out"]
        self.Storer.set_param(PARAM)
        self.Storer.store(self.Object)

    def finish(self, store_path):
        # store
        pass