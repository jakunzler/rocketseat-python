from typing import Dict
from abc import ABC, abstractmethod

class CreateUserInterface(ABC):

    @abstractmethod
    def create(self, username: str, password: str) -> Dict: pass