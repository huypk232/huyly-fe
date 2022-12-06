from flask import Blueprint, request, render_template, flash, redirect
from flask.json import jsonify
from flask_login import current_user, login_user, login_required, logout_user
from flask_cors import cross_origin

import repository
import service
import jwt
import datetime

dashboard_api = Blueprint("dashboard_api", __name__)

secret_key = 'secretaryship'

@dashboard_api.route('', methods=['GET', 'POST'])
@dashboard_api.route('/home', methods=['GET', 'POST'])
def dashboard():
    if current_user.is_authenticated:
        if request.method == "POST":
            if not request.form["name"]:
                return "Missing group name", 400
            json_data = {
                "current_user_id": current_user.id,
                "name": request.form["name"]
            }
            return render_template("dashboard.html")
        elif request.method == "GET":
            return render_template("index.html", context={'user_id': current_user.id})
    else:
        return redirect('./login')


@dashboard_api.route('/<int:id>', methods=['GET', 'POST', 'DELETE'])
def manage(id):
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
            group = group_service.read_by_id(id)
            group["entity"] = "groups"
            return render_template("manage.html", context=group)
    else:
        return jsonify({"HTTP Response": 204, "content": "U must login"})


@dashboard_api.route('/login', methods=['POST', 'GET', 'OPTION'])
def login():
    if request.method == "POST":
        email = request.json['username']
        password = request.json['password']
        if not email:
            return 'Missing Email', 401
        if not password:
            return 'Missing Password', 401
        res = service.Auth.login({
            "email": email,
            "password": password
        })

        if res is not None:
            login_user(res)
            token = jwt.encode({
                "email": email,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)},
                secret_key
            )

            return jsonify({
                "token":  "otoke"
            })
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    else:
        return {
            "token": "otoke"
        }


@dashboard_api.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        if password != confirm_password:
            flash('2 password ko giong nhau', 'danger')
        form_data = {
            "email": email,
            'password': password,
        }
        if request.form['role'] == 'customer':
            form_data['role_id'] = 2
        elif request.form['role'] == 'partner':
            form_data['role_id'] = 3
        else:
            form_data['role_id'] = 4
        register_res = service.Auth.register(form_data)
        login_res = service.Auth.login(register_res['email'], register_res['password'])

        if login_res is not None:
            login_user(login_res)
            token = jwt.encode({
                "email": login_res['email'],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=1)},
                secret_key
            )
            return redirect('/')
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    else:
        return render_template('login.html')

@dashboard_api.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('./login')