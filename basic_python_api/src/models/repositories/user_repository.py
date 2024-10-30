from datetime import datetime
from sqlalchemy import or_
from sqlalchemy.orm.exc import NoResultFound
from src.models.entities.user import User
from src.models.interfaces.user_repository import UserRepositoryInterface

class UserRepository(UserRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        
    def authenticate_user(self, username: str, email: str, password: str) -> bool:
        with self.__db_connection as database:
            try:
                (
                    database.session.query(User)
                    .filter(
                        or_(User.username == username, User.email == email),
                        User.password == password
                    )
                    .one()
                )
                return True
            except NoResultFound:
                return False
            
    def set_first_login_date(self, user_id: int) -> None:
        with self.__db_connection as database:
            try:
                user = database.session.query(User).get(user_id)
                user.first_login_date = datetime.now()
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
    ) -> None:
        print(username, email, password)
        print(self.__db_connection)
        with self.__db_connection as database:
            try:
                user_info = User(
                    username=username,
                    email=email,
                    password=password,
                    created_at=datetime.now(),
                )
                database.session.add(user_info)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_user_by_username(self, username: str) -> User:
        with self.__db_connection as database:
            try:
                user_info = (
                    database.session
                    .query(User)
                    .filter(User.username == username)
                    .one()
                )
                return user_info
            except NoResultFound:
                return None
            
    def get_user_by_id(self, user_id: int) -> User:
        with self.__db_connection as database:
            try:
                user_info = database.session.query(User).get(user_id)
                return user_info
            except NoResultFound:
                return None
            
    def get_all_users(self) -> list:
        with self.__db_connection as database:
            try:
                all_users = database.session.query(User).all()
                return all_users
            except NoResultFound:
                return None

    def update_user(
        self,
        user_id: int,
        first_name: str,
        last_name: str,
        username: str,
        email: str,
        password: str,
        is_admin: bool,
    ) -> None:
        with self.__db_connection as database:
            try:
                user_info = User(
                    id=user_id,
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    email=email,
                    password=password,
                    is_admin=is_admin,
                )
                database.session.add(user_info)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_user(self, user_id: int) -> None:
        with self.__db_connection as database:
            try:
                user_info = database.session.query(User).get(user_id)
                database.session.delete(user_info)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception