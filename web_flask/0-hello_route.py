#!/usr/bin/python3
"""script that starts a Flask web application."""
from flask import Flask

app = Flask(__name__)
#app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Flask Hello World."""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(debug=True)
