

'''

 In the client-server architecture, the request object contains all the data that is sent from the client to the server. 
 we can retrieve the data at the server side using the HTTP methods.


 Request object and its important attributes: 
    1.  Form :  It is the dictionary object which contains the key-value pair of form parameters and their values.
 	2	args	It is parsed from the URL. It is the part of the URL which is specified in the URL after question mark (?).
 	3	Cookies	It is the dictionary object containing cookie names and the values. It is saved at the client-side to track the user session.
 	4	files	It contains the data related to the uploaded file.
 	5	method	It is the current request method (get or post).


'''


from flask import Flask, render_template ,url_for, request
from markupsafe import escape 

app = Flask(__name__)

@app.route('/')
def customer():
	return render_template('customer.html')


@app.post('/success/')
def print_data():
	result = request.form
	name = request.form['name']
	return render_template("result_data.html", result=result, name=name)


if __name__ == "__main__":
	app.run(debug=True)

