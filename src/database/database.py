from flask_pymongo import PyMongo


class Database:
    """
    Singleton class for connecting with mongodb database.
    """

    __shared_instance = None  # variable to hold instance of class

    @staticmethod
    def getinstance():
        """
        Static function returns the orignal instance created.
        If no instance was created Exception "No instance created" is raised.
        """
        if Database.__shared_instance == None:
            raise Exception("No instance created")
        else:
            return Database.__shared_instance

    def __init__(self, app):
        """
        Establish connection with mongodb server with uri.
        """
        if Database.__shared_instance == None:
            self.mongo = PyMongo(app)
            Database.__shared_instance = self
