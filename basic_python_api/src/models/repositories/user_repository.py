import os
from dotenv import load_dotenv

load_dotenv()

from datetime import datetime
from sqlalchemy import or_, update
from sqlalchemy.orm.exc import NoResultFound
from src.models.entities.user import User
from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.password_handler import PasswordHandler
from src.errors.types.http_bad_request import HttpBadRequestError

class UserRepository(UserRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        self.__password_handle = PasswordHandler()

    def authenticate_user(self, username: str, email: str, password: str) -> bool:
        with self.__db_connection as database:
            try:
                user = (
                    database.session.query(User)
                    .filter(
                        or_(User.username == username, User.email == email)
                    )
                    .one()
                )

                if not self.__password_handle.check_password(password, user.password):
                    raise HttpBadRequestError("Invalid credentials.")

                if user is None:
                    return None

                if user.first_login_date is None:
                    user.first_login_date = datetime.now()
                    user.last_login_date = datetime.now()
                    self.update_user(user.to_dict())
                else:
                    user.last_login_date = datetime.now()
                    self.update_user(user.to_dict())

                return user
            except NoResultFound:
                return None

    def create_user(
        self,
        username: str,
        email: str,
        password: str,
    ) -> User:
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
                return database.session.query(User).filter(User.username == username).one()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_user_by_username(self, username: str) -> User:
        with self.__db_connection as database:
            try:
                user_info = (
                    database.session
                    .query(User)
                    .filter(User.username == username, User.deleted_by.is_(None))
                    .one()
                )
                return user_info
            except NoResultFound:
                return None

    def get_user_by_email(self, email: str) -> User:
        with self.__db_connection as database:
            try:
                user_info = (
                    database.session
                    .query(User)
                    .filter(User.email == email, User.deleted_by.is_(None))
                    .one()
                )
                return user_info
            except NoResultFound:
                return None

    def get_user_by_id(self, user_id: str) -> User:
        with self.__db_connection as database:
            try:
                user_info = (
                    database.session
                    .query(User)
                    .filter(User.id == user_id, User.deleted_by.is_(None))
                    .one()
                )
                return user_info
            except NoResultFound:
                return None

    def get_all_users(self, page: int = None, page_length: int = None) -> list[User]:
        """
        Obtém uma lista de usuários com paginação.

        :param page: Número da página (começa em 1).
        :param page_length: Número de usuários por página.
        :return: Lista paginada de usuários.
        """

        if not isinstance(page, int) and page is not None:
            raise HttpBadRequestError("page must be integer.")
        if not isinstance(page_length, int) and page_length is not None:
            raise HttpBadRequestError("page_length must be integer.")
        if not page:
            page = 1
        elif page < 1:
            raise HttpBadRequestError("page must be greater than 0.")

        with self.__db_connection as database:
            try:
                query = (
                    database.session.query(User)
                        .filter(User.deleted_by.is_(None))
                )

                if page_length:
                    if page_length < 1:
                        raise HttpBadRequestError("page_length must be greater than 0.")
                    offset = (page - 1) * page_length
                    query = query.limit(page_length).offset(offset)

                paginated_users = query.all()

                return paginated_users if paginated_users else []
            except NoResultFound:
                return []

    def update_user(self, partial_user: User) -> User:
        with self.__db_connection as database:
            try:
                partial_user["updated_at"] = datetime.now()

                database.session.execute(
                    update(User),
                    [
                        partial_user
                    ]
                )
                database.session.commit()
                return (
                    database.session
                    .query(User)
                    .filter(User.id == partial_user["id"])
                    .one()
                )
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_user(self, current_user_id: str, user_id: str) -> bool:
        if bool(os.environ.get("LOGICAL_DELETE")) is True:
            with self.__db_connection as database:
                try:
                    database.session.execute(
                        update(User)
                        .where(User.id == user_id)
                        .values(deleted_at=datetime.now(), deleted_by=current_user_id)
                    )
                    database.session.commit()
                except Exception as exception:
                    database.session.rollback()
                    raise exception
        else:
            with self.__db_connection as database:
                try:
                    user_info = (
                        database.session
                        .query(User)
                        .filter(User.id == user_id)
                        .one()
                    )
                    database.session.delete(user_info)
                    database.session.commit()
                except Exception as exception:
                    database.session.rollback()
                    raise exception
