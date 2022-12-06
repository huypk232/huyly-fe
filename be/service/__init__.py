from .auth import Auth
from .cart import Cart
from .category import Category
from .product import Product
from .order import Order
from .user import User
from .warehouse import Warehouse


class Service:
    auth = Auth()
    cart = Cart()
    category = Category()
    order = Order()
    user = User()
    product = Product()
    warehouse = Warehouse()
