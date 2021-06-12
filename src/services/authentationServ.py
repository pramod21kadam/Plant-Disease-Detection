import re
from .base import *

from database.database import Database


class AuthentationServ:
    """
    Authentication service includes function related to authetication.
    """

    def sign_in(self, email, password):
        """
        Validates user email id and password.
        """
        mongo = Database.getinstance().mongo
        result = mongo.db.Users.find_one({"email": email, "password": password})
        if result != None:
            return True, generate_token(data={"email": email})
        else:
            return False, "Incorrect email id or password"

    def sign_up(self, email, password):
        """
        Creaets new user account if new email id is provided.
        """
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
