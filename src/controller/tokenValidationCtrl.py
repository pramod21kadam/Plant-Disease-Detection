from .base import *
from database.database import Database


class TokenValidationCtrl(MethodView):
    """
    contorller validates the token.
    """

    def post(self):
        response = request.form
        if (response != None) and ("x-access-token" in response):
            token = decode_token(response["x-access-token"])
            if token and ("email" in token):
                # email is present in it.
                email = token["email"]
                mongo = Database.getinstance().mongo
                if mongo.db.Users.find_one({"email": email}):
                    return successRes(msg="Valid token"), 200

        return failureRes(msg="Invalid or missing token"), 400
