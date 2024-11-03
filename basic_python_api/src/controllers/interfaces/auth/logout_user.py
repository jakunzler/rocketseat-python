from typing import Dict
from abc import ABC, abstractmethod

class LogoutUserInterface(ABC):

    @abstractmethod
    def logout_user(self) -> Dict: pass
