from flask import g, current_app

from app.lib.error_code import AuthFail
from app.lib.scope import is_in_scope

__author__ = 'wuxian'

from flask_httpauth import HTTPBasicAuth
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer, BadSignature, SignatureExpired

auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(account, password):
    userinfo = verify_auth_token(account)
    if not userinfo:
        return False
    else:
        g.userinfo = userinfo
        return True


def verify_auth_token(token):
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except BadSignature:
        raise AuthFail(error_code=1005, msg='token is invalid')
    except SignatureExpired:
        raise AuthFail(error_code=1006, msg='token is expired')

    if data['scope'] is None or not is_in_scope(data['scope']):
        raise AuthFail(error_code=1007, msg='without auth')

    return data


