import bcrypt
from .base import DBConnectionHandler
import model.order_item as order_item_entity
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text


class OrderItemRepository:
    @classmethod
    def insert_item(cls, order_id, product_id, customer_price, quantity) -> order_item_entity.OrderItem:
        with DBConnectionHandler() as db_connection:
            try:
                order_item = order_item_entity.OrderItem(order_id=order_id, product_id=product_id, customer_price=customer_price,
                                                      quantity=quantity)
                db_connection.session.add(order_item)
                db_connection.session.commit()
                return order_item

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
    def get_by_id(cls, item_id) -> order_item_entity.OrderItem:
        with DBConnectionHandler() as db_connection:
            try:
                order_item = (
                    db_connection.session.query(order_item_entity.OrderItem)
                    .filter_by(id=item_id)
                    .one()
                )
                return order_item

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
    def get_by_order_id(cls, order_id) -> List[order_item_entity.OrderItem]:
        with DBConnectionHandler() as db_connection:
            try:
                order_items = (
                    db_connection.session.query(order_item_entity.OrderItem)
                    .filter_by(order_id=order_id)
                    .all()
                )
                return order_items

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()
