

from flask import Flask, request, redirect, url_for, abort, render_template
import logging 


# ---------------------------------------------------------------------
#  Basic Configuration
'''from logging.config import dictConfig


dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})'''
# ---------------------------------------------------------------------


app = Flask(__name__)


users = {
    'anil': '9644',
    'lokesh': '1045',
    'harsh' : '5736'
}


# logging filed
logging.basicConfig(filename = "userLogin.log")



@app.route("/")
def index():
    return render_template("login.html")

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if the username exists and the password is correct
        if username in users and users[username] == password:

            # Successful login
            app.logger.info('%s logged in successfully with username : ', username )    # to write in log files
            return f'Hello, {username}! You are logged in.'
        else:
            # Failed login
            app.logger.info('%s failed to log in with username : ',username)    # to write in log files
            abort(500)

@app.route("/anilg")
def anilg():
    return "anilg in the house......!!!!"


if __name__ == '__main__':
    app.run(debug=True)
