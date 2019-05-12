from flask_wtf import Form
from flask import request

from app.lib.error_code import ClientParameterError

__author__ = 'wuxian'


class BaseForm(Form):

    def __init__(self, data=None):
        if not data:
            data = request.json
        super(BaseForm, self).__init__(data=data, csrf_enabled=False)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            raise ClientParameterError(msg=self.errors)
        return self
