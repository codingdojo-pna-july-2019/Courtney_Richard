from flask import Flask,render_template, request, redirect	# any other flask imports needed
from config import app, db
from models import User, Event
import routes
# from models import #classes from models.py file i.e. our database from SQLALchemy





if __name__ == "__main__":
    app.run(debug=True)