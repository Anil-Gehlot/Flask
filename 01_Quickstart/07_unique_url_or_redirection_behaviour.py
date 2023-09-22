

from flask import Flask

app = Flask(__name__)

 

@app.route('/projects/')
def project():
	return 'this is project page'

@app.route('/about')
def about():
	return 'this is about page'


'''

 Unique URLs / Redirection Behavior: 
 canonical url : canonical url is the standard form of url. example  '/projects/'  

 If a user accesses a URL without a trailing slash that has a canonical form with a trailing slash (e.g., '/projects' instead of '/projects/'), 
 Flask will automatically redirect the user to the canonical URL with the trailing slash ('/projects/'). but if user will try '/about/' it will raise an errorL: no url found.

'''