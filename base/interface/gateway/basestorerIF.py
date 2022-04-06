import os
from abc import ABC, abstractmethod
from base.interface.surface.IO.basestorer import NpStorer, PickleStorer, H5pyStorer, ZarrStorer

class BaseStorerIF(ABC):
    @abstractmethod
    def set_storer(self, DATA_PATH: str):
        pass

class StorerIF(BaseStorerIF):
    def __init__(self, DATA_PATH: str):
        self.DATA_PATH = DATA_PATH
        self.set_storer(DATA_PATH)

    @classmethod
    def from_param(cls, PARAM):
        return cls(PARAM["path"])

    @classmethod
    def from_dir(cls, dir, name, ext):
        return cls(os.path.join(dir, name + ext))
    
    def set_storer(self, DATA_PATH: str):
        if DATA_PATH.endswith(".h5"):
            self.storer = H5pyStorer()
        elif DATA_PATH.endswith(".zarr"):
            self.storer = ZarrStorer()
        elif DATA_PATH.endswith(".npy"):
            self.storer = NpStorer()
        elif DATA_PATH.endswith(".pickle"):
            self.storer = PickleStorer()
        else:
            raise NotImplementedError(f"{DATA_PATH} not implemented")

#------------------------------------------------------------------------------
class DataStorerIF(StorerIF):
    def store(self, obj):
        self.storer.store(self.DATA_PATH, obj)

class DictStorerIF(StorerIF):    
    def store_arg(self, arg, val):
        self.storer.store_arg(self.DATA_PATH, arg, val)

    def store_dict_args(self, DArgs, keys=None):
        if keys is not None:
            DStore = {key: DArgs.__dict__[key] for key in keys}
        else:
            DStore = DArgs
        self.storer.store_dict_args(self.DATA_PATH, DStore)

#------------------------------------------------------------------------------

class ObjectStorerIF(ABC):
    @abstractmethod
    def set_param(self, PARAM):
        pass
    @abstractmethod
    def store(self):
        pass