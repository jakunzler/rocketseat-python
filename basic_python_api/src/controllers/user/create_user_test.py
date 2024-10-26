from .create_user import CreateUser

class MockUserRepository:
    def __init__(self) -> None:
        self.create_user_attributes = {}
    
    def create_user(self, username, password) -> None:
        self.create_user_attributes["username"] = username
        self.create_user_attributes["password"] = password


def test_create():
    repository = MockUserRepository()
    controller = CreateUser(repository)

    username = "olaMundo"
    password = "myPassword"

    response = controller.create(username, password)

    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.create_user_attributes["username"] == username
    assert repository.create_user_attributes["password"] is not None
    assert repository.create_user_attributes["password"] != password