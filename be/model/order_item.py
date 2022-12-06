from sqlalchemy.sql.schema import ForeignKey, Table
from .base import Base
from sqlalchemy import Column, Integer, String


class OrderItem(Base):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id', name='product_id'))
    order_id = Column(Integer, ForeignKey('orders.id', name='order_id'))
    price = Column(Integer)
    quantity = Column(Integer)

    def json(self):
        return {
            'id': self.id,
            'product_id': self.product_id,
            'owner_id': self.order_id,
            'price': self.price
        }
