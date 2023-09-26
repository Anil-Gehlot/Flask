
# WSGI is a specification that describes the communication
# between web servers and Python web applications or frameworks







from flask import Flask, render_template, abort
from flask import json

# Werkzeug is a comprehensive WSGI web application library.
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


# ****it generate the error name in dictionary form.****
@app.errorhandler(HTTPException)
def handle_exception(error):

    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = error.get_response()

    # replace the body with JSON
    response.data = json.dumps({
        "code": error.code,
        "name": error.name,
        "description": error.description,
    })
    response.content_type = "application/json"
    return response








@app.route("/bad_request/")
def bad_request():
	abort(400)	# Bad Request

@app.route("/unauthorised/")
def unauthorised():
	abort(401)

@app.route("/forbidden/")
def forbidden():
	abort(403)

@app.route("/")
def index():
	return render_template("index.html")  #404

@app.route("/not_acceptable/")
def not_acceptable():
	abort(406)

@app.route("/unsupported_media_type/")
def unsupported_media_type():
	abort(415)
 	
@app.route("/too_many_request/")
def too_many_request():
	abort(429)
 	
@app.route("/internal_server_error/")
def internal_server_error():
	abort(500)