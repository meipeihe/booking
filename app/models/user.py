from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.lib.error_code import NotFound, AuthFail
from app.models.base import Base, db

__author__ = 'wuxian'


class User(Base):
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    email = Column(String(30), unique=True)
    nick_name = Column(String(50))
    _password = Column('password', String(200))
    auth = Column(SmallInteger, default=1)

    def keys(self):
        return ('email', 'nick_name')

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(account, nickname, secure):
        with db.auto_commit():
            user = User()
            user.email = account
            user.nick_name = nickname
            user.password = secure
            db.session.add(user)

    @staticmethod
    def verify(account, password):
        user = User.query.filter_by(email=account).first()
        if not user:
            raise NotFound()
        if not user.check_password(password):
            raise AuthFail()
        return {
            'uid': user.id
        }

    def check_password(self, password):
        if not self._password:
            return False
        return check_password_hash(self._password, password)