import re
from .base import *


class AuthentationServ:
    def sign_in(self, email, password):
        # pass data to data access object to check for valid user
        obj = LoginDao.sign_in(email=email, password=password)
        if len(obj) == 1:
            data = {"email": email, "id": obj[0].id}
            # Generate and return jwt token
            return True, generate_token(data=data)
        return False, "Failed Sign in"

    def sign_up(self, email, password):
        try:
            # check if user is already persent
            boolean, msg = self.sign_in(email=email, password=password)
            # if yes return 'user already present in database'
            if boolean:
                return False, "user already present in database"
            # if not send the data to data access layer to insert it into database
            return LoginDao.sign_up(email=email, password=password)
        except Exception as error:
            return False, error
