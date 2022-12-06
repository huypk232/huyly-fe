from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.orm import relationship
from .base import Base
from .product import Product
from sqlalchemy import Column, Integer, String


class CartItem(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id', name='product_id'))
    cart_id = Column(Integer, ForeignKey('carts.id'))
    customer_price = Column(Integer)
    quantity = Column(Integer)

    # product = relationship("Product", backref="cart_items",  foreign_keys=product_id)


    def json(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "cart_id": self.cart_id,
            "customer_price": self.customer_price,
            "quantity": self.quantity
        }
