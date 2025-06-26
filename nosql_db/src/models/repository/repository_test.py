"""
This module is used to test the orders repository.
"""

import pytest

from src.models.connection.connection_handler import DBConnectionHandler
from src.models.repository.orders_repository import OrdersRepository


@pytest.fixture
def connection_handler():
    """
    This fixture is used to create a connection to the MongoDB database.
    """
    conn = DBConnectionHandler()
    conn.connect_to_db()
    return conn


@pytest.fixture
def connection_driver(connection_handler):
    """
    This fixture is used to create a connection to the MongoDB database.
    """
    return connection_handler.get_db_connection()


@pytest.fixture
def orders_repository(connection_driver):
    """
    This fixture is used to create an orders repository.
    """
    return OrdersRepository(connection_driver)


@pytest.fixture(scope="function")
def clear_orders_collection(orders_repository):
    """
    This fixture is used to clear the orders collection.
    """
    orders_repository.delete_all_documents()


def test_insert_document(orders_repository, clear_orders_collection):
    """
    This test is used to test the insert_document method of the orders repository.
    """
    orders_repository.insert_document(
        {"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert orders_repository.get_document({"name": "John Doe"}) is not None


def test_insert_many_documents(orders_repository, clear_orders_collection):
    """
    This test is used to test the insert_many_documents method of the orders repository.
    """
    orders_repository.insert_many_documents(
        [
            {"name": "John Doe", "email": "john.doe@example.com"},
            {"name": "Jane Doe", "email": "jane.doe@example.com"},
        ]
    )
    assert orders_repository.get_document({"name": "John Doe"}) is not None
    assert orders_repository.get_document({"name": "Jane Doe"}) is not None


def test_get_document(orders_repository, clear_orders_collection):
    """
    This test is used to test the get_document method of the orders repository.
    """
    orders_repository.insert_document(
        {"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert orders_repository.get_document({"name": "John Doe"}) is not None


def test_get_all_documents(orders_repository, clear_orders_collection):
    """
    This test is used to test the get_all_documents method of the orders repository.
    """
    orders_repository.insert_many_documents(
        [
            {"name": "John Doe", "email": "john.doe@example.com"},
            {"name": "Jane Doe", "email": "jane.doe@example.com"},
        ]
    )
    assert len(orders_repository.get_all_documents()) == 2


def test_update_document(orders_repository, clear_orders_collection):
    """
    This test is used to test the update_document method of the orders repository.
    """
    orders_repository.insert_document(
        {"name": "John Doe", "email": "john.doe@example.com"}
    )
    orders_repository.update_document(
        {"name": "John Doe"}, {"name": "John Doe", "email": "john.doe@example.com"}
    )
    assert orders_repository.get_document({"name": "John Doe"}) is not None


def test_delete_document(orders_repository, clear_orders_collection):
    """
    This test is used to test the delete_document method of the orders repository.
    """
    orders_repository.insert_document(
        {"name": "John Doe", "email": "john.doe@example.com"}
    )
    orders_repository.delete_document({"name": "John Doe"})
    assert orders_repository.get_document({"name": "John Doe"}) is None
