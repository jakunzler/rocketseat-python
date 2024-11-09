from src.models.entities.user import User
from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def authenticate_user(self, username: str, email: str, password: str) -> bool: pass
    
    @abstractmethod
    def set_first_login_date(self, user_id: int) -> None: pass

    @abstractmethod
    def create_user(self, username: str, email: str, password: str) -> User: pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User: pass
    
    @abstractmethod
    def get_user_by_email(self, email: str) -> User: pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> User: pass
    
    @abstractmethod
    def get_all_users(self) -> list[User]: pass
    
    @abstractmethod
    def update_user(self, partial_user: User) -> User: pass
    
    @abstractmethod
    def delete_user(self, user_id: int) -> bool: pass