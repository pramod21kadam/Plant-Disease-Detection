from .base import *
from schemas.loginSchema import *
from flask import make_response


class SigninCtrl(MethodView):
    """
    Sign in controller user processes post request only.
    If valid email id and password are provided generates new jwt tokes as response.
    """

    def post(self):
        try:
            # get payload from request
            payload = request.form

            # Validate it with Schema
            if isValidationError(payload, loginSchema.post):
                # pass the payload data to service layer for provessing
                boolean, msg = AuthentationServ().sign_in(
                    payload["email"], payload["password"]
                )
                if boolean:
                    resp = make_response(successRes(msg="Successfully logged in"))
                    # set json as cookies
                    resp.set_cookie(key="x-access-token", value=msg, httponly=True)
                    return resp, 200
                # return failure message on unsuccessful execution
                # response consist of jsonified object and status code
                return failureRes(msg=msg), 400
            return failureRes(msg="Invalid data format"), 400
        except Exception as error:
            return failureRes(f"{error}"), 500
