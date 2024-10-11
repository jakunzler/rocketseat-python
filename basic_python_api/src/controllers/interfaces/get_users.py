from typing import Dict
from abc import ABC, abstractmethod

class CreateUserInterface(ABC):

    @abstractmethod
    def get_users(self, username: str, password: str) -> Dict: pass
