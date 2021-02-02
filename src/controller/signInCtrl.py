from .base import *
from schemas.loginSchema import *

class SigninCtrl(MethodView):
    '''
        Sign in controller user
    '''
    def post(self):
        try:
            # get payload from request
            payload = getData(request)
            # Validate it with Schema
            if isValidationError(payload, loginSchema.post):
                # pass the payload data to service layer for provessing 
                boolean, msg = AuthentationServ().sign_in(payload['email'], payload['password'])
                if boolean:
                    return successRes(msg='Successfully logged in', key='x-access-token', value=msg), 200
                # return failure message on unsuccessful execution
                # response consist of jsonified object and status code
                return failureRes(msg=msg), 400                
            return failureRes(msg="Imporper request data"), 400
        except Exception as error:
            return failureRes(f"{error}"), 500