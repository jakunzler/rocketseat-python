from src.configs.connection import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_user import LoginUser
from src.views.login_creator_view import LoginCreatorView

def login_creator_composer():
    conn = db_connection_handler
    model = UserRepository(conn.connect_to_db())
    controller = LoginUser(model)
    view = LoginCreatorView(controller)

    return view
