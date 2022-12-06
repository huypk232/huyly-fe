from sqlalchemy.sql.expression import null
from flask_login import login_manager
from flask import session
import jwt
import bcrypt
import datetime
import repository as repo


class User:
    def __init__(self):
        pass

    def check_email_existed(self, email):
        res = self.user_repository.select_by_email(email)
        if res is None:
            return True
        else:
            return False


    @classmethod
    def register(cls, email, password, role_id):
        new_user = repo.UserRepository.insert_user(email, password, role_id)
        return {"user": new_user}

    @classmethod
    def login(cls, data):
        # user = self.user_repository.select(data)
        user = repository.UserRepository.select(data)
        if user is not None:
            token = jwt.encode({
                "email": data["email"],
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=1)},
                "secretkey",
                algorithm="HS256"
            )
            session["token"] = token
            return user
        return None

    # @classmethod
    # def loaded_user(cls, user_id):
    #     return repository.UserRepository.loaded_user(user_id)


    @classmethod
    def get_users(cls, role_id):
        users = repo.UserRepository.get_by_role_id(role_id)
        return {
            'users': users
        }


    @classmethod
    def get_user_detail(cls, user_id):
        user = repo.UserRepository.get_by_id(user_id)
        return user.json()
