from packages.packages import wraps, jwt, request, jsonify, timedelta, datetime
from utils.config import config
from dao.loginDao import LoginDao

def token_required(f):
    """
        Decorator function that checks the json web token for authentation and\n
        return the current user login contex to the route
    """
    @wraps(f) 
    def decorated(*args, **kwargs): 
        token = None
        # jwt is passed in the request cookies
        if 'x-access-token' in request.cookies.keys():
            token = request.cookies['x-access-token'] 
        # return 401 if token is not passed 
        if not token: 
            return jsonify({'message' : 'Token is missing !!'}), 401
   
        try: 
            # decoding the payload to fetch the stored details
            data = jwt.decode(token,  config('config.cfg')['SECRET_KEY'])
            current_user = LoginDao.get(email=data['email'])
            if data['id'] != current_user.id:
                return jsonify({ 
                    'message' : 'Token is invalid !!'
                    }), 401
        except Exception as error:
            print(error) 
            return jsonify({ 
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users contex to the routes not to api
        # for api use get_current_user
        return  f(current_user)
    return decorated 

def get_current_user(request):
    """
        Returns current users information from the jwt
    """
    try:
        data = jwt.decode(request.args['x-access-token'],  config('config.cfg')['SECRET_KEY'])
        return data
    except Exception as error:
        return None

def check_for_token(request):
    """
        Checks for token available
    """
    token = None
    if 'x-access-token' in request.args: 
        return True, request.args['x-access-token']
    return False, None

def generate_token(data, expire_time = datetime.utcnow() + timedelta(minutes = 30)):
    """
        Generate jwt tokens
    """
    # expire time is the time for jwt death
    data['exp'] = expire_time
    return jwt.encode(data, config('config.cfg')['SECRET_KEY'])