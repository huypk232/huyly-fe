from sqlalchemy.sql.expression import null
from flask_login import login_manager
from flask import session
import jwt
import bcrypt
import datetime
import repository as repo
import service
import model.order as order_model


class Order:
    def __init__(self):
        pass


    @classmethod
    def get_current_user_orders(cls, user_id):
        orders = repo.OrderRepository.get_orders(user_id)
        user = repo.UserRepository.get_by_id(user_id)

        return {
            'orders': orders,
            'user': user,
        }


    @classmethod
    def get_order_detail(cls, order_id) -> dict:
        order = repo.OrderRepository.get_by_id(order_id)
        items = repo.OrderItemRepository.get_by_order_id(order.id)

        order_item_res = []
        for item in items:
            sub_res = item.json()
            print('product_id', item.product_id)
            product = repo.ProductRepository.get_by_id(item.product_id)
            sub_res['name'] = product.name
            sub_res['code'] = product.code
            sub_res['img_url'] = product.img_url
            order_item_res.append(sub_res)
        return {
            'order': order,
            'order_items': items,
        }

    @classmethod
    def get_item_by_order_id(cls, order_id) -> dict:
        items = repo.OrderItemRepository.get_by_order_id(order_id)

        return {
            'order_items': items,
        }

    @classmethod
    def create_order(cls, cart_id, current_user_id) -> dict:
        cart = service.Cart.get_current_cart(current_user_id)
        order = repo.OrderRepository.insert_order({
            'code': str(datetime.datetime.now()),
            'cart_id': cart_id,
            'owner_id': cart['cart'].owner_id
        })
        items = cart['cart_items']
        item_res = []
        for item in items:
            item_res.append(repo.OrderItemRepository.insert_item(order.id, item.product_id, item.customer_price,
                                                                 item.quantity))
        return {
            'order': order,
            'order_items': item_res,
        }
