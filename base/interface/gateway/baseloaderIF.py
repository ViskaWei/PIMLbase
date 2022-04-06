import os
from abc import ABC, abstractmethod
from base.interface.surface.IO.baseloader import H5pyLoader, NpLoader, PickleLoader, ZarrLoader

class BaseLoaderIF(ABC):
    @abstractmethod
    def set_loader(self, DATA_PATH):
        pass

class PathLoaderIF(BaseLoaderIF):
    def __init__(self, DATA_PATH):
        self.DATA_PATH = DATA_PATH
        self.set_loader(DATA_PATH)
    
    @classmethod
    def from_dir(cls, dir, name, ext):
        return cls(os.path.join(dir, name + ext))

    def set_loader(self, DATA_PATH: str):
        if DATA_PATH.endswith(".h5"):
            self.loader = H5pyLoader()
        elif DATA_PATH.endswith(".zarr"):
            self.loader = ZarrLoader()
        elif DATA_PATH.endswith(".npy"):
            self.loader = NpLoader()
        elif DATA_PATH.endswith(".pickle"):
            self.loader = PickleLoader()
        else:
            raise NotImplementedError(f"{DATA_PATH} not implemented")

#-----------------------------------------------------------------------------
class DataLoaderIF(PathLoaderIF):
    def load(self):
        return self.loader.load(self.DATA_PATH)

class DictLoaderIF(PathLoaderIF):
    def load_dict_args(self):
        self.keys = self.loader.get_keys(self.DATA_PATH)
        return self.loader.load_dict_args(self.DATA_PATH)

    def load_arg(self, arg):
        return self.loader.load_arg(self.DATA_PATH, arg)
    
    def is_arg(self, arg):
        return self.loader.is_arg(self.DATA_PATH, arg)

#-----------------------------------------------------------------------------
class ObjectLoaderIF(ABC):
    required_attributes = ["loader"]
    @abstractmethod
    def set_param(self, PARAM):
        pass
    @abstractmethod
    def load(self):
        pass

#-----------------------------------------------------------------------------