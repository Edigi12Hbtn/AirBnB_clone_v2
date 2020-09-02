#!/usr/bin/python3
"""Flask web application. Routes  / and /hbnb."""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states():
    """displays HTML only if n is integer."""
    states = storage.all(State)
    list = []
    for val in states.values():
        list.append(val)
#    print(states)
#    return "All ok."
    return render_template('7-states_list.html', states=list)

@app.teardown_appcontext
def teardown_appcontext(arg):
    """tear down method."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
