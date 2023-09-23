


'''

Flask class provides the redirect() function which redirects the user to some specified URL with the specified status code.

 	An HTTP status code is a response from the server to the request of the browser. When we visit a website, a request is sent to the server,
 	and the server then responds to the browser's request with a three-digit code: the HTTP status code. This status code also represents the error.

'''

from flask import Flask,abort, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
	return render_template("home.html")



@app.route('/login/')
def login():
	return render_template('login.html')



@app.route('/success/')
def success():
	return "logged in suucessfully"



'''@app.route('/validate', methods=["POST"])
def validate():
	if request.method=="POST" and request.form['pass']=='jtp':
		return redirect(url_for("success"))
	return redirect(url_for('login'))'''



@app.route('/validate/', methods=["POST"])
def validate():
	if request.method=="POST" and request.form['pass']=='jtp':
		return redirect(url_for("success"))
	else:
		# abort(400) 	# Bad Request
		# abort(401)		# Unauthorized
		# abort(403)		# Forbidden
		# abort(404)		# Not Found
		# abort(406)		# Not Acceptable
		# abort(415)		# Unsupported Media Type
		# abort(429)		# Too Many Requests
		abort(500)

'''
In the /login route, the abort(401) function is used to trigger a 401 HTTP error, which signifies "access denied." 
This means that anyone trying to access the /login route will receive a 401 error.
'''


if __name__=="__main__":
	app.run(debug=True)