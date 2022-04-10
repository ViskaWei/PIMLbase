
from abc import ABC, abstractmethod

class BasePipeline(ABC):
    """ Base class for Pipeline. """
    @abstractmethod
    def run(self):
        pass

class ProcessPipeline(BasePipeline):
    def run(self, PARAM, Object) -> None:
        for process in self.process_list:
                process.set_process(PARAM)
                process.start(Object)
                process.finish(Object)