



from flask import Flask

app = Flask('__name___')

@app.route('/')
def index():
	return "index page"

@app.route('/hello')
def next():
	# print("hekfdnfsdhf")
	return "hello page"



'''

 @app.route : this decorater bind a python function to a specific url in web page 

 @app.route('/'): it is binding the index fuction to the root url , which is usually 
 		the main page of website.

@app.route('/hello'): binds the next function to url '/hello' , which is another page.

when a user visits there urls , the binded function will display its reurned value. 



'''