from model.master import db, Login
from .base import *
class LoginDao:
    def sign_in(email, password):
        """
            Checks for email and password authenticity.\n
            Returns true on successful sugn_in
        """
        try:
            result = db.session.query(func.count(Login.id)).\
                filter(Login.email == email).\
                filter(Login.password == password).\
                one()
            if result[0] == 1:
                return True
            else:
                return False
        except Exception as error:
            return False

    def sign_up(email, password):
        """
            Inserts email and password into database.\n
            Returns True on successful sign_up
        """
        try:
            if not LoginDao.sign_in(email=email, password=password):
                obj = Login(email=email, password=password)
                if  base.insert(obj=obj):
                    if base.commit():
                        return True
            else:
                return False
        except Exception as error:
            return False

    def get(email):
        return db.session.query(Login).filter( Login.email == email).first()