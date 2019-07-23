from flask import render_template, redirect, request	# we now need fewer imports because we're not doing everything in this file!
# if we need to work with the database, we'll need those imports:   
from config import db
from models import User, Event #whatever classes we need to import from the model file



# home_page
def home():
    
    return render_template('index.html')


#  add a user from home page need to add validation
def add_user():

    new_instance_of_user = User(first_name = request.form['fname'],
                                 last_name = request.form['lname'],
                                    email = request.form['email'], 
                                    password = request.form['password'])
    # if (new_instance_of_user.f)
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