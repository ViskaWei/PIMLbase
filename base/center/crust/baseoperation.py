import numpy as np

from abc import ABC, abstractmethod
from .basemodel import BaseModel
from base.center.core.basesampler import SamplerBuilder

class BaseOperation(ABC):
    """ Base class for Process. """
    @abstractmethod
    def perform(self, data):
        pass

class BaseModelOperation(BaseOperation):
    def __init__(self, MODEL) -> None:
        self.model: BaseModel = self.set_model(MODEL["type"])
        if "param" in MODEL:
            self.model.set_model_param(MODEL["param"])
        else:
            self.model.set_model_param()

    @abstractmethod
    def set_model(self, model_type) -> BaseModel:
        pass

    def perform(self, data):
        return self.model.apply(data)

class LogOperation(BaseOperation):
    def perform(self, flux):
        return np.log(flux)

class SelectOperation(BaseOperation):
    """ class for selective process. """
    def __init__(self, IdxSelected) -> None:
        self.IdxSelected = IdxSelected

    def perform(self, data):
        return data[self.IdxSelected, ...]

class SplitOperation(BaseOperation):
    """ class for splitting data. """
    def __init__(self, rng) -> None:
        self.rng = rng
        self.split_idxs = None

    def get_split_idxs(self, data):
        if (np.min(data) <= self.rng[0]) and (np.max(data) >= self.rng[1]):
            self.split_idxs = np.digitize(self.rng, data)
        else:
            self.split_idxs = None
            
    def perform(self, data):
        self.get_split_idxs(data)
        return self.split(data, self.split_idxs)

    def split(self, data, split_idxs):
        if split_idxs is None:
            return data
        else:
            return data[..., split_idxs[0]:split_idxs[1]]

class BuildScalerOperation(BaseOperation):
    def __init__(self, origin, tick=1) -> None:
        self.origin = origin
        self.tick = tick

    def get_scalers(self):
        self.scaler = lambda x: (x - self.origin) / self.tick
        self.rescaler = lambda x: x * self.tick + self.origin

    def perform(self, coord):
        self.get_scalers()
        return self.scaler(coord)

class SamplingOperation(BaseOperation):
    def __init__(self, method):
        self.method = method
    
    def perform(self, ndim):
        builder = SamplerBuilder(ndim)
        sampler = builder.build(self.method)
        return sampler