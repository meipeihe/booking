from flask import current_app, jsonify

from app.lib.enums import ClientTypeEnums
from app.lib.redprint import Redprint
from app.models.user import User
from app.validate.forms import ClientForm
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


__author__ = 'wuxian'

api = Redprint('token')


@api.route('/login', methods=['POST'])
def get_token():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnums.USER_EMAIL: User.verify
    }
    user = promise[form.type.data](form.account.data,form.secure.data)

    token = generate_auth_token(user['uid'], form.type.data, user['scope'], current_app.config['EXPIRATION'])

    t = {
        'token': token.decode('ascii')
    }

    return jsonify(t), 201


def generate_auth_token(uid, ac_type, scope=None,
                        expiration=7200):
    s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)

    return s.dumps({
        'uid': uid,
        'type': ac_type.value,
        'scope': scope
    })




