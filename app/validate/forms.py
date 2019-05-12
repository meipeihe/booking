from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, length, Email, ValidationError

from app.lib.enums import ClientTypeEnums
from app.models.user import User
from app.validate.baseforms import BaseForm

__author__ = 'wuxian'


class ClientForm(BaseForm):
    account = StringField(validators=[DataRequired(), length(max=50, min=3)])
    secure = StringField()
    type = IntegerField()

    def validate_type(self, value):
        try:
            client = ClientTypeEnums(value.data)
        except ValueError as e:
            raise e

        self.type.data = client


class UserEmailForm(ClientForm):
    account = StringField(validators=[Email('invalidate email')])
    secure = StringField(validators=[DataRequired(), length(min=5, max=50)])
    nickname = StringField(validators=[DataRequired(), length(min=2, max=50)])

    def validate_account(self, value):
        if User.query.filter_by(email=value.data).first():
            raise ValidationError('account exists')


