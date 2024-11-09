from typing import Dict
from abc import ABC, abstractmethod

class GetUsersInterface(ABC):

    @abstractmethod
    def get_users(self) -> Dict: pass
