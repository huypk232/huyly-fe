from datetime import date, datetime
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.sql.schema import ForeignKey, Table
from .base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from flask_login import LoginManager

#
# @login_manager.user_loader
# def get_user(ident):
#     return User.query.get(int(ident))


class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    avatar = Column(String)
    email = Column(String, nullable=False)
    password = Column(String)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return f"{self.id}"

    def get_id(self):
        return self.id

    def json(self):
        d = {
            "id": self.id,
            "name": self.name,
            "avatar": self.avatar,
            "email": self.email,
            "role_id": self.role_id,
        }
        return d
