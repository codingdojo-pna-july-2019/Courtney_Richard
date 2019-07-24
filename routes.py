from config import app
from controller_functions import home, add_user, homepage, login, logout #importing all the functions associated with the routes we're writing

app.add_url_rule("/", view_func=home)
app.add_url_rule("/register", view_func=add_user, methods=["POST"])
app.add_url_rule("/login", view_func=login, methods=["POST"])
app.add_url_rule("/logout",view_func=logout)
app.add_url_rule("/homepage", view_func=homepage )