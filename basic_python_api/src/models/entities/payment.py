import uuid
from sqlalchemy import Column, String, Float, Boolean, DateTime
from src.configs.base import Base

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    value = Column(Float, nullable=False)
    paid = Column(Boolean, default=False)
    bank_payment_id = Column(String(255), nullable=True)
    qr_code = Column(String(255), nullable=False)
    expiration_date = Column(DateTime)
    
    def __repr__(self):
        return f'<Payment {self.payment_id}>'
      
    def to_dict(self):
        return {
            'id': self.id,
            'value': self.value,
            'paid': self.paid,
            'bank_payment_id': self.bank_payment_id,
            'qr_code': self.qr_code,
            'expiration_date': self.expiration_date
        }