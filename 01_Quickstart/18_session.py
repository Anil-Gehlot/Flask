'''
session is the time bw the login and logout of a user on a server.

session is stored on server side in temporary directoty.

har session ki id hoti he jo cookie me top par store hoti he, iski help se hi server ko session ke bare me pata chalta he.

'''




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

@app.route("/profile/")
def profile():
	if 'name' in session:
		name = session['name']
		return render_template("profile.html", name=name)
	else:
		msg = "login first"
		return render_template("login_form.html", msg=msg)


'''

#  Session:	The session can be defined as the duration for which a user logs into the server and logs out. 

The data which is used to track this session is stored into the temporary directory on the server.

The session data is stored on the top of cookies and signed by the server cryptographically.

In the flask, a session object is used to track the session data which is a dictionary object 
that contains a key-value pair of the session variables and their associated values.


'''