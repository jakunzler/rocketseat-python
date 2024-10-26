from typing import Dict
from abc import ABC, abstractmethod

class CreateUserInterface(ABC):

    @abstractmethod
    def update_user(self, username: str, password: str) -> Dict: pass
