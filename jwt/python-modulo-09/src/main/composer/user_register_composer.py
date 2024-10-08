from src.models.settings.connection import DBConnectionHandler
from src.models.repositories.user_repository import UserRepository
from src.controllers.create_user import CreateUser
from src.views.user_register_view import UserRegisterView

def user_register_composer():
    conn = DBConnectionHandler()
    model = UserRepository(conn.connect_to_db())
    controller = CreateUser(model)
    view = UserRegisterView(controller)

    return view
