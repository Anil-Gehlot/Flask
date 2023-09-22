
'''

HTTP methods:

	By default, a route only answers to GET requests. You can use the methods argument of the route() decorator to handle different HTTP methods.
'''



# 	1.Handling Multiple HTTP Methods in One Function:

from flask import request,Flask

app = Flask(__name__)

@app.route('/login/', methods=['GET', 'POST'])
def login():
	if request.method=='POST':
		return "POST method"
	else:
		return "GET method"

# In the example provided, the '/login' route handles both GET and POST requests. Inside the login() function, 
# it checks the request method using request.method to determine whether it should show the login form or process the login data.



# 2.Separate Functions for Different Methods:

@app.get('/login_get/')
def do_login():
	return "get method for login"

@app.post('/login_post/')
def show_form():
	return "post method for login"

# You can also separate views for different HTTP methods into different functions. Flask provides a shortcut for decorating such routes with @app.get(), @app.post(), and so on, for each common HTTP method.

