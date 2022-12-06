from sqlalchemy.sql.expression import null
from flask_login import login_manager
from flask import session
import jwt
import bcrypt
import datetime
import repository as repo


class Cart:
    def __init__(self):
        pass

    def check_email_existed(self, email):
        res = self.user_repository.select_by_email(email)
        if res is None:
            return True
        else:
            return False

    def register(self, request):
        name = request["name"]
        email = request['email']
        password = request['password']

        new_user = self.user_repository.insert_user({"name":name, "email":email, "password":password})
        group_response = self.user_group_repository.insert(new_user["id"], 4) #4 for register user group

        return {"data": new_user}

    @classmethod
    def create_empty_cart(cls, user_id):
        # user = self.user_repository.select(data)
        cart = repo.CartRepository.insert_carts(data={
            'owner_id': user_id
        })
        return cart


    @classmethod
    def get_current_cart(cls, current_user_id) -> dict:
        # will add more cart for each user
        carts = repo.CartRepository.get_carts(current_user_id)
        if not carts or len(carts) == 0:
            new_cart = cls.create_empty_cart(current_user_id)
            return {
                "cart": new_cart,
            }
        cart_items = repo.CartItemRepository.get_by_cart_id(carts[0].id)
        cart_item_res = []
        for item in cart_items:
            sub_res = item.json()
            product = repo.ProductRepository.get_by_id(item.product_id)
            sub_res["name"] = product.name
            sub_res["code"] = product.code
            sub_res["img_url"] = product.img_url
            cart_item_res.append(sub_res)
        return {
            "cart": carts[0].json(),
            "cart_items": cart_item_res,
        }

    @classmethod
    def add_product_to_cart(cls, cart_id, product_id, quantity) -> dict:
        existed_items = repo.CartItemRepository.get_by_cart_id(cart_id)
        print(existed_items)
        print("why")
        for item in existed_items:
            if item.product_id == product_id:
                repo.CartItemRepository.update_cart_item(item.id, item.customer_price, item.quantity + quantity)
                print("in")
                res = cls.get_current_cart(cart_id)
                return res
        product = repo.ProductRepository.get_by_id(product_id)
        repo.CartItemRepository.create_cart_item(cart_id, product_id, product.price, quantity)
        current_cart = repo.CartRepository.get_by_id(cart_id)
        res = cls.get_current_cart(current_cart.id)
        return res
