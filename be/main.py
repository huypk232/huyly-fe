import os

from flask import Flask, flash, request, jsonify, render_template, redirect
from flask.helpers import url_for
# from service.auth import Auth
from flask_cors import CORS
from flask_login import current_user, LoginManager, login_user, current_user, logout_user, login_required
from handler import api
from service.auth import Auth
# from https.api.auth_bp import secret_key


def init_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = 'secret_key'
    
    # app.config['CORS_HEADERS'] = 'Content-Type'
    app.register_blueprint(api, url_perfix="/api/v1")
    app.debug = True
    # app.register_blueprint(ui_bp, url_prefix="")
    login_manager = LoginManager(app)
    login_manager.login_view = 'login'
    login_manager.login_message_category = 'info'

    @login_manager.user_loader
    def load_user(user_id):
        return Auth.loaded_user(user_id)

    app.run()


if __name__ == '__main__':
    init_app()
