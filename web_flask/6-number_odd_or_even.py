#!/usr/bin/python3
"""
taks file with a flask app
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    This function handles the root URL (/) and returns "Hello HBNB".
    """
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    This function handles the URL /hbnb and returns "HBNB".
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_rute(text):
    """
    This function handles URLs like /c/something,
    where <text> captures the value
    after "/c/". It replaces underscores with
    spaces and returns "C " followed by
    the modified text.
    """
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_rute(text=None):
    """
    This function handles URLs like /c/something,
    where <text> captures the value
    after "/python/". It replaces underscores
    with spaces and returns "C " followed by
    the modified text.
    """
    if text is None:
        text = "is cool"
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def num_rute(n):
    """
    This function handles URLs like /c/something,
    where <text> captures the value
    after "/python/". It replaces
    underscores with spaces and returns "C " followed by
    the modified text.
    """
    number = int(n)
    return f"{number} is a number"


@app.route("/number_template/<n>", strict_slashes=False)
def num_template(n):
    """
    This function handles URLs like /c/something,
    where <text> captures the value
    after "/python/". It replaces underscores
    with spaces and returns "C " followed by
    the modified text.
    """
    number = int(n)
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def num_odd_template(n):
    """
    This function handles URLs like /c/something,
    where <text> captures the value
    after "/python/". It replaces underscores
    with spaces and returns "C " followed by
    the modified text.
    """
    state = ' is even' if (int(n) % 2 == 0) else ' is odd'
    return render_template("6-number_odd_or_even.html", n=n, state=state)
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
