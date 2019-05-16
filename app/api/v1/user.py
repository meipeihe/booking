from flask import g, jsonify

from app.lib.redprint import Redprint
from app.lib.token_auth import auth
from app.models.user import User

__author__ = 'wuxian'


api = Redprint('user')


@api.route('/<int:id>', methods=['GET'])
@auth.login_required
def get_user(id):
    user = User.query.get_or_404(id)

    return jsonify(user)


