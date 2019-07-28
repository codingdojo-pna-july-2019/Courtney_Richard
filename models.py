from sqlalchemy.sql import func
from config import db
from sqlalchemy import create_engine, Column, Integer, String, text
# Models holds our classes to make the database in SQLALchemy

attendees_table = db.Table('attendees',
                  db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True ),
                  db.Column('event_id', db.Integer, db.ForeignKey('event.id'), primary_key=True),
                  )
users_message_event_details = db.Table('user_messages',
                  db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True ),
                  db.Column('message_id', db.Integer, db.ForeignKey('message.id'), primary_key=True),
                  )

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
    users_that_attend_events = db.relationship('Event', lazy = 'dynamic', secondary = attendees_table)
    messages_who_have_users = db.relationship('Message', secondary = users_message_event_details)
    

class Event(db.Model):
    __Tablename__ = "events"
    id = db.Column(db.Integer, primary_key=True)
    event_title = db.Column(db.String(100))
    date = db.Column(db.String(8))
    time = db.Column(db.String(12))
    location = db.Column(db.String(100))
    information = db.Column(db.TEXT)
    creator_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    author = db.relationship('User', foreign_keys=[creator_id], backref="user_messages", cascade="all")
    events_that_have_attendees = db.relationship('User', lazy = 'dynamic', secondary = attendees_table)


class Message(db.Model):
    __Tablename__ = "messages"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.TEXT)
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(db.DateTime, server_default=func.now(), onupdate=func.now())
    user_who_messages = db.relationship('User', secondary = users_message_event_details)





