from flask import render_template, redirect, request	# we now need fewer imports because we're not doing everything in this file!
# if we need to work with the database, we'll need those imports:    
from config import db
from models import User, Event #whatever classes we need to import from the model file


# home_page
def home():
    
    return render_template('index.html')