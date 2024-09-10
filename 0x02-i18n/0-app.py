#!/usr/bin/env python3
"""Basic Flask app that renders a simple HTML template."""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Index route that renders a basic HTML page."""
    return render_template("0-index.html",)


if __name__ == "__main__":
    app.run(debug=True)
