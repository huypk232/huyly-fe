from flask import Blueprint, request, render_template, flash, redirect, url_for
from flask.json import jsonify
from flask_login import current_user
import service

import repository

cart_api = Blueprint("cart_api", __name__)



@cart_api.route('', methods=['GET', 'POST'])
def get_current_cart():
    if current_user.is_authenticated:
        if request.method == "POST":
            action = request.form['action']
            if action == 'create':

                product_id = request.form['product_id']
                quantity = request.form['quantity']
                if not quantity:
                    quantity = 1
                user_cart = service.Cart.add_product_to_cart(cart_id, product_id, quantity)
                product = service.Product.get_by_id(product_id)
                context = product
                context['user_cart'] = user_cart.__getitem__('cart')
                # return render_template('product.html', context=context)
                # return redirect(f'../products/{product_id}')
                # return render_template('shop.html', scroll='add-to-cart')
                return redirect('../products')
            elif action == 'add_product':
                product_id = request.form['product_id']
                quantity = request.form['quantity']
                user_cart = service.Cart.get_current_cart(current_user.id)
                print("vao chua?")
                updated_user_cart = service.Cart.add_product_to_cart(user_cart, product_id, quantity)
                context = updated_user_cart
                context['user_cart'] = updated_user_cart.__getitem__('cart')
                return render_template('cart.html', context=context)
            else:
                items = [
                    {
                        "id": 1,
                        "quantity": 2,
                        "customer_price": 3,
                    }
                ]
                for input_value in request.form:
                    if '|' in input_value:
                        elem = input_value.split('|')
                        entity, entity_id, entity_attribute = elem[0], elem[1], elem[2]
                        print(elem)
                user_cart = service.Cart.get_current_cart(current_user.id)
                context = user_cart
                context['user_cart'] = user_cart.__getitem__('cart')
                return render_template('cart.html', context=context)
        elif request.method == "GET":
            user_cart = service.Cart.get_current_cart(current_user.id)
            context = user_cart
            context['user_cart'] = user_cart.__getitem__('cart')
            print(context)
            return render_template('cart.html', context=context)
    else:
        return jsonify({"HTTP Response": 204, "content": "U must login"})


@cart_api.route('/<int:cart_id>/cart_items/<int:cart_item_id>', methods=['GET', 'POST'])
def cart_detail(cart_id, cart_item_id):
    if current_user.is_authenticated:
        if request.method == "POST":
            action = request.form['action']
            if action == 'create':

                product_id = request.form['product_id']
                quantity = request.form['quantity']
                if not quantity:
                    quantity = 1
                user_cart = service.Cart.add_product_to_cart(cart_id, product_id, quantity)
                product = service.Product.get_by_id(product_id)
                context = product
                context['user_cart'] = user_cart.__getitem__('cart')
                # return render_template('product.html', context=context)
                # return redirect(f'../products/{product_id}')
                # return render_template('shop.html', scroll='add-to-cart')
                return redirect('../products')
            else:
                print(request.form['cart_items|1|quantity'])
                user_cart = service.Cart.get_current_cart(current_user.id)
                context = user_cart
                context['user_cart'] = user_cart.__getitem__('cart')
                return render_template('cart.html', context=context)
        else:
            # delete
            if not cart_id or not cart_item_id:
                return jsonify({"HTTP Response": 500, "content": "Internal Server"})

            return render_template("cart.html")
    else:
        return jsonify({"HTTP Response": 204, "content": "U must login"})@cart_api.route('/<int:cart_id>', methods=['GET', 'POST', 'DELETE'])


# @cart_api.route('/<int:cart_id>', methods=['UPDATE'])
# def update_cart(cart_id):
#     if current_user.is_authenticated:
#         if request.method == "POST":
#             product_id = request.form['product_id']
#             quantity = request.form['quantity']
#             if not quantity:
#                 quantity = 1
#             print(quantity)
#             user_cart = service.Cart.add_product_to_cart(cart_id, product_id, quantity)
#             product = service.Product.get_by_id(product_id)
#             context = product
#             context['user_cart'] = user_cart.__getitem__('cart')
#             # return render_template('product.html', context=context)
#             # return redirect(f'../products/{product_id}')
#             # return render_template('shop.html', scroll='add-to-cart')
#             return redirect('../products')
#         elif request.method == "PUT":
#             user_cart = service.Cart.get_current_cart(current_user.id)
#             context = user_cart
#             context['user_cart'] = user_cart.__getitem__('cart')
#             return render_template('cart.html', context=context)
#         else:
#             if not cart_id:
#                 return jsonify({"HTTP Response": 500, "content": "Internal Server"})

#             return render_template(".html")
#     else:
#         return jsonify({"HTTP Response": 204, "content": "U must login"})@cart_api.route('/<int:cart_id>', methods=['GET', 'POST', 'DELETE'])
