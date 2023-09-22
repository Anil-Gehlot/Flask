'''

 Variable Rules :
			 it is a feature in flask to allow us to create 
         	 dynamic routes and handle different types of data.

'''


from markupsafe import escape
from flask import Flask 

app = Flask(__name__)


@app.route('/user/<username>')
def user_profile(username):
	return f"hello {escape(username)}"


@app.route('/post/<int:post_id>')
def post(post_id):
	return f"post id: {escape(post_id)}"


@app.route('/marks/<float:marks>')
def mark(marks):
	return f'your total marks are :  {escape(marks)}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
	return f"subpath = {escape(subpath)}"


'''
@app.route('/user/<username>') defines a route where the URL includes a variable section indicated by <username>. 
This variable section captures whatever value is provided in the URL and passes it as an argument to the show_user_profile(username) function.

@app.route('/post/<int:post_id>') defines a route where the variable section <int:post_id> specifies that the captured value should be converted to an integer.

@app.route('/path/<path:subpath>') defines a route where the variable section <path:subpath> indicates that the captured value can include slashes ('/') and is used as a path.

@app.route('/marks/<float:marks>') defines a route where the variable section '<float:marks>' indicates that the captured value should be floating value.

'''