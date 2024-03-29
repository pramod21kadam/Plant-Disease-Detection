from packages.packages import Flask, json, request, wraps, jsonify, jwt

"""
   Implemented singelton class for application 
"""


class Metaclass(type):
    __instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Metaclass, cls).__call__(*args, **kwargs)
        return cls.__instance


class App(metaclass=Metaclass):
    def __new__(cls):
        cls.instance = Flask(__name__)
        cls.instance.config.from_pyfile("config.cfg")
        return cls.instance
