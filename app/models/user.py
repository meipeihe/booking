from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db

__author__ = 'wuxian'


class User(Base):
    id = Column(Integer, unique=True, primary_key=True, autoincrement=True)
    email = Column(String(30), unique=True)
    nick_name = Column(String(50))
    _password = Column('password', String(200))
    auth = Column(SmallInteger, default=1)

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
