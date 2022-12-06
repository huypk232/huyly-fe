import bcrypt
from .base import DBConnectionHandler
import model.category as category_entity
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text


class CategoryRepository:
    # @classmethod
    # def get_all(cls) -> category_entity.Category:
    #     with DBConnectionHandler() as db_connection:
    #         try:
    #             categories = (
    #                 db_connection.session.query(category_entity.Category)
    #                 .all()
    #             )
    #             return ca
    #         except Exception as ex:
    #             db_connection.session.rollback()
    #             print(ex)
    #             raise
    #         finally:
    #             db_connection.session.close()

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
    def get_all(cls) -> List[category_entity.Category]:

        with DBConnectionHandler() as db_connection:
            try:
                categories = (
                    db_connection.session.query(category_entity.Category)
                    .all()
                )
                return categories

            except NoResultFound:
                return []
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

    @classmethod
    def get_by_id(cls, id: int) -> category_entity.Category:
        db_conn = DBConnectionHandler()
        data = db_conn.execute(text("""SELECT * FROM carts WHERE id={}""".format(id))).fetchone()
        # json_data = User(id, data.name, data.email, data.password).get_as_json()
        return data

    @classmethod
    def select_by_email(cls, email: str) -> category_entity.Category:
        db_conn = DBConnectionHandler()
        data = db_conn.execute(
            text("""SELECT * FROM users WHERE email='{}'""".format(email))).fetchone()
        if data is None:
            return None
        return category_entity.Category(id, data.name, data.email,
                    data.password).get_as_json()


    @classmethod
    def get_all(cls) -> category_entity.Category:
        with DBConnectionHandler() as db_connection:
            try:
                data = None
                if id:
                    # Select user by id
                    with DBConnectionHandler() as db_connection:
                        data = (
                            db_connection.session.query(category_entity.Category)
                            .all()
                        )

                return data

            except NoResultFound:
                return data
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()

