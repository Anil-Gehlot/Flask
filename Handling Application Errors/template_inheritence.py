
from flask import abort, render_template, request, Flask


app = Flask(__name__)

@app.route("/")
def root():
    # return render_template("profile.html")
    return render_template("inherit_template.html")

