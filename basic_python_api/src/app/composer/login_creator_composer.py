from src.models.settings.connection import DBConnectionHandler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_user import LoginUser
from src.views.login_creator_view import LoginCreatorView

def login_creator_composer():
    conn = DBConnectionHandler()
    model = UserRepository(conn.connect_to_db())
    controller = LoginUser(model)
    view = LoginCreatorView(controller)

    return view
