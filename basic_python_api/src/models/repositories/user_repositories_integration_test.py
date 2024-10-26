import pytest
from src.configs.connection import db_connection_handler
from .user_repository import UserRepository

@pytest.mark.skip(reason="interacao com o banco")
def test_create_user():
    # Assess the function create_user from UserRepository
    model = UserRepository(db_connection_handler.connect_to_db())
    print(model)
    assert model.create_user("test", "test", "test") == True
    
@pytest.mark.skip(reason="interacao com o banco")
def test_get_user_by_username():
    pass
