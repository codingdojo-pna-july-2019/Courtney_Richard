from config import app
from controller_functions import home, add_user, homepage, login, logout, new, addnew, new_attendee, event, create_msg, delete, search
#importing all the functions associated with the routes we're writing

app.add_url_rule("/", view_func=home)
app.add_url_rule("/register", view_func=add_user, methods=["POST"])
app.add_url_rule("/login", view_func=login, methods=["POST"])
app.add_url_rule("/logout",view_func=logout)
app.add_url_rule("/new",view_func=new)
app.add_url_rule("/addnew", view_func=addnew, methods=["POST"])
app.add_url_rule("/homepage", view_func=homepage)
app.add_url_rule("/new_attendee", view_func=new_attendee, methods=["POST"])
# app.add_url_rule("/get_event", view_func=get_event, methods=["POST"])
app.add_url_rule("/event/<id>", view_func=event)
app.add_url_rule("/create_msg", view_func=create_msg, methods=['POST'])
app.add_url_rule("/delete", view_func=delete, methods=['POST'])
app.add_url_rule("/search", view_func=search)