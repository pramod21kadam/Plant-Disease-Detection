from flask_pymongo import PyMongo


class Database:
    __shared_instance = None

    @staticmethod
    def getinstance():
        if Database.__shared_instance == None:
            raise Exception("No instance created")
        else:
            return Database.__shared_instance

    def __init__(self, app):
        if Database.__shared_instance == None:
            self.mongo = PyMongo(app)
            Database.__shared_instance = self
