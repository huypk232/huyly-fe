import bcrypt
from .base import DBConnectionHandler
import model.cart as cart_entity
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text


class CartRepository:
    @classmethod
    def insert_carts(cls, data) -> cart_entity.Cart:
        with DBConnectionHandler() as db_connection:
            try:
                cart = cart_entity.Cart(owner_id=data['owner_id'])
                db_connection.session.add(cart)
                db_connection.session.commit()
                return cart
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()

    # @classmethod
    # def get_by_id(cls, id) -> model.Cart:
    #     db_conn = DBConnectionHandler()
    #     datas = db_conn.execute(text("""SELECT * FROM carts WHERE id = """))
    #     print(type(datas))
    #     json_datas = {}
    #     for data in datas:
    #         print(type(data))
    #         json_datas[str(data.name)] = User(
    #             data.id, data.name, data.email).get_as_json()
    #     return json_datas


    @classmethod
    def select(cls, data) -> List[cart_entity.Cart]:

        with DBConnectionHandler() as db_connection:
            try:
                user = (
                    db_connection.session.query(cart_entity.cart)
                    .filter_by(email=str(data["email"]))
                    .one()
                )
                if bcrypt.checkpw(str(data["password"]).encode('utf-8'), user.password):
                    return user
                else:
                    return None

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
    def get_by_id(cls, id: int) -> cart_entity.Cart:
        db_conn = DBConnectionHandler()
        data = db_conn.execute(text("""SELECT * FROM carts WHERE id={}""".format(id))).fetchone()
        # json_data = User(id, data.name, data.email, data.password).get_as_json()
        return data

    #Not done yet
    @classmethod
    def get_carts(cls, created_by_id) -> cart_entity.Cart:
        with DBConnectionHandler() as db_connection:
            try:
                data = db_connection.session.query(cart_entity.Cart).filter_by(owner_id=created_by_id).all()

                return data

            except NoResultFound:
                return data
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()


    @classmethod
    def update_cart(cls, item_id, price, quantity) -> cart_entity.Cart:
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


    @classmethod
    def drop_row(cls, id) -> bool:

        with DBConnectionHandler() as db_connection:
            dropable = False
            try:
                if id:
                    data = db_connection.session.query(
                        cart_entity.cart).filter_by(id=id).one()
                    db_connection.session.delete(data)
                    db_connection.session.commit()
            except NoResultFound:
                return dropable
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.expunge_all()
                db_connection.session.close()
