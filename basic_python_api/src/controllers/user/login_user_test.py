import pytest
from src.drivers.password_handler import PasswordHandler
from src.controllers.user.login_user import LoginUser

username = "meuUsername"
password = "minhaSenha"
hashed_password = PasswordHandler().encrypt_password(password)

class MockUserRepository:
    def __init__(self, name, passwd) -> None:
        self.username = name
        self.password = passwd
    
    def get_user_by_username(self, us_name: str) -> tuple:
        return ('MinhaStringUUID', us_name, self.password)

def test_create():
    user_repository = MockUserRepository(username, hashed_password)
    login_creator = LoginUser(user_repository)
    response = login_creator.login_user(username, password)

    assert response["access"] == True
    assert response["username"] == username
    assert response["token"] is not None

def test_create_with_wrong_password():
    login_creator = LoginUser(MockUserRepository(username, password))

    with pytest.raises(Exception):
        login_creator.login_user(username, "algumaSenha")
