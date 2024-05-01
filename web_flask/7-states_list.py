#!/usr/bin/python3
"""
"""
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route("/states_list")
def states_list():
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def tear(self):
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0")
