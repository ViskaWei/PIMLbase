from abc import ABC, abstractmethod

class BaseParamIF(ABC):
    @abstractmethod
    def set_param(self, PARAM):
        pass

    @abstractmethod
    def get(self, PARAM):
        pass

class ParamIF(BaseParamIF):
    def __init__(self):
        self.OBJECT: dict = {}
        self.OP    : dict = {}
        self.MODEL : dict = {}
        self.DATA  : dict = {}
        self.OUT   : dict = {}

    def set_param(self, PARAM):
        pass

    def get(self):
        self.assemble()
        return self.PARAM

    def assemble(self):
        self.PARAM = {
            "OBJECT": self.OBJECT,
            "OP"    : self.OP,
            "MODEL" : self.MODEL,
            "DATA"  : self.DATA,
            "OUT"   : self.OUT
        }

    @staticmethod
    def is_arg(name, args):
        return name in args and args[name] is not None

    @staticmethod
    def get_arg(name, args, old_args=None):
        if name in args and args[name] is not None:
            return args[name]
        else:
            return old_args