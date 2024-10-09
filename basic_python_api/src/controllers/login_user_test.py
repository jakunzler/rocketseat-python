import pytest
from src.drivers.password_handler import PasswordHandler
from src.controllers.login_user import LoginUser

username = "meuUsername"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_password(password)

class MockUserRepository:
    def get_user_by_username(self, username):
        return (10, username, hashed_password)

def test_create():
    login_creator = LoginUser(MockUserRepository())
    response = login_creator.login_user(username, password)

    assert response["access"] == True
    assert response["username"] == username
    assert response["token"] is not None

def test_create_with_wrong_password():
    login_creator = LoginUser(MockUserRepository())

    with pytest.raises(Exception):
        login_creator.login_user(username, "algumaSenha")
