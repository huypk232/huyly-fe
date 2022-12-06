from datetime import date, datetime
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.sql.schema import ForeignKey, Table
from database.db_base import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from flask_login import LoginManager


class Role(Base):
    __tablename__ = "roles"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
