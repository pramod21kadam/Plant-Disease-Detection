import re
from .base import *

from database.database import Database


class AuthentationServ:
    def sign_in(self, email, password):
        # pass data to data access object to check for valid user
        mongo = Database.getinstance().mongo
        result = mongo.db.Users.find_one({"email": email, "password": password})
        if result != None:
            return True, generate_token(data={"email": email})
        else:
            return False, "Incorrect email id or password"

    def sign_up(self, email, password):
        try:
            mongo = Database.getinstance().mongo
            if mongo.db.Users.find_one({"email": email}) == None:
                result = mongo.db.Users.insert_one(
                    {"email": email, "password": password}
                )
                return result != None, None
            else:
                return False, "user already present in database"
        except Exception as err:
            return False, err
