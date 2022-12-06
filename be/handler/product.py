from flask import Blueprint, request, render_template, flash, redirect
from flask.json import jsonify
from flask_login import current_user

import service

product_api = Blueprint("product_api", __name__)


@product_api.route('', methods=['GET', 'POST'])
def get_all():
    # if current_user.is_authenticated:
        if request.method == "POST":
            data = {
                "name": request.form['name'],
                "code": request.form['code'],
                "price": request.form['price'],
                "img_url": request.form['img_url'],
                "uom": request.form['uom'],
                "stock": request.form['stock'],
                "owner_id": current_user.id
            }
            if not request.form["name"]:
                return "Missing group name", 400
            json_data = {
                "current_user_id": current_user.id,
                "name": request.form["name"]
            }
            return render_template("products.html")
        elif request.method == "GET":
            products = service.Product.get_all()
            # # return render_template("products.html", context=products)
            # user_cart = service.Cart.get_current_cart(current_user.id)
            # print(user_cart.__getitem__('cart'))
            # context = products
            # context['user_cart'] = user_cart.__getitem__('cart')
            # # print(context['user_cart'].id)
            # categories = service.Category.get_all()
            # context['categories'] = categories
            # print(1)
            return jsonify({
                "products": products
            })
    # else:
    #     return jsonify({"HTTP Response": 204, "content": "U must login"})


@product_api.route('/<int:product_id>', methods=['GET', 'POST', 'DELETE'])
def get_by_id(product_id):
    if current_user.is_authenticated:
        if request.method == "POST":
            if request.form["act"] == "Update":
                if not request.form["name"]:
                    return "Missing group name", 400
                json_update_data = {
                    "id": id,
                    "name": request.form["name"],
                    "current_user_id": current_user.id
                }
                update_result = group_service.update(json_update_data)
                return render_template("response.html", context=update_result)
            elif request.method == "DELETE":
                delete_result = group_service.delete({
                    "id": id,
                    "current_user_id": current_user.id,
                    "entity": "group"
                })
                return render_template("response.html", context=delete_result)
        else:
            product = service.Product.get_by_id(product_id)
            context = product
            user_cart = service.Cart.get_current_cart(current_user.id)
            print(user_cart.__getitem__('cart'))
            context['user_cart'] = user_cart.__getitem__('cart')
            return render_template("product.html", context=context)
    else:
        return jsonify({"HTTP Response": 204, "content": "U must login"})
