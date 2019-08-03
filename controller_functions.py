


from flask_bcrypt import Bcrypt  
from flask import Flask, render_template, redirect, request, flash, session	# we now need fewer imports because we're not doing everything in this file!
# if we need to work with the database, we'll need those imports:   
from config import db
from models import User, Event, Message, attendees_table #whatever classes we need to import from the model file
from config import app
import re


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
    events = Event.query.all()
    return render_template ("add_new_event_page.html", all_events = events)


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
    if len(request.form['Time']) < 2:
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
                                        creator_id = session['uid'],
                                    information = request.form['Info'])
        db.session.add(adding_event)
        db.session.commit()
        flash('Success')
        return redirect("/new")
    return redirect("/new")


# add a atendee
def new_attendee():

    # if (request.form['Attend'] == "Attend")
    existing_event = Event.query.get(request.form['e_id'])
    print(existing_event)
    user_wanting_to_attend = User.query.get(session['uid'])
    print(user_wanting_to_attend)
    user_wanting_to_attend.users_that_attend_events.append(existing_event)
    db.session.commit()
        # request.form['Attend'] = "Unattend"
    return redirect("/homepage")


# user landing page closest event & upcomeing events
def homepage():
    events = Event.query.all()
    user = User.query.get(session['uid'])
    user_events = user.users_that_attend_events.all()
    
    return render_template("user_home_page.html", all_events = events, all_events_of_user = user_events)

# notification page where messages are displayed and edited
def event(id):
    user_events = Event.query.get(id)
    get_messages = Message.query.filter_by(event_info = id)
    print(get_messages)
    
    
     #get all users if session not found in this then hide button iwth if statement
    
    return render_template("message_board.html", organize_event = user_events, read_message = get_messages)

def create_msg():
    new_message = Message(content = request.form['msg'], 
                        user_who_created = session['uid'],
                        user_info = session['uid'],
                        event_info = request.form['e_id'])
    

    db.session.add(new_message)
    db.session.commit()

    
    return redirect("/event/" + request.form['e_id'])


#delete message
def delete():
    message_to_delete = Message.query.get(request.form['message_id'])
    # user_associated.user_messages.delete(message_to_delete)
    db.session.delete(message_to_delete)
    db.session.commit()

    return redirect("/event/" + request.form['e_id'])
   

#search feature for ticketmaster api
def search():

    return render_template("search.html")