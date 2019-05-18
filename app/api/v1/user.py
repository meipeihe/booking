from flask import g, jsonify

from app.lib.error_code import DeleteSuccess
from app.lib.redprint import Redprint
from app.lib.token_auth import auth
from app.models.base import db
from app.models.user import User

__author__ = 'wuxian'


api = Redprint('user')


@api.route('/<int:uid>', methods=['GET'])
@auth.login_required
def super_get_user(uid):
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('/', methods=['GET'])
@auth.login_required
def get_user():
    uid = g.userinfo['uid']
    user = User.query.get_or_404(uid)
    return jsonify(user)


@api.route('/<int:uid>', methods=['DELETE'])
@auth.login_required
def delete_user(uid):
    with db.auto_commit():
        user = User.query.get_or_404(uid)
        user.delete()
    return DeleteSuccess()






