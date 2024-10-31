from typing import Dict, Tuple
from src.models.interfaces.user_repository import UserRepositoryInterface
from src.drivers.jwt_handler import JwtHandler
from src.drivers.password_handler import PasswordHandler
from src.errors.types.http_bad_request import HttpBadRequestError
from src.errors.types.http_not_found import HttpNotFoundError
from ..interfaces.user.login_user import LoginUserInterface


class LoginUser(LoginUserInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository
        self.__jwt_handler = JwtHandler()
        self.__password_handle = PasswordHandler()

    def login_user(self, username: str, email: str, password: str) -> Dict:        
        if username:
            user = self.__find_by_username(username)
        elif email:
            user = self.__find_by_email(email)
        else:
            raise HttpBadRequestError("Username or Email is required")

        user_id = user.id
        hashed_password = user.password

        self.__verify_correct_password(password, hashed_password)
        token = self.__create_jwt_token(user_id)
        return self.__format_response(username, token)

    def __find_by_username(self, username: str) -> Tuple[str, str, str]:
        user = self.__user_repository.get_user_by_username(username)
        if not user: raise HttpNotFoundError("User not found")

        return user
    
    def __find_by_email(self, email: str) -> Tuple[str, str, str]:
        user = self.__user_repository.get_user_by_email(email)
        if not user: raise HttpNotFoundError("User not found")

        return user

    def __verify_correct_password(self, password: str, hashed_password: str) -> None:
        is_password_correct = self.__password_handle.check_password(password, hashed_password)
        if not is_password_correct: raise HttpBadRequestError("Wrong Password")

    def __create_jwt_token(self, user_id: str) -> str:
        payload = { "user_id": user_id }
        token = self.__jwt_handler.create_jwt_token(payload)
        return token

    def __format_response(self, username: str, token: str) -> Dict:
        return {
            "access": True,
            "username": username,
            "token": token
        }
