from datetime import date, datetime
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from sqlalchemy.sql.schema import ForeignKey, Table
from .base import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from flask_login import LoginManager


class Warehouse(Base):
    __tablename__ = "warehouses"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    code = Column(String)
    address = Column(String)
    owner_id = Column(Integer, ForeignKey('users.id'))

