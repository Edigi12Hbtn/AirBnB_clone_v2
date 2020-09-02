#!/usr/bin/python3
"""Flask web application. Routes  / and /hbnb."""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """Flask Hello World."""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Manage hbnb route."""
    return "HBNB"


@app.route('/c/<text>')
def text_func(text):
    """returns text in path: /c/<text>"""
    text = text.replace('_', ' ')
    return "{} {}".format('C', text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
