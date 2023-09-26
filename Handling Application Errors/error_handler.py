
from flask import Flask, render_template, abort


app = Flask(__name__)


@app.errorhandler(400)
def bad_request(error):
	return "<h2> Bad request handling!!!!!!!! </h2>"

@app.errorhandler(401)
def unauthorised(error):
	return "<h2> handling unauthorised error</h2>"

@app.errorhandler(403)
def forbidden(error):
	return "<h2> handling Forbidden error</h2>"

@app.errorhandler(404)
def not_found(error):
    return '<h2> Not Found error handling!!!!!!!!!! </h2>'

@app.errorhandler(406)
def not_acceptable(error):
    return '<h2> Not Acceptable error handling!!!!!!!!!! </h2>'

@app.errorhandler(415)
def unsupported_media_type(error):
    return '<h2> Unsupported Media Type error handling!!!!!!!!!! </h2>'

@app.errorhandler(429)
def too_many_request(error):
    return '<h2> Too Many Requests error handling!!!!!!!!!! </h2>'

@app.errorhandler(500)
def internal_server_error(error):
    return '<h2> Internal Server Error error handling!!!!!!!!!! </h2>'










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