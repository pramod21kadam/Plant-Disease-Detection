from packages.packages import (redirect, render_template, url_for)
from application import App
from utils.auth import token_required
app = App()

@app.route('/')
def home():
    return "Home"

@app.route('/user')
@token_required
def user(current_user):
    """
        `current_user` content is passed by @token_required which contains the jwt token information of current user
        Only verified users can access paths which are wrapped by @token_required
    """
    return "Only protected content"

@app.route('/login', methods = ['GET'])
def login():
    return render_template('login.html')