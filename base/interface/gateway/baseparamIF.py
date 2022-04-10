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

class MultiParamIF(ParamIF):
    def __init__(self):
        super().__init__()
        self.paramIF_list:ParamIF =[]

    def set_param(self, PARAM):
        for paramIF in self.paramIF_list:
            paramIF.set_param(PARAM)
            self.merge(paramIF)

    def merge(self, new_dict):
        self.OBJECT.update(new_dict.OBJECT)
        self.OP    .update(new_dict.OP)
        self.MODEL .update(new_dict.MODEL)
        self.DATA  .update(new_dict.DATA)
        self.OUT   .update(new_dict.OUT)

