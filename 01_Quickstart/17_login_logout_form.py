


from flask import Flask, render_template, url_for, request, session

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = "ANIL"

@app.route("/")
def index():
	return render_template("login_form.html")

@app.route("/logout/")
def logout():
	session.pop("name",None)
	return render_template('login_form.html')

@app.post("/login/")
def login():

	username = request.form["username"]
	password = request.form["password"]

	if (username == "anil" and password=="9644"):
		# return render_template("success_form.html",username = username)
		
		# creating a session variable
		session['name']=username
		return render_template("success_form.html", name=username)


	else:
		msg = "Invalid username/password"
		return render_template("login_form.html", msg = msg)