from .base import *

class Metaclass(type):
    __instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Metaclass, cls).__call__(*args, **kwargs)   
        return cls.__instance

class Model:
    def __new__(self):
        self.instance = load_model('assets/mobile_net_9756999611854553.h5')
        return self.instance
