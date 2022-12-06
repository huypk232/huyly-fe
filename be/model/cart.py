from sqlalchemy.sql.schema import ForeignKey, Table
from .base import Base
from sqlalchemy import Column, Integer, String


class Cart(Base):
    __tablename__ = 'carts'

    id = Column(Integer, primary_key=True)
    owner_id = Column(Integer, ForeignKey('users.id'))

    def json(self):
        return {
            'id': self.id,
            'owner_id': self.owner_id
        }
