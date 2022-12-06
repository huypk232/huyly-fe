from flask import Blueprint, request, render_template, flash, redirect
from flask.json import jsonify
from flask_login import current_user

import service

user_api = Blueprint("user_api", __name__)


@user_api.route('/<string:role>', methods=['POST', 'GET'])
def get_users(role):
    if request.method == 'POST':
        return render_template('dashboard.html')
    else:
        # customer role id = 2
        # partner role id = 3
        # vendor role id = 4
        if role == 'customer':
            res = service.User.get_users(2)
            render_template()
        if role == 'partner':
            res = service.User.get_users(3)
        if role == 'vendor':
            res = service.User.get_users(4)
        users = service.User.get_users()
        return render_template('users.html', context=users)\


@user_api.route('/<int:user_id>', methods=['POST', 'GET'])
def user_with_id(user_id):
    if request.method == 'POST':
        return render_template('dashboard.html')
    else:
        user = service.User.get_user_detail(user_id)
        # get total products and orders of users
        return render_template('about.html', context=user)


@user_api.route('/vendors', methods=['POST', 'GET'])
def get_vendors():
    if request.method == 'POST':
        return render_template('dashboard.html')
    else:
        # customer role id = 2
        # partner role id = 3
        # vendor role id = 4
        users = service.User.get_users(4)
        return render_template('users.html', context=users) \


@user_api.route('/partners', methods=['POST', 'GET'])
def get_partners():
    if request.method == 'POST':
        return render_template('dashboard.html')
    else:
        # customer role id = 2
        # partner role id = 3
        # vendor role id = 4
        users = service.User.get_users(3)
        return render_template('users.html', context=users) \


@user_api.route('/customers', methods=['POST', 'GET'])
def get_customers():
    if request.method == 'POST':
        return render_template('dashboard.html')
    else:
        # customer role id = 2
        # partner role id = 3
        # vendor role id = 4
        users = service.User.get_users(2)
        return render_template('users.html', context=users)

