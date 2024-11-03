from src.views.http_types.http_response import HttpResponse
from .logout_user_view import LogoutUserView

class MockController:
    def logout_user(self):
        return "Logout Successful"
    
def test_handle_logout_user():

    mock_controller = MockController()
    logout_user_view = LogoutUserView(mock_controller)

    response = logout_user_view.handle({})

    assert isinstance(response, HttpResponse)
    assert response.body == {'data': 'Logout Successful'}
    assert response.status_code == 200