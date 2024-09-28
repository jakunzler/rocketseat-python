from repository.database import db

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id = db.Column(db.String(255), nullable=False)
    value = db.Column(db.Float, nullable=False)
    paid = db.Column(db.Boolean, default=False)
    bank_payment_id = db.Column(db.String(255), nullable=True)
    qr_code = db.Column(db.String(255), nullable=False)
    expiration_date = db.Column(db.DateTime)
    
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