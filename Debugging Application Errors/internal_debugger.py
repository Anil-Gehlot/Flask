

# The debugger is enabled by default when the development server is run in debug mode.
# 	flask --app hello run --debug

# When running from Python code, passing debug=True enables debug mode, which is mostly equivalent.
# app.run(debug=True)

from flask import Flask

app = Flask(__name__)

@app.route('/s/')
def hello():
    name = "World"

    # Add a breakpoint here
    # return f"Hello, {name}!"
    return render_template("djo.html")

if __name__ == '__main__':
    app.run(debug=True)