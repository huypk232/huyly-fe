from flask import Blueprint, request, render_template, flash, redirect
from flask.json import jsonify
from flask_login import current_user

import service

order_api = Blueprint("order_api", __name__)



@order_api.route('', methods=['GET', 'POST'])
def orders():
    if current_user.is_authenticated:
        if request.method == "POST":
            current_cart = service.Cart.get_current_cart(current_user.id)
            cart_id = current_cart['cart'].id
            order = service.Order.create_order(cart_id, current_user.id)
            return render_template("order.html", context=order)
        elif request.method == "GET":
            res = service.Order.get_current_user_orders(current_user.id)
            return render_template("orders.html", context=res)
    else:
        return jsonify({"HTTP Response": 204, "content": "U must login"})


@order_api.route('/<int:order_id>', methods=['GET', 'POST', 'DELETE'])
def get_detail(order_id):
    if current_user.is_authenticated:
        if request.method == "POST":

            return render_template("order.html")
        else:
            order = service.Order.get_order_detail(order_id)
            return render_template("order.html", context=order)
    else:
        return jsonify({"HTTP Response": 204, "content": "U must login"})
