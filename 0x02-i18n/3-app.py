#!/usr/bin/env python3
"""
Flask app with Babel and template localization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _


class Config:
    """
    Config class for Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determines the best match for supported languages from request headers.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Index route that renders a localized HTML page.
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
