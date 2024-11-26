from src.models.entities.payment import Payment
from abc import ABC, abstractmethod

class PaymentRepositoryInterface(ABC):
  
    @abstractmethod
    def create_payment(self, value: float) -> Payment: pass
    
    @abstractmethod
    def get_payment_by_id(self, payment_id: int) -> Payment: pass
    
    @abstractmethod
    def get_payment_by_bank_payment_id(self, bank_payment_id: str) -> Payment: pass
    
    @abstractmethod
    def get_all_payments(self, page: int, page_length: int) -> list[Payment]: pass
    
    @abstractmethod
    def update_payment(self, partial_payment: Payment) -> Payment: pass
    
    @abstractmethod
    def delete_payment(self, payment_id: int) -> bool: pass