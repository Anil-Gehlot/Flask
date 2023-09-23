
'''
cookies are the small text files , jisme information store rehti h, or ye cookies files client side par hi store hoti h mean hamare browser per

cookies ki help se hum user ke data ko track karte like usne kya2 search kia , kab2 visit kiya, search histoty etc OR us data ke base per hum website ke content ko user ke acc
personalised kar sakte h  

'''

from flask import Flask, request, make_response

app = Flask(__name__)


@app.route("/")
def index():
	return "working with cookies"

@app.route("/set/")
def setcookie():
	resp = make_response("setting the cookies.")
	resp.set_cookie("cookies_name", "cookies_value")
	resp.set_cookie("APICID", "random cookies")

	return resp

@app.route("/get/")
def getcookie():
	name1 = request.cookies.get("cookies_name")
	name2 = request.cookies.get("APICID") 
	
	return [name1, name2]
