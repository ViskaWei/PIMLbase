import h5py
import zarr
import pickle
import numpy as np
from abc import ABC, abstractmethod

class BaseStorer(ABC):
    """ Base class for all data loaders. """
    @abstractmethod
    def store(self, path, data):
        pass

class PickleStorer(BaseStorer):
    def store(self, PATH, val):
        with open(PATH, 'wb') as f:
            pickle.dump(val, f, pickle.HIGHEST_PROTOCOL)

class NpStorer(BaseStorer):
    def store(self, PATH, val):
        np.save(PATH, val)


class BaseDictStorer(ABC):
    @abstractmethod
    def store_arg(self, PATH, arg, val):
        pass

    @abstractmethod
    def store_dict_args(self, PATH, DArgs):
        pass

class DictStorer(BaseDictStorer):
    @staticmethod
    def is_arg(f, arg):
        return arg in f.keys()

class H5pyStorer(DictStorer):
    def store_arg(self, PATH, arg, val):
        with h5py.File(PATH, 'a') as f:
            self.store(arg, val, f)

    def store_dict_args(self, PATH, DArgs):
        with h5py.File(PATH, 'w') as f:    
            for arg, val in DArgs.items():
                self.store(arg, val, f)
                
    def store(self, arg, val, f):
        val_shape = val.shape if isinstance(val, np.ndarray) else None
        f.create_dataset(arg, data=val, shape=val_shape)

class ZarrStorer(DictStorer):
    def store_arg(self, PATH, arg, val):
        with zarr.open(PATH, 'a') as f:
            pass
    
    def store_dict_args(self, PATH, DArgs):
        with zarr.open(PATH, 'w') as f:
            pass

