from sqlalchemy.sql import func
from config import db
from sqlalchemy import create_engine, Column, Integer, String, text
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

class Event(db.Model):
    __Tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(100))
    date = db.Column(db.DateTime)
    time = db.Column(db.DateTime)
    location = db.Column(db.String(100))
    information = db.Column(db.TEXT)


class Message(db.Model):
    __Tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.TEXT)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())



