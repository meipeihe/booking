from datetime import date

from flask import Flask as _Flask
from flask.json import JSONEncoder as _JSONEncoder

from app.api.v1 import create_blueprint_v1
from app.config import setting, secure
from app.lib.error_code import ServerError
from app.models.base import db

__author__ = 'wuxian'


class JSONEncoder(_JSONEncoder):
    def default(self, o):
        if hasattr(o, 'keys') and hasattr(o, '__getitem__'):
            return dict(o)
        if isinstance(o, date):
            return o.strftime('%Y-%m-%d')
        raise ServerError()


class Flask(_Flask):
    json_encoder = JSONEncoder


def create_app():
    app = Flask(__name__)
    app.config.from_object(setting)
    app.config.from_object(secure)
    register(app)
    apply_plugins(app)
    return app


def apply_plugins(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register(app):
    app.register_blueprint(create_blueprint_v1(), url_prefix='/api/v1/')



