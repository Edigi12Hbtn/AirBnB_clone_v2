#!/usr/bin/python3
"""Flask web application. Routes  / and /hbnb."""
from flask import Flask, render_template

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


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_func(text):
    """handling with optional route."""
    text = text.replace('_', ' ')
    return "{} {}".format('Python', text)


@app.route('/number/<int:n>')
def number_int(n):
    """handling route with integer."""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def template_func(n):
    """display a HTML page only if n is an integer."""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
