




from flask import Flask, render_template ,url_for, request
from markupsafe import escape 

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('file_upload_form.html')

@app.post('/success/')
def success():
	file = request.files['file']
	file.save(file.filename)

	return render_template('success.html', name = file.filename)



if __name__ == "__main__":
	app.run(debug=True)


'''

for uploading files in falsk we need to have an **HTML form with the encryption set to multipart/form-data** .
	Eg: 	enctype="multipart/form-data

The server-side flask script fetches the file from the request object using request.files[] Object.

to get the file from html form:
	file = request.files['file']

to get the name of that file :
	name = request.files['file'].filename  

'''
#_-----------------------------------------------------------------------------------------------------------

