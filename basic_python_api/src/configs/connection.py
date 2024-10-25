from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

class DBConnectionHandler:
    def __init__(self) -> None:
        self.db_folder = os.path.join(os.getcwd(), 'src/db')
        os.makedirs(self.db_folder, exist_ok=True)
        self.__connection_string = f"sqlite:///{self.db_folder}/storage.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self, Base=None):
        self.__engine = create_engine(self.__connection_string)
        if Base:
            Base.metadata.create_all(self.__engine)

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_maker = sessionmaker()

        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


db_connection_handler = DBConnectionHandler()
