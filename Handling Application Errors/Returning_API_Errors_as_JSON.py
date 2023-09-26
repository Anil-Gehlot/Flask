

# returning errors in json forms.



from flask import abort, jsonify, Flask, render_template

app = Flask(__name__)



@app.errorhandler(404)
def resource_not_found(e):
    return jsonify(error=str(e))




@app.route("/")
def index():
	return render_template("index.html")  #404

