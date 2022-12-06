from .user import UserRepository
from .cart import CartRepository
from .cart_item import CartItemRepository
from .category import CategoryRepository
from .order import OrderRepository
from .order_item import OrderItemRepository
from .product import ProductRepository
from .user import UserRepository
from .warehouse import WarehouseRepository


class Repo:
    def __init__(self):
        cart_repo = CartRepository()
        cart_item_repo = CartItemRepository()
        # category_repo = CategoryRepository
        order_repo = OrderRepository
        order_item_repo = OrderItemRepository
        product_repo = ProductRepository()
        user_repo = UserRepository()
        warehouse_repo = WarehouseRepository()
