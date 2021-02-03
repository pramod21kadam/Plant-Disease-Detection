from packages.packages import SQLAlchemy, datetime
from application import App
db = SQLAlchemy(app = App())

class Login(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    email = db.Column(db.String(20), nullable = False)
    password = db.Column(db.String(50), nullable=True)
    created_on = db.Column(db.DateTime, nullable = False)

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.created_on = datetime.now()

db.create_all()