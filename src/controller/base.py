from packages.packages import MethodView, Draft7Validator, json, jsonify, request
from utils.auth import (
    generate_token,
    decode_token,
)
from services.__init__ import *


def isValidationError(dataInstance, schema):
    """
    Checks for Errors in json schema of `dataInstance`.\n
    """

    GereralSchemas = Draft7Validator(schema)
    validationErrors = []
    for error in sorted(GereralSchemas.iter_errors(dataInstance), key=str):
        validationErrors.append(error.message)
    if not validationErrors:
        return True
    return False


def successRes(msg=None, key=None, value=None):
    """
    Takes string message and key value and
    """
    out = {"status": "success", "message": msg if msg else "Success Msg"}
    if key and value:
        out.update({"data": {key: value}})
    return jsonify(out)


def failureRes(msg=None, errors=None):
    """
    Takes two string(i.e. `msg` and `errors` ) as input and converts it into jsonified string.\n
    Use this function in case of failure.
    """
    out = {"status": "failure", "message": msg if msg else "Failure Msg"}
    if errors:
        out.update({"errors": errors})
    return jsonify(out)


def getData(request):
    """
    Extracts data from request and converts into json data.\n
    >>> getData(request)
    {'key': 'value'}
    """
    try:
        # print(request.form)
        return json.loads(request.data)
    except Exception as error:
        print(error)
        return None


def custom(set_cookies):
    response = make_response()
    for key in set_cookies.keys():
        response.set_cookie(key, set_cookies[key], httponly=True)
