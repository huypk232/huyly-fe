from sqlalchemy.sql.sqltypes import BigInteger

from sqlalchemy.sql import func
from sqlalchemy import DateTime, Integer, String, Enum, Column, ForeignKey
import enum
from .base import Base


class ProductStatus(enum.Enum):
    waiting_shipper = 1
    delivering = 2
    complete = 3
    cancel = 4


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    code = Column(String, nullable=False)
    price = Column(Integer, nullable=True)
    img_url = Column(String, nullable=False)
    uom = Column(String, nullable=False)
    status = Column(Enum(ProductStatus))
    stock = Column(Integer)
    owner_id = Column(Integer, ForeignKey('users.id', name='owner_id'))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now())

    def json(self):
        d = {
            "id": self.id,
            "name": self.name,
            "code": self.code,
            "price": self.price,
            "img_url": self.img_url,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }
        return d


class ProductItem(Base):
    __tablename__ = 'Products'

    id = Column(Integer, primary_key=True)
    code = Column(String, nullable=False)
    status = Column(Enum(ProductStatus))
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    def to_dict(self):
        d = {
            "id": self.id,
            "name": self.name,
            "created_at": str(self.created_at),
            "updated_at": str(self.updated_at),
        }
        return d