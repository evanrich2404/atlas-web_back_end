#!/usr/bin/env python3
"""
placeholder
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def home():
    """template"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """babel location selection"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    user_id = request.args.get('login_as')
    if user_id is not None:
        user_id = int(user_id)
        if user_id in users:
            return users[user_id]
    return None


@app.before_request
def before_request():
    """before request"""
    user = get_user
    g.user = user


if __name__ == "__main__":
    app.run(debug=True)
