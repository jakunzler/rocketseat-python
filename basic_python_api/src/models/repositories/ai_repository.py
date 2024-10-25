from datetime import datetime
from sqlalchemy.orm.exc import NoResultFound
from src.models.entities.ai import AI
from src.models.interfaces.ai_repository import AIRepositoryInterface

class AIRepository(AIRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection
        
    def create_ai(
        self,
        name: str,
        model: str,
    ) -> None:
        with self.__db_connection as database:
            try:
                ai_info = AI(
                    name=name,
                    model=model,
                    created_at=datetime.now(),
                )
                database.session.add(ai_info)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_ai_by_id(self, ai_id: int) -> AI:
        with self.__db_connection as database:
            try:
                ai_info = database.session.query(AI).get(ai_id)
                return ai_info
            except NoResultFound:
                return None
            
    def get_all_ais(self) -> list:
        with self.__db_connection as database:
            try:
                all_ais = database.session.query(AI).all()
                return all_ais
            except NoResultFound:
                return None

    def update_ai(
        self,
        ai_id: str,
        name: str,
        model: str,
    ) -> None:
        with self.__db_connection as database:
            try:
                ai_info = AI(
                    id=ai_id,
                    name=name,
                    model=model,
                    updated_at=datetime.now(),
                )
                database.session.add(ai_info)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def delete_ai(self, ai_id: int) -> None:
        with self.__db_connection as database:
            try:
                ai_info = AI(
                    id=ai_id,
                    deleted_by="admin", #TODO: Change this to the actual user
                    deleted_at=datetime.now(),
                )
                database.session.add(ai_info)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
            
    def force_delete_ai(self, ai_id: int) -> None:
        with self.__db_connection as database:
            try:
                ai_info = database.session.query(AI).get(ai_id)
                database.session.delete(ai_info)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception