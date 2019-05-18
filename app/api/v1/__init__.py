from flask import Blueprint

from app.api.v1.token import api as token
from app.api.v1.client import client
from app.api.v1.user import api as user

__author__ = 'wuxian'


def create_blueprint_v1():
    blur_print = Blueprint('v1', __name__)
    client.register(blur_print)
    token.register(blur_print)
    user.register(blur_print)
    return blur_print


