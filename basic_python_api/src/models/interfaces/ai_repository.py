from typing import Tuple
from abc import ABC, abstractmethod

class AIRepositoryInterface(ABC):
    
    @abstractmethod
    def create_ai(self, name: str, model: str) -> None: pass

    @abstractmethod
    def get_ai_by_id(self, ai_id: int) -> Tuple[int, str, str]: pass
    
    @abstractmethod
    def get_all_ais(self) -> Tuple[Tuple[int, str, str]]: pass
    
    @abstractmethod
    def update_ai(self, ai_id: int, name: str, model: str) -> None: pass
    
    @abstractmethod
    def delete_ai(self, ai_id: int) -> None: pass
