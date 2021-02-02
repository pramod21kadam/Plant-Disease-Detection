from packages.packages import MethodView, Draft7Validator, json, jsonify, request
from utils.auth import token_required, get_current_user, check_for_token, generate_token
from services.__init__ import *
def isValidationError(dataInstance, schema):
    """
        Checks for Errors in json schema of `dataInstance`.\n
        outputs:\n
            \t`True` if error and `False` if no error.
    """

    GereralSchemas = Draft7Validator(schema)
    validationErrors = []
    for error in sorted(GereralSchemas.iter_errors(dataInstance), key=str):
        validationErrors.append(error.message)
    if not validationErrors:
        return False
    return validationErrors

def successRes(msg=None, key=None, value=None):
    """
        Takes string message and key value and 
    """
    out = {"status": 'success',
           "message": msg if msg else 'Success Msg'}
    if key and value:
        out.update({"data": {
            key: value
        }
        })
    return jsonify(out)

def failureRes(msg=None, errors=None):
    """
        Takes two string(i.e. `msg` and `errors` ) as input and converts it into jsonified string.\n
        Use this function in case of failure. 
    """
    out = {
        "status": 'failure',
        "message": msg if msg else 'Failure Msg'
    }
    if errors:
        out.update({'errors': errors})
    return jsonify(out)

def getData(request):
    """
        Extracts data from request and converts into json data.\n
        >>> getData(request)
        {'key': 'value'}
    """
    try:
        return json.loads(request.data)
    except Exception as e:
        print(e)
        return None