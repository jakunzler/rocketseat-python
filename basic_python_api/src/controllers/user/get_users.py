from typing import Dict
from src.models.interfaces.user_repository import UserRepositoryInterface
from ..interfaces.user.get_users import GetUsersInterface

class GetUsers(GetUsersInterface):
    def __init__(self, user_repository: UserRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def get_users(self) -> Dict:
        users = self.__get_all_users()

        return self.__format_response(users)
    
    def __get_all_users(self) -> Dict:
        users = self.__user_repository.get_all_users()

        return users
    
    def __format_response(self, users: Dict) -> Dict:
        return {
            "type": "Users",
            "count": len(users),
            "users": users,
        }