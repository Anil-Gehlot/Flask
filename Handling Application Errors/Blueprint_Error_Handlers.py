

from flask import jsonify, render_template, Flask, request, abort

app = Flask(__name__)


# at the application level
# not the blueprint level
@app.errorhandler(404)
def page_not_found(e):
    # if a request is in our blog URL space
    if request.path.startswith('/blog/'):
        # we return a custom blog 404 page
        return render_template("index.html"), 404
    else:
        # otherwise we return our generic site-wide 404 page
        return render_template("profile.html"), 404

@app.errorhandler(405)
def method_not_allowed(e):
    # if a request has the wrong method to our API
    if request.path.startswith('/api/'):
        # we return a json saying so
        return jsonify(message="Method Not Allowed"), 405
    else:
        # otherwise we return a generic site-wide 405 page
        return render_template("inherit_template.html"), 405



@app.route("/blog")
def index():
	abort(404)

# @app.route("/api/")
@app.route("/405/")
def index1():
	abort(405)
