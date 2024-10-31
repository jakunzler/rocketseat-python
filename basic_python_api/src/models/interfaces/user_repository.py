from typing import Tuple
from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    @abstractmethod
    def authenticate_user(self, username: str, email: str, password: str) -> bool: pass
    
    @abstractmethod
    def set_first_login_date(self, user_id: int) -> None: pass

    @abstractmethod
    def create_user(self, username: str, email: str, password: str) -> None: pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> Tuple[str, str, str]: pass
    
    @abstractmethod
    def get_user_by_email(self, email: str) -> Tuple[str, str, str]: pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Tuple[str, str, str]: pass
    
    @abstractmethod
    def get_all_users(self) -> Tuple[Tuple[str, str, str]]: pass
    
    @abstractmethod
    def update_user(self, user_id: int, first_name: str, last_name: str, username: str, email: str, password: str, is_admin: bool) -> None: pass
    
    @abstractmethod
    def delete_user(self, user_id: int) -> None: pass