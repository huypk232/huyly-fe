import bcrypt
from .base import DBConnectionHandler
import model.product as product_entity
from typing import List
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.sql.expression import text


class ProductRepository:
    @classmethod
    def insert(cls, data) -> product_entity.Product:
        with DBConnectionHandler() as db_connection:
            try:
                product = product_entity.Product(
                    name=data['name'],
                    code=data['code'],
                    price=data['price'],
                    img_url=data['img_url'],
                    uom=data['uom'],
                    stock=data['stock'],
                    owner_id=data['owner_id'],
                )
                db_connection.session.add(product)
                db_connection.session.commit()
                return product
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()


    @classmethod
    def get_all(cls) -> product_entity.Product:
        with DBConnectionHandler() as db_connection:
            try:
                products = db_connection.session.query(product_entity.Product).all()
                return products
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()\


    @classmethod
    def get_by_id(cls, product_id) -> product_entity.Product:
        with DBConnectionHandler() as db_connection:
            try:
                product = db_connection.session.query(product_entity.Product).filter_by(id=product_id).one()
                return product
            except Exception as ex:
                db_connection.session.rollback()
                print(ex)
                raise
            finally:
                db_connection.session.close()
