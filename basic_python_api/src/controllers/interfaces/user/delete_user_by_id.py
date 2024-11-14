from typing import Dict
from abc import ABC, abstractmethod

class DeleteUserByIdInterface(ABC):

    @abstractmethod
    def delete_user_by_id(self, user_id: str) -> Dict: pass
