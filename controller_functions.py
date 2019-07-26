


import re
from flask_bcrypt import Bcrypt  
from flask import Flask, render_template, redirect, request, flash, session	# we now need fewer imports because we're not doing everything in this file!
# if we need to work with the database, we'll need those imports:   
from config import db
from models import User, Event #whatever classes we need to import from the model file
from config import app


bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

# home_page
def home():
    
    return render_template('index.html')


#  add a user from home page need to add validation
def add_user():
    is_valid = True
    if len(request.form["fname"]) < 2:
        is_valid = False
        flash("Please enter a valid first name")

    if len(request.form["lname"]) < 2:
        is_valid = False
        flash("Please enter a valid last name")
    if not EMAIL_REGEX.match(request.form["email"]):    
        is_valid = False
        flash("Invalid email address!")
    if len(request.form["password"]) < 8:
        is_valid = False
        flash("Password should be at least 8 characters")
    if request.form['password'] != request.form['confirm_pass']:
        is_valid = False
        flash("Passwords need to match")
    if is_valid:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        new_instance_of_user = User(first_name = request.form['fname'],
                                    last_name = request.form['lname'],
                                    email = request.form['email'], 
                                    password = pw_hash)
     
        db.session.add(new_instance_of_user)
        db.session.commit()
    return redirect("/")


#login route
def login():
    instance_of_user = User.query.filter_by(email=request.form['email']).first()
    if instance_of_user:
        pw = bcrypt.check_password_hash(instance_of_user.password, request.form['password'])
        if pw:
            session['uid'] = instance_of_user.id
            session['greetings'] = instance_of_user.first_name
            return redirect('/homepage')
    else:
        flash('Invalid user name or password')
        return redirect('/')


# kills session
def logout():
    session.clear()
    return redirect("/")


# adds a new event
def new():
    
    return render_template ("add_new_event_page.html")


# adds an event to the db
    # create form to add new events in
    # create validations that check for unfilled requests and for dublicate events
    # add event to the db
def addnew():    
    # need to query the database for current events - doesnt need to query - Richard*
    is_valid = True
    if len(request.form['EventName']) < 2:
        is_valid = False
        flash('Has to be more than 2 characters')
    if len(request.form['Location']) < 8:
        is_valid = False
        flash('Please be more specific Address, City, State, Zip')
    if len(request.form['Time']) < 5:
        is_valid = False
        flash('Please enter a valid time')
    if len(request.form['Info']) < 5:
        is_valid = False
        flash('Please enter a little more info about this event Thanks! Arrigato')
    if is_valid:
        adding_event = Event(event_title = request.form['EventName'],
                                    location = request.form['Location'],
                                        date = request.form['Date'],
                                        time = request.form['Time'],
                                    information = request.form['Info'])
        db.session.add(adding_event)
        db.session.commit()
        flash('Success')
        return redirect("/new")
    return redirect("/new")


# user landing page closest event & upcomeing events
def homepage():

    # we need to query the database and display info from events then,
    # add it to the render so we can display it
    # things to query for are "events name", "Location", "number of attendees"
    # and future events

    return render_template("user_home_page.html")