from datamodel.master import db, Login
from .base import *
class LoginDao:
    @staticmethod
    def sign_in(email, password):
        """
            Checks for email and password authenticity.\n
            Returns true on successful sugn_in
        """
        try:
            # Query data from database
            # SELECT * FROM login WHERE login.email = email AND login.password = password
            result = db.session.query(Login).\
                filter(Login.email == email).\
                filter(Login.password == password).\
                all()
            return result
        except Exception as error:
            return error

    @staticmethod
    def sign_up(email, password):
        """
            Inserts email and password into database.\n
            Returns True on successful insertion
        """
        try:
            # For new entry in login table create a Login object
            obj = Login(email=email, password=password)
            # insert it into database
            if  base.insert(obj=obj):
                # commit
                if base.commit():
                    return True, 'Successful'
                return False, 'Commit error'
            return False, 'Insert error'
        except Exception as error:
            return False, error

    def get(email):
        return db.session.query(Login).filter( Login.email == email).first()