import pytest
from src.drivers.password_handler import PasswordHandler
from src.controllers.user.login_user import LoginUser

username = "meuUsername"
email = "meuEmail"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_password(password)

class User():
    id = 'MinhaStringUUID'
    username = "meuUsername"
    email = "meuEmail"
    password = hashed_password

class MockUserRepository:
    def __init__(self, name, mail, passwd) -> None:
        self.username = name
        self.email = mail
        self.password = passwd

    def get_user_by_username(self, us_name: str) -> User: # pylint: disable=unused-argument
        return User

    def get_user_by_email(self, us_email: str) -> User: # pylint: disable=unused-argument
        return User

def test_create():
    user_repository = MockUserRepository(username, email, hashed_password)
    login_creator = LoginUser(user_repository)
    response = login_creator.login_user(username, email, password)

    assert response["access"] == True
    assert response["username"] == username
    assert response["token"] is not None

def test_create_with_wrong_password():
    login_creator = LoginUser(MockUserRepository(username, email, password))

    with pytest.raises(Exception):
        login_creator.login_user(username, email, "algumaSenha")
