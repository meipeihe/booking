from werkzeug.exceptions import HTTPException

from app.app import create_app
from app.lib.error import APIException

__author__ = 'wuxian'

app = create_app()


@app.errorhandler(Exception)
def framework_error(e):
    if isinstance(e, APIException):
        return e
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
        error_code = 1007
        return APIException(code=code, msg=msg, error_code=error_code)
    else:
        return APIException()


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])