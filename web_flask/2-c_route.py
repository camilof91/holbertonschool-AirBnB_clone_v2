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
    This function handles URLs like /c/something, where <text>
    captures the value after "/c/". It replaces underscores
    with spaces and returns "C " followed by
    the modified text.
    """
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
