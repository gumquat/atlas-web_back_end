#!/usr/bin/env python3
"""basic flask app with index.html template
"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)

users = {
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


@app.route('/')
def index():
    """`/` route
    """
    return render_template('4-index.html')


@babel.localeselector
def get_locale():
    """returns the locale to use for the current request
    """
    locale = request.args.get('locale')  # get locale from query string
    if locale and locale in Config.LANGUAGES:  # check if locale is valid
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
