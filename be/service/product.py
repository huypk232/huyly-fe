from sqlalchemy.sql.expression import null
from flask_login import login_manager
from flask import session
import jwt
import bcrypt
import datetime
import repository as repo


class Product:
    def __init__(self):
        pass

    @staticmethod
    def get_all():
        products = repo.ProductRepository.get_all()
        res = []
        for product in products:
            res.append(product.json())
        return res

    @staticmethod
    def get_by_id(product_id):
        product = repo.ProductRepository.get_by_id(product_id)
        return {
            "product": product.json(),
        }


    @classmethod
    def get_current_cart(cls, current_user_id) -> dict:
        cart = repo.CartRepository.get_carts(current_user_id)[0]
        cart_items = repo.CartItemRepository.get_by_cart_id(cart.id)
        cart_item_res = []
        for item in cart_items:
            sub_res = item.json()
            product = repo.ProductRepository.get_by_id(item.product_id)
            sub_res["name"] = product.name
            sub_res["code"] = product.code
            cart_item_res.append(sub_res)
        return {
            "cart": cart,
            "cart_items": cart_item_res,
        }
