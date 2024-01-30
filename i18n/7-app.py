#!/usr/bin/env python3
"""basic flask app with index.html template
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz

app = Flask(__name__)

users = {  # mocking a dictionary of users for testing purposes
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """CLASS - configures available languages
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)  # set Babel's default locale and timezone
babel = Babel(app)  # initialize Babel in the app


@app.route('/', strict_slashes=False)
def index():
    """`/` route
    """
    return render_template('6-index.html')


@babel.localeselector
def get_locale():
    """returns the locale to use for the current request
    """
    locale = request.args.get('locale')  # get locale from query string
    if locale and locale in Config.LANGUAGES:  # if locale is in LANGUAGES
        return locale

    user = get_user()  # get user locale from the user's settings
    # check global g for user's locale
    if 'locale' in g and g.user_locale in app.config['g.user_locale']:
        return g.user_locale
    if user and user.get('locale') in app.config['LANGUAGES']:
        return user.get('locale')
    # get the users locale from the users header
    request_header_locale = request.headers.get('LANGUAGES')
    if request_header_locale:
        # Extract the preferred language from the Accept-Language header
        preferred_languages = [
            lang.strip() for lang in request_header_locale.split(',')
            ]
        for lang in preferred_languages:
            if lang in app.config['locale']:
                return lang

# UNDER CONSTRUCTION // UNDER CONSTRUCTION // UNDER CONSTRUCTION
@babel.timezoneselector
def get_user_timezone():
    """returns the timezone to use for the current request
    """
    # find the timezone parameter in URL parameters
    user_timezone = request.args.get('timezone')  # get timezone from query string
    if user_timezone:
        try:
            pytz.timezone(user_timezone)
            return True
        except pytz.exceptions.UnknownTimeZoneError:
            return False
    # find timezone from user settings
    user = get_user()  # get user locale from the user's settings
    if user and user.get('timezone'):
        try:
            pytz.timezone(user.get('timezone'))
            return timezone
        except pytz.exceptions.UnknownTimeZoneError:
            # uhhh
            pass
            return user.get('timezone')
    # default to UTC
    return 'UTC'


# MOCK CONTENT BELOW
def get_user():
    """returns a user dict
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users.get(int(user_id))  # get user from users dictionary
    return None


@app.before_request
def before_request():
    """calls get_user on start to get a user
    and set it as a global variable on 'flask.g.user'
    """
    g.user = get_user()  # set g.user as a global variable


if __name__ == '__main__':
    app.run()
