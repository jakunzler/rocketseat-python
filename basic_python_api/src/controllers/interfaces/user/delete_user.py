from typing import Dict
from abc import ABC, abstractmethod

class CreateUserInterface(ABC):

    @abstractmethod
    def delete_user(self, username: str, password: str) -> Dict: pass
