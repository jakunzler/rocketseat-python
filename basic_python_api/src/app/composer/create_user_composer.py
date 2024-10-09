from src.configs.connection import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.create_user import CreateUser
from src.views.user_register_view import UserRegisterView

def create_user_composer():
    conn = db_connection_handler
    model = UserRepository(conn.connect_to_db())
    controller = CreateUser(model)
    view = UserRegisterView(controller)

    return view
