from pymongo import MongoClient, MongoClientError, errors


class DBConnectionHandler:
    """
    This class is used to connect to the MongoDB database.
    """

    def __init__(
            self,
            user: str,
            password: str,
            host: str,
            port: int,
            database: str
        ) -> None:
        self.__connection_string = f"mongodb://{user}:{password}@{host}:{port}/?authSource=admin"
        self.__database = database
        self.__client = None
        self.__db_connection = None

    def connect_to_db(self):
        """
        Connect to the MongoDB database.
        """
        try:
            self.__client = MongoClient(self.__connection_string)
            self.__db_connection = self.__client[self.__database]
        except errors.ConnectionFailure as e:
            raise MongoClientError(f'Failed to connect to the MongoDB database: {e}') from e

    def get_db_connection(self):
        """
        Get the MongoDB client.
        """
        return self.__client

    def get_collection(self, collection_name: str):
        """
        Get the MongoDB collection.
        """
        return self.__db_connection[collection_name]
    
    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        self.__client.close()