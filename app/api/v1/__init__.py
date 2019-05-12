from flask import Blueprint

from app.api.v1.client import client

__author__ = 'wuxian'


def create_blueprint_v1():
    blur_print = Blueprint('/v1', __name__)
    client.register(blur_print)
    return blur_print


