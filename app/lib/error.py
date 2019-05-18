from flask import json
from werkzeug.exceptions import HTTPException

__author__ = 'wuxian'


class APIException(HTTPException):
    code = 500
    error_code = 1001
    msg = 'sorry, we made a mistake'
    success = False

    def __init__(self, code=None, error_code=None, msg=None):
        if code:
            self.code = code
        if error_code:
            self.error_code = error_code
        if msg:
            self.msg = msg
        super(APIException, self).__init__(description=self.msg, response=None)

    def get_body(self, environ=None):
        result = {
            "success": self.success,
            "code": self.code,
            "error_code": self.error_code,
            "msg": self.msg
        }

        return json.dumps(result)

    def get_headers(self, environ=None):
        return [("Content-Type", "application/json")]