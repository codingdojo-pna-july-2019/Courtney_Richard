from config import app
from controller_functions import home #importing all the functions associated with the routes we're writing

app.add_url_rule("/", view_func=home)