from flask import Flask

from app.api.v1 import create_blueprint_v1
from app.config import setting, secure
from app.models.base import db

__author__ = 'wuxian'


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
    app.register_blueprint(create_blueprint_v1(), url_prefix='/api/v1')
