
'''


Flask looks for templates in the 'templates' folder by default.

Jinja2 Template Engine: Flask configures the Jinja2 template engine automatically for you. 
						Jinja2 is a powerful and widely used template engine that allows you
						to create templates for generating HTML, plain text, emails, and more.

Rendering Templates: To render a template in your Flask view function, 
						you can use the render_template() method. 
						It takes the name of the template file and any variables you want to pass to the template as keyword arguments.

'''


from flask import render_template, Flask
from markupsafe import Markup

app = Flask(__name__)

@app.route('/hello/')
@app.route('/hello/<name>')

def hello(name=None):
	return render_template('hello.html',name=name)




@app.route("/")
def markup_example():

	# Using the Markup class to mark a string as safe HTML
	safe_html = Markup("<strong>Hello %s!</strong>") % "<blink>hacker</blink>"

	# Using Markup.escape() to escape special characters
	escaped_html = Markup.escape('<blink>hacker</blink>')

	# Using Markup.striptags() to remove HTML tags
	stripped_text = Markup('<em>Marked up</em> &raquo; HTML').striptags()

	return render_template('markupsafe.html', safe_html=safe_html, escaped_html=escaped_html, stripped_text=stripped_text)



'''

Flask automatically enables HTML escaping for variables rendered in templates to enhance security. 
This means that any HTML tags and special characters in the variables are escaped by default.

for safe_html :  the string is marked as safe HTML, allowing the embedded <blink>hacker</blink> HTML tags to be rendered as actual HTML.

for escaped_html: The Markup class also provides an escape() method that escapes special characters in a string without marking it as safe HTML:

for stripped_text: The Markup class includes a striptags() method that removes HTML tags from a string, returning plain text. 
					This can be useful when you want to strip HTML tags from a variable before rendering it:

'''