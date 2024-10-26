import pytest
from src.configs.connection import db_connection_handler
from .user_repository import UserRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interacao com o banco")
def test_create_user():
    # Assess the function create_user from UserRepository
    assert True


@pytest.mark.skip(reason="interacao com o banco")
def test_get_user_by_username():
    pass
