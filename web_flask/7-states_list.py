#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

# Create Flask application instance
app = Flask(__name__)

# Enable template auto-reload during development
app.config['TEMPLATES_AUTO_RELOAD'] = True

# Set the templates directory
app.config['TEMPLATES_DIR'] = 'web_flask/templates'


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the SQLAlchemy session after each request."""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Retrieves all State objects, sorts them by name, and renders a list."""
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)