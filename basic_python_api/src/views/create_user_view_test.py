import pytest
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from .create_user_view import CreateUserView

class MockController:
    def create(self, username, password):
        return { "alguma": "coisa" }

def test_handle_create_user():
    body = {
        "username": "MyUsername",
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    create_user_view = CreateUserView(mock_controller)

    response = create_user_view.handle(request)

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': {'alguma': 'coisa'}}
    assert response.status_code == 201

def test_handle_create_user_with_validation_error():
    body = {
        "password": "MyPassword"
    }
    request = HttpRequest(body=body)

    mock_controller = MockController()
    create_user_view = CreateUserView(mock_controller)

    with pytest.raises(Exception):
        create_user_view.handle(request)
