"""
This module is used to interact with the orders collection in the MongoDB database.
"""

from pymongo import errors

from src.models.connection.connection_handler import DBConnectionHandler


class OrdersRepository:
    """
    This class is used to interact with the orders collection in the MongoDB database.
    """

    def __init__(self, db_connection: DBConnectionHandler) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        """
        Insert a document into the orders collection.
        """
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            collection.insert_one(document)
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f"Failed to insert document into the orders collection: {e}"
            ) from e

    def insert_many_documents(self, documents: list[dict]) -> None:
        """
        Insert many documents into the orders collection.
        """
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            collection.insert_many(documents)
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f"Failed to insert many documents into the orders collection: {e}"
            ) from e

    def get_document(self, doc_filter: dict) -> dict:
        """
        Get a document from the orders collection.
        """
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            document = collection.find_one(doc_filter)
            return document
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f"Failed to get document from the orders collection: {e}"
            ) from e

    def get_all_documents(self) -> list[dict]:
        """
        Get all documents from the orders collection.
        """
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            documents = list(collection.find())
            return documents
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f"Failed to get all documents from the orders collection: {e}"
            ) from e

    def update_document(self, doc_filter: dict, document: dict) -> None:
        """
        Update a document in the orders collection.
        """
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            collection.update_one(doc_filter, {"$set": document})
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f"Failed to update document in the orders collection: {e}"
            ) from e

    def delete_document(self, doc_filter: dict) -> None:
        """
        Delete a document from the orders collection.
        """
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            collection.delete_one(doc_filter)
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f"Failed to delete document from the orders collection: {e}"
            ) from e

    def delete_all_documents(self) -> None:
        """
        Delete all documents from the orders collection.
        """
        try:
            collection = self.__db_connection.get_collection(self.__collection_name)
            collection.delete_many({})
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f"Failed to delete all documents from the orders collection: {e}"
            ) from e
