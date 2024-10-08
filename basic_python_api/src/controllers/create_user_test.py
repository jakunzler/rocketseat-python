from .create_user import CreateUser

class MockUserRepository:
    def __init__(self) -> None:
        self.registry_user_attributes = {}
    
    def registry_user(self, username, password) -> None:
        self.registry_user_attributes["username"] = username
        self.registry_user_attributes["password"] = password


def test_registry():
    repository = MockUserRepository()
    controller = CreateUser(repository)

    username = "olaMundo"
    password = "myPassword"

    response = controller.create(username, password)

    assert response["type"] == "User"
    assert response["username"] == username

    assert repository.registry_user_attributes["username"] == username
    assert repository.registry_user_attributes["password"] is not None
    assert repository.registry_user_attributes["password"] != password