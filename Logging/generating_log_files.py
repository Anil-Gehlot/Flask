

# logging is mainly used to keep log of running application


from flask import Flask
import logging

# creating flask application
app = Flask(__name__)

# yadi filename nahi denge to sara log terminal pe dikhega, filename se file me store hoga.
logging.basicConfig(filename = "logging.log", format="%(levelname)s:%(name)s:%(message)s")

@app.route("/")
def hello():
	return "hello Duniaa!!!!!!!!"

@app.route("/profile/")
def profile():
	return "this is profile section!!!!!!!!"

if "__name__"=="__main__":
	app.run(debug=True, port=8080)

