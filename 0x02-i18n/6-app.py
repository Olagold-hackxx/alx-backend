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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """Get user details"""
    return users.get(user_id)


@app.before_request
def before_request():
    """Get query params"""
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale():
    """Get the locale"""

    # Check if user is logged in
    if g.user:
        # Get locale from parameters
        url_locale = request.args.get('locale')
        if url_locale:
            return url_locale
        # Get locale from user settings if available
        elif g.user['locale']:
            return g.user['locale']
        # Get locale from request header
        elif request.headers.get('Accept-Language'):
            header_locale = request.headers.get('Accept-Language')
            # Split the Accept-Language header to get the preferred locale
            preferred_locale = header_locale.split(',')[0]
            if preferred_locale in app.config['LANGUAGES']:
               return preferred_locale

    # Return default locale if no match found
    return app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def home():
    """Home page
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
