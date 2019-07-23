from sqlalchemy.sql import func
from config import db
# Models holds our classes to make the database in SQLALchemy

# User registration class
class User(db.Model):
    __Tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable = False)
    last_name = db.Column(db.String(100), nullable = False)
    password = db.Column(db.String(200), unique = True, nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    security_answer1 = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    events = db.relationship ('Event', backref = 'user', lazy = True)

class Event(db.Model):
    __Tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(100))
    date = db.Column(db.DATE)
    time = db.Column(db.TIME)
    location = db.Column(db.String(100))
    information = db.Column(db.TEXT)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)