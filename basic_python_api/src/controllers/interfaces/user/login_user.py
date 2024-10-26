from typing import Dict
from abc import ABC, abstractmethod

class LoginUserInterface(ABC):

    @abstractmethod
    def login_user(self, username: str, password: str) -> Dict: pass
