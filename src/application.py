from packages.packages import Flask
from blueprints.api import api
class Metaclass(type):
    __instance = None
    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Metaclass, cls).__call__(*args, **kwargs)   
        return cls.__instance

class App(metaclass=Metaclass):
    def __new__(self, config_file = None):
        self.instance = Flask(__name__)
        self.instance.config.from_pyfile('config.cfg')
        self.instance.register_blueprint(api, url_prefix='/api')
        return self.instance