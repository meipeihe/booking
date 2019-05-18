
from app.lib.error import APIException

__author__ = 'wuxian'


class Success(APIException):
    code = 201
    error_code = 0
    success = True
    msg = ''


class DeleteSuccess(Success):
    code = 202


class ClientError(APIException):
    code = 400
    error_code = 1001
    msg = 'client invalid'


class ClientParameterError(APIException):
    code = 401
    error_code = 1002
    msg = 'invalid parameters'


class NotFound(APIException):
    code = 402
    error_code = 1003
    msg = 'not found'


class AuthFail(APIException):
    code = 403
    error_code = 1004
    msg = 'auth fail'


class ServerError(APIException):
    pass