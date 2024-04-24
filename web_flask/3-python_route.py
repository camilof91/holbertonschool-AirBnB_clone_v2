#!/usr/bin/python3
from flask import Flask

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
    This function handles URLs like /c/something, where <text> captures the value
    after "/c/". It replaces underscores with spaces and returns "C " followed by
    the modified text.
    """
    text = text.replace("_", " ")
    return f"C {text}"

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_rute(text=None):
    """
    This function handles URLs like /c/something, where <text> captures the value
    after "/python/". It replaces underscores with spaces and returns "C " followed by
    the modified text.
    """
    if text is None:
        text = "is cool"
    text = text.replace("_", " ")
    return f"Python {text}"

@app.route("/number/<n>", strict_slashes=False)
def num_rute(n):
    """
    This function handles URLs like /c/something, where <text> captures the value
    after "/python/". It replaces underscores with spaces and returns "C " followed by
    the modified text.
    """
    try:
        number = int(n)
        return f"{number} is a number"
    except ValueError:
        return "Not a number", 400 

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)