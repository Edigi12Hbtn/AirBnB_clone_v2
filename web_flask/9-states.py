#!/usr/bin/python3
"""Flask web application. Routes  / and /hbnb."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False
app.jinja_env.add_extension('jinja2.ext.do')


@app.route('/states/')
@app.route('/states/<id>')
def states_id(id=0):
    """displays HTML."""
    states = storage.all(State)
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def teardown_appcontext(arg):
    """tear down method."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
