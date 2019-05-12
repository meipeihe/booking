
from app.lib.enums import ClientTypeEnums
from app.lib.error_code import Success
from app.lib.redprint import Redprint
from app.models.user import User
from app.validate.forms import ClientForm, UserEmailForm

__author__ = 'wuxian'


client = Redprint('client')


@client.route('/register', methods=['POST'])
def register():
    form = ClientForm().validate_for_api()
    promise = {
        ClientTypeEnums.USER_EMAIL: register_by_email
    }
    promise[form.type.data]()
    return Success()


def register_by_email():
    form = UserEmailForm().validate_for_api()
    User.register_by_email(
        form.account.data,
        form.nickname.data,
        form.secure.data
    )

