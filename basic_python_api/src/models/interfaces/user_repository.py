from src.models.entities.user import User
from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):

    @abstractmethod
    def authenticate_user(self, username: str, email: str, password: str) -> User: pass

    @abstractmethod
    def create_user(self, username: str, email: str, password: str) -> User: pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User: pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User: pass

    @abstractmethod
    def get_user_by_id(self, user_id: str) -> User: pass

    @abstractmethod
    def get_all_users(self, page: int, page_length: int) -> list[User]: pass

    @abstractmethod
    def update_user(self, partial_user: User) -> User: pass

    @abstractmethod
    def delete_user(self, current_user_id: str, user_id: str) -> bool: pass
