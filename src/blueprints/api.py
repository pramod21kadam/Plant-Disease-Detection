from flask import Blueprint
from controller.__init__ import *
from application import App
api = Blueprint('api', __name__,template_folder='templates')

def register_api(view, endpoint, url, pk='id', pk_type='int'):
    view_func = view.as_view(endpoint)
    api.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', 'PATCH', 'PUT', 'DELETE'])
    api.add_url_rule(url, view_func=view_func, methods=['POST', 'OPTIONS'])
    api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func, methods=['GET', 'PATCH', 'PUT', 'DELETE'])
    
register_api(PredictionCtrl, 'prediction', '/predict')
register_api(SignUpCtrl, 'signup', '/signup')
register_api(SigninCtrl, 'signin', '/signin')
App().register_blueprint(api, url_prefix='/api')