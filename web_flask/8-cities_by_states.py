#!/usr/bin/python3
"""Flask web application. Routes  / and /hbnb."""
from flask import Flask, render_template
from models import storage
from models.state import State
from os import getenv

type_db = getenv('HBNB_TYPE_STORAGE')

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """displays HTML."""
    states = storage.all(State)

    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_appcontext(arg):
    """tear down method."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
