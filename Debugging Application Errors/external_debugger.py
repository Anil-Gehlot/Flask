

# more powerful debugging experience than the built-in debugger.
# When using an external debugger, the app should still be in debug mode, otherwise Flask turns unhandled errors into generic 500 error pages.
# However, the built-in debugger and reloader should be disabled so they don’t interfere with the external debugger.

# app.run(debug=True, use_debugger=False, use_reloader=False)
# flask --app hello run --debug --no-debugger --no-reload


from flask import Flask

app = Flask(__name__)

@app.route('/s/')
def hello():
    name = "World"

    # Add a breakpoint here
    return f"Hello, {name}!"

if __name__ == '__main__':
    app.run(debug=True, use_debugger=False, use_reloader=False)