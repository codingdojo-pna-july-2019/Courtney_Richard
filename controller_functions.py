import re
from flask_bcrypt import Bcrypt  
from flask import Flask, render_template, redirect, request, flash	# we now need fewer imports because we're not doing everything in this file!
# if we need to work with the database, we'll need those imports:   
from config import db
from models import User, Event #whatever classes we need to import from the model file



bcrypt = Bcrypt()
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
                                    password = pw_hash,
                                    confirm_pass = request.form['confirm_pass'])
     
    db.session.add(new_instance_of_user)
    db.session.commit()
    return redirect("/")


# user landing page closest event & upcomeing events
def homepage():

    # we need to query the database and display info from events then,
    # add it to the render so we can display it
    # things to query for are "events name", "Location", "number of attendees"
    # and future events

    return render_template("user_home_page.html")