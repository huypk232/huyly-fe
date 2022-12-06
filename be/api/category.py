import datetime

from service.auth import admin_login_required, UserAuth
from model.user import User
from model.listing import Listing
from model.trigger import Trigger
from model.order import Order
from model.orders_sync import OrdersSync
from model.postgres.listing_rating import ListingRating
from util.postgre import db
from blps.api.tasks.fire_triggers import LISTING_PAGE_SIZE, TRIGGER_PAGE_SIZE, DELIVERY_DAYS_OFFSET, ORDER_PAGE_SIZE

from google.cloud import ndb
from flask import request, make_response, redirect
from flask_restx import Namespace, Resource

api = Namespace('category', description='category api')


@api.route('/<')
class AdminLoginHandlers(Resource):
    def get(self):
        email = request.args.get('email').lower()
        password = request.args.get('password')
        user = UserAuth.validate_admin(email, password)
        if not user:
            resp = make_response({"error": "Bad email or password"}, 404)
            return resp

        resp = make_response({"admin_email": email})
        UserAuth.login_admin(resp, admin_email=email)

        return resp

    def post(self):
        email = request.form.get('email').lower()
        password = request.form.get('password')
        user = UserAuth.validate_admin(email, password)
        if not user:
            resp = make_response({"error": "Bad email or password"}, 404)
            return resp

        resp = make_response({"admin_email": email})
        UserAuth.login_admin(resp, admin_email = email)

        return resp

@api.route('/logout')
class LoginHandlers(Resource):
    def get(self):
        resp = make_response(redirect('/'))
        UserAuth.logout_admin(resp)

        return resp

@api.route('/search_user')
class UserSearchHandler(Resource):
    @admin_login_required
    def post(self):
        search_string = request.form.get("search").lower()
        match_result = User.search_users(search_string)
        if not match_result:
            resp = make_response({"message": "No such user, email or id is incorrect"}, 404)
            return resp
        reply = match_result.to_json(get_refresh_token=True)
        return make_response(reply)

@api.route('/get_last_user')
class LastUserHandler(Resource):
    @admin_login_required
    def get(self):
        match_result = User.get_new_users()
        users = [{"email":user.email,"id":user.key.id()} for user in match_result]
        reply = {"users": users}
        return make_response(reply, 200)

@api.route('/login_as')
class LoginAsHandlers(Resource):
    @admin_login_required
    def post(self):
        email = request.form.get('email').lower()
        # password = request.form.get('password')
        # user = User.auth_user_by_creds(email, password)
        user = User.query(User.email == email).get()
        if not user:
            resp = make_response({"error": "User not found"}, 404)
            return resp

        uid = user.key.id()
        resp = make_response({"uid": uid})
        UserAuth.login_user(resp, uid)

        return resp


@api.route("/delete_user/<int:user_id>")
class DeleteUserHandler(Resource):
    @admin_login_required
    def delete(self, user_id):
        user = User.get_by_id(user_id)
        if not user.spapi_refresh_token:
            listings = Listing.query(Listing.user_key == user.key).fetch(keys_only=True)
            for listing in listings:
                db.session.query(ListingRating).filter_by(listing_key=listing.id()).delete()
                db.session.commit()
            ndb.delete_multi(listings)
            ndb.delete_multi(
                Trigger.query(Trigger.user_key == user.key).fetch(keys_only=True)
            )
            ndb.delete_multi(
                Order.query(Order.user_key == user.key).fetch(keys_only=True)
            )
            ndb.delete_multi(
                OrdersSync.query(OrdersSync.user_key == user.key).fetch(keys_only=True)
            )
            user.key.delete()
            return make_response({"res": "success"})
        else:
            return make_response({"error": "refresh_token still exists"})


@api.route("/solic_sent_statistic")
class SolicSentExpect(Resource):
    @admin_login_required
    def get(self):
        days_delay = int(request.args.get("days_delay", "5"))
        user_id = request.args.get("user_id")
        user = User.get_by_id(int(user_id))
        refresh_token = user.spapi_refresh_token
        listings = Listing.query(Listing.user_key == user.key, Listing.triggers_active == True).fetch(LISTING_PAGE_SIZE)
        real_solics = []
        expect_solics = []
        error_orders = []
        for day_before in range(0, 30):
            now = datetime.datetime.now() - datetime.timedelta(day_before)
            real_solic = 0
            expect_solic = 0
            error_solic = []
            for l in listings:
                triggers = Trigger.query(Trigger.user_key == user.key, Trigger.listing_key == l.key).order(Trigger.num_of_items_max).fetch(TRIGGER_PAGE_SIZE)
                for t in triggers:
                    offset = days_delay
                    delta = datetime.timedelta(days=offset)
                    timeframe_from = now - delta
                    timeframe_from = timeframe_from.replace(hour=0, minute=0, second=0, microsecond=0)
                    timeframe_to = timeframe_from + datetime.timedelta(days=1)
                    expect_orders = Order.query(Order.user_key == user.key).filter(Order.asin == t.asin,
                                                                                   Order.solicitable_since > timeframe_from,
                                                                                   Order.solicitable_since < timeframe_to,
                                                                                   ).fetch(ORDER_PAGE_SIZE)
                    for o in expect_orders:
                        result = o.send_solic(refresh_token=refresh_token)
                        if result:
                            expect_solic += 1
                        else:
                            continue
                    real_orders = Order.query(Order.user_key == user.key).filter(Order.asin == t.asin,
                                                                                 Order.solic_sent_date > timeframe_from,
                                                                                 ).fetch(ORDER_PAGE_SIZE)
                    for o in real_orders:
                        if not (t.num_of_items_max >= o.num_of_items >= t.num_of_items_min and
                                o.solicitable_since <= timeframe_to):
                            continue
                        real_solic += 1
                    error_order_daily = Order.query(Order.user_key == user.key).filter(Order.asin == t.asin,
                                                                                       Order.solicitable_since > timeframe_from,
                                                                                       Order.solicitable_since < timeframe_to,
                                                                                       Order.solic_sent == False,
                                                                                       ).fetch(ORDER_PAGE_SIZE)
                    for o in error_order_daily:
                        error_solic.append(o.to_dict())
            expect_solics.append({"date": now, "total": expect_solic})
            real_solics.append({"date": now, "total": real_solic})
            error_orders.append({"date": now, "orders": error_solic})
        resp = {
            "expect": expect_solics,
            "real": real_solics,
            "error_order": error_orders
        }
        return make_response({"resp": resp})
