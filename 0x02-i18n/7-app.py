#!/usr/bin/env python3
"""Flask babel"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

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
    """Get query params before resolving each request"""
    user_id = request.args.get('login_as')
    user = get_user(int(user_id)) if user_id else None
    g.user = user


@babel.localeselector
def get_locale():
    """Get the locale"""
    requested_locale = request.args.get('locale')

    # If the requested locale is supported, return it
    if requested_locale and requested_locale in app.config['LANGUAGES']:
        return requested_locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def home():
    """Home page
    """
    return render_template('5-index.html')



@babel.timezoneselector
def get_timezone():
    # Get timezone from URL parameters
    url_timezone = request.args.get('timezone')

    # Check if user is logged in
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        if user and user['timezone']:
            try:
                pytz.timezone(user['timezone'])
                return user['timezone']
            except pytz.UnknownTimeZoneError:
                pass

    # Get timezone from user settings if available
    if 'login_as' in request.args:
        user = get_user(int(request.args.get('login_as')))
        if user and user['timezone']:
            try:
                pytz.timezone(user['timezone'])
                return user['timezone']
            except pytz.UnknownTimeZoneError:
                pass

    # If no valid timezone found, default to UTC
    return 'UTC'


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
