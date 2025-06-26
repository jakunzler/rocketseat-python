"""
This module is used to test the orders repository.
"""

import pytest

from src.models.connection.connection_handler import DBConnectionHandler
from src.models.repository.orders_repository import OrdersRepository

@pytest.fixture
def __connection_handler():
    """
    This fixture is used to create a connection to the MongoDB database.
    """
    return DBConnectionHandler().connect_to_db()

@pytest.fixture
def __connection_driver(connection_handler = __connection_handler):
    """
    This fixture is used to create a connection to the MongoDB database.
    """
    return connection_handler.get_db_connection()

@pytest.fixture
def __orders_repository(connection_driver = __connection_driver):
    """
    This fixture is used to create an orders repository.
    """
    return OrdersRepository(connection_driver)
  
def test_create_db(connection_handler = __connection_handler):
    """
    This test is used to test the create_db method of the orders repository.
    """
    connection_handler.create_db()
    assert connection_handler.get_db_connection() is not None


def test_insert_document(orders_repository = __orders_repository):
    """
    This test is used to test the insert_document method of the orders repository.
    """
    orders_repository.insert_document({'name': 'John Doe', 'email': 'john.doe@example.com'})
    assert orders_repository.get_document({'name': 'John Doe'}) is not None
