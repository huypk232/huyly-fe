import bcrypt
from .base import DBConnectionHandler
import model.order as order_entity
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text


class OrderRepository:
    @classmethod
    def insert_order(cls, data) -> order_entity.Order:
        with DBConnectionHandler() as db_connection:
            try:

                new_order = order_entity.Order(code=data['code'], cart_id=data['cart_id'], owner_id=data['owner_id'])
                db_connection.session.add(new_order)
                db_connection.session.commit()
                db_connection.session.expunge_all()
                return new_order
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()


    @classmethod
    def get_orders(cls, owner_id) -> List[order_entity.Order]:
        with DBConnectionHandler() as db_connection:
            try:
                orders = (
                    db_connection.session.query(order_entity.Order)
                    .filter_by(owner_id=owner_id)
                    .all()
                )
                return orders

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
    def get_by_id(cls, order_id) -> order_entity.Order:
        with DBConnectionHandler() as db_connection:
            try:
                order = (
                    db_connection.session.query(order_entity.Order)
                    .filter_by(id=order_id)
                    .one()
                )
                return order

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
    def update(cls, data) -> order_entity.Order:
        with DBConnectionHandler() as db_connection:
            try:
                order = cls.get_by_id(cls, data['order_id'])
                order.status = data['status']
                db_connection.session.commit()
                return order

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()
