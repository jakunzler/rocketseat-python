from src.configs.connection import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.create_user import CreateUser
from src.views.create_user_view import CreateUserView

def user_register_composer():
    conn = db_connection_handler
    model = UserRepository(conn.connect_to_db())
    controller = CreateUser(model)
    view = CreateUserView(controller)

    return view
