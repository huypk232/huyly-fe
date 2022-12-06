from flask import Blueprint
from flask_restful import Api

from .cart import cart_api
from .category import category_api
from .customer import customer_api
from .dashboard import dashboard_api
from .order import order_api
from .partner import partner_api
from .product import product_api
from .vendor import vendor_api
from .user import user_api

api = Blueprint("api", __name__, static_folder="static",
                   template_folder="templates", url_prefix="/api/v1")
api.register_blueprint(cart_api, url_prefix="/carts")
api.register_blueprint(customer_api, url_prefix="/customers")
api.register_blueprint(dashboard_api, url_prefix="/")
api.register_blueprint(order_api, url_prefix="/orders")
api.register_blueprint(partner_api, url_prefix="/partners")
api.register_blueprint(product_api, url_prefix="/products")
api.register_blueprint(category_api, url_prefix="/categories")
api.register_blueprint(vendor_api, url_prefix="/vendors")
api.register_blueprint(user_api, url_prefix="/users")
# api.register_blueprint(user_bp, url_prefix="/api/v1/users")

# ui_bp = Blueprint("ui", __name__, static_folder="static",
#                   template_folder="templates")
# ui_bp.register_blueprint(auth_ui, url_prefix="")
# ui_bp.register_blueprint(fc_ui, url_prefix="/football_clubs")
# ui_bp.register_blueprint(group_ui, url_prefix="/groups")
# ui_bp.register_blueprint(league_ui, url_prefix="/leagues")
# ui_bp.register_blueprint(per_ui, url_prefix="/permissions")
# ui_bp.register_blueprint(player_ui, url_prefix="/players")
# ui_bp.register_blueprint(user_ui, url_prefix="/users")
