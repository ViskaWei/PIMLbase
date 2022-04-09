from abc import ABC, abstractmethod
from base.center.core.baseinterpbuilder import RBFInterpBuilder
from base.interface.gateway.basestorerIF import DataStorerIF

class BaseModel(ABC):
    @abstractmethod
    def set_model_param(self, param):
        pass
    @abstractmethod
    def apply(self):
        pass



class RBFInterpBuilderModel(BaseModel):
    def set_model_param(self, kernel="gaussian", epsilon=0.5):
        self.builder = RBFInterpBuilder(kernel, epsilon) 

    def apply(self, coord, value):
        self.builder.build(coord, value)
        def interpolator(eval_coord):
            if eval_coord.ndim == 1:
                return self.builder.base_interpolator([eval_coord])[0]
            else:
                return self.builder.base_interpolator(eval_coord)
        return interpolator

    def store(self, DATA_DIR, name="interp"):
        self.storer = DataStorerIF.from_dir(DATA_DIR, name, ".pickle")
        self.storer.store(self.builder.base_interpolator)