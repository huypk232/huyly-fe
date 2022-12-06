import bcrypt
from .base import DBConnectionHandler
import model.cart_item as cart_item_entity
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text


class CartItemRepository:
    @classmethod
    def get_by_cart_id(cls, cart_id) -> List[cart_item_entity.CartItem]:
        with DBConnectionHandler() as db_connection:
            try:
                cart_items = (
                    db_connection.session.query(cart_item_entity.CartItem)
                    .filter_by(cart_id=cart_id)
                    .all()
                )
                return cart_items

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()


    @classmethod
    def get_by_id(cls, cart_item_id) -> cart_item_entity.CartItem:
        with DBConnectionHandler() as db_connection:
            try:
                cart_item = (
                    db_connection.session.query(cart_item_entity.CartItem)
                    .filter_by(id=cart_item_id)
                    .one()
                )
                return cart_item

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()


    @classmethod
    def create_cart_item(cls, cart_id, product_id, price, quantity) -> List[cart_item_entity.CartItem]:

        with DBConnectionHandler() as db_connection:
            try:
                cart_item = cart_item_entity.CartItem(cart_id=cart_id, product_id=product_id, customer_price=price,
                                                       quantity=quantity)
                db_connection.session.add(cart_item)
                db_connection.session.commit()
                return cart_item

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()


    @classmethod
    def update_cart_item(cls, item_id, price, quantity) -> cart_item_entity.CartItem:
        with DBConnectionHandler() as db_connection:
            try:
                cart_item = cls.get_by_id(item_id)
                cart_item.quantity = quantity
                cart_item.customer_price = price
                db_connection.session.commit()
                return cart_item
            except NoResultFound:
                return None
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()

