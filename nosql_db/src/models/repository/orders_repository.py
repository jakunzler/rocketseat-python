"""
This module is used to interact with the orders collection in the MongoDB database.
"""

from pymongo import errors

from src.models.connection.connection_handler import DBConnectionHandler

class OrdersRepository:
    """
    This class is used to interact with the orders collection in the MongoDB database.
    """
    def __init__(self, connection_handler: DBConnectionHandler) -> None:
        self.__collection_name = 'orders'
        self.__connection_handler = connection_handler

    def insert_document(self, document: dict) -> None:
        """
        Insert a document into the orders collection.
        """
        try:
            collection = self.__connection_handler.get_collection(self.__collection_name)
            collection.insert_one(document)
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f'Failed to insert document into the orders collection: {e}'
                ) from e

    def get_document(self, document_id: str) -> dict:
        """
        Get a document from the orders collection.
        """
        try:
            collection = self.__connection_handler.get_collection(self.__collection_name)
            document = collection.find_one({'_id': document_id})
            return document
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f'Failed to get document from the orders collection: {e}'
                ) from e

    def get_all_documents(self) -> list[dict]:
        """
        Get all documents from the orders collection.
        """
        try:
            collection = self.__connection_handler.get_collection(self.__collection_name)
            documents = list(collection.find())
            return documents
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f'Failed to get all documents from the orders collection: {e}'
                ) from e

    def update_document(self, document_id: str, document: dict) -> None:
        """
        Update a document in the orders collection.
        """
        try:
            collection = self.__connection_handler.get_collection(self.__collection_name)
            collection.update_one({'_id': document_id}, {'$set': document})
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f'Failed to update document in the orders collection: {e}'
                ) from e

    def delete_document(self, document_id: str) -> None:
        """
        Delete a document from the orders collection.
        """
        try:
            collection = self.__connection_handler.get_collection(self.__collection_name)
            collection.delete_one({'_id': document_id})
        except errors.OperationFailure as e:
            raise errors.OperationFailure(
                f'Failed to delete document from the orders collection: {e}'
                ) from e
