from flask import Blueprint, request, render_template, flash, redirect
from flask.json import jsonify
from flask_login import current_user

import service

category_api = Blueprint("category_api", __name__)


@category_api.route('', methods=['GET', 'POST'])
def get_all():
    # if current_user.is_authenticated:
        if request.method == "POST":
            if not request.form["name"]:
                return "Missing group name", 400
            json_data = {
                "current_user_id": current_user.id,
                "name": request.form["name"]
            }
            return render_template("products.html")
        elif request.method == "GET":
            categories = service.Category.get_all()
            print(categories)
            return jsonify({
                "categories": categories
            })
    # else:
    #     return jsonify({"HTTP Response": 204, "content": "U must login"})

