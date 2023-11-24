#!/usr/bin/env python3
"""Flask babel"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """Babel config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)

@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def home():
    """Home page
    """
    return render_template('index.html', title=_('home_title'), header=_('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
