from flask import Blueprint
from flask_cors import CORS
from controller.__init__ import *
from application import App
from database.database import Database

api = Blueprint("api", __name__, template_folder="templates")
# enabling cors on api.
CORS(api)


def register_api(
    view,
    endpoint,
    url,
    pk="id",
    pk_type="int",
    methods=["GET", "PATCH", "PUT", "DELETE", "POST"],
):
    """
    Function to register API endpoints.
    """
    view_func = view.as_view(endpoint)
    # api.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', 'PATCH', 'PUT', 'DELETE'])
    api.add_url_rule(url, view_func=view_func, methods=["POST", "OPTIONS"])
    # api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func, methods=['GET', 'PATCH', 'PUT', 'DELETE'])


register_api(PredictionCtrl, "prediction", "/predict", methods=["POST"])
register_api(SignUpCtrl, "signup", "/signup", methods=["POST"])
register_api(SigninCtrl, "signin", "/signin", methods=["POST"])
register_api(TokenValidationCtrl, "validate-token", "/validate-token", methods=["POST"])

#
Database(App())

App().register_blueprint(api, url_prefix="/api")
