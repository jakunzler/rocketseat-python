from datetime import datetime
from sqlalchemy import or_, update
from sqlalchemy.orm.exc import NoResultFound
from src.models.entities.user import User
from src.models.interfaces.user_repository import UserRepositoryInterface
from src.errors.types.http_bad_request import HttpBadRequestError

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
                    .filter(User.username == username)
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
                    .filter(User.email == email)
                    .one()
                )
                return user_info
            except NoResultFound:
                return None

    def get_user_by_id(self, user_id: int) -> User:
        with self.__db_connection as database:
            try:
                user_info = (
                    database.session
                    .query(User)
                    .filter(User.id == user_id)
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
                query = database.session.query(User)

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

    def delete_user(self, user_id: int) -> bool:
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
