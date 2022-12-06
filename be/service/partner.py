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
    def login(cls, data):
        # user = self.user_repository.select(data)
        user = repository.UserRepository.select(data)
        if user is not None:
            token = jwt.encode({
                "email": data["email"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)},
                "secretkey",
                algorithm="HS256"
            )
            session["token"] = token
            print(token)
            return user
        return None


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

    @classmethod
    def add_product_to_cart(cls, cart_id, product_id, quantity) -> dict:
        product = repo.ProductRepository.get_by_id(product_id)
        print(quantity)
        new_cart_item = repo.CartItemRepository.create_cart_item(cart_id, product_id, product.price, quantity)
        print(new_cart_item)
        current_cart = repo.CartRepository.get_by_id(cart_id)
        res = cls.get_current_cart(current_cart.id)
        return res
