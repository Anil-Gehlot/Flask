# 1.A Minimal Application


# importing the flask class 
from flask import Flask

# creating instancce of Flask class. this is neede so that flask knows where to look resources such as templates and static files.
app = Flask(__name__)


# by route we tell to flask  what url should be trigger.  and the hello function returns the message we want to display to user.
@app.route('/')
def helloo():
    return "hello Duniya!!!!"

 #  to run this application:  flask --app appName run
                      # Eg:   flask --app flask_document.py run

