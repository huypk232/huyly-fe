import model.warehouse as warehouse_model
from .base import DBConnectionHandler
# from database.model import model.User as model.UserModel
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text


class WarehouseRepository:
    @classmethod
    def insert_warehouse(cls, name, address, owner_id) -> warehouse_model.Warehouse:
        with DBConnectionHandler() as db_connection:
            try:
                warehouse = warehouse_model.Warehouse(name=name, address=address, owner_id=owner_id)
                db_connection.session.add(warehouse)
                db_connection.session.commit()
                return warehouse
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()


    @classmethod
    def get_by_owner_id(cls, owner_id) -> warehouse_model.Warehouse:
        with DBConnectionHandler() as db_connection:
            try:
                warehouses = (
                    db_connection.session.query(warehouse_model.Warehouse)
                    .filter_by(owner_id=owner_id)
                    .all()
                )
                return warehouses
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_by_id(cls, warehouse_id) -> warehouse_model:
        with DBConnectionHandler() as db_connection:
            try:
                warehouse = (
                    db_connection.session.query(warehouse_model)
                    .filter_by(id=warehouse_id)
                    .one()
                )
                return warehouse

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

    # @classmethod
    # def select_by_id(cls, id: int) -> model.User:
    #     db_conn = DBConnectionHandler()
    #     data = db_conn.execute(text("""SELECT * FROM model.Users WHERE id={}""".format(id))).fetchone()
    #     json_data = model.User(id, data.name, data.email, data.password).get_as_json()
    #     return json_data
    #
    # @classmethod
    # def select_by_email(cls, email: str) -> model.User:
    #     db_conn = DBConnectionHandler()
    #     data = db_conn.execute(
    #         text("""SELECT * FROM model.Users WHERE email='{}'""".format(email))).fetchone()
    #     if data is None:
    #         return None
    #     return model.User(id, data.name, data.email,
    #                       data.password).get_as_json()
