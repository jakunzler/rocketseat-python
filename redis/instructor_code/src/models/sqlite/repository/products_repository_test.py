import pytest
from src.models.sqlite.settings.connection import SqliteConnectionHandle
from .products_repository import ProductsRepository

conn_handle = SqliteConnectionHandle()
conn = conn_handle.connect()

@pytest.mark.skip(reason="interacao com o banco")
def test_insert_product():
    repo = ProductsRepository(conn)

    name = "algumaCoisa2"
    price = 12.34
    quantity = 8

    repo.insert_product(name, price, quantity)

@pytest.mark.skip(reason="interacao com o banco")
def test_find_product():
    repo = ProductsRepository(conn)

    name = "algumaCoisa2"
    response = repo.find_product_by_name(name)
    print(response)
    print(type(response))
