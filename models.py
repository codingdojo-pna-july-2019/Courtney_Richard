from sqlalchemy.sql import func
from config import db
# Models holds our classes to make the database in SQLALchemy

# User registration class
class User(db.Model):
    __Tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    password = db.Column(db.String(200))
    email = db.Column(db.String(100))
    security_answer1 = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())

class Event(db.Model):
    __Tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(100))
    date = db.Column(db.DATE)
    time = db.Column(db.TIME)
    location = db.Column(db.String(100))
    information = db.Column(db.TEXT)
