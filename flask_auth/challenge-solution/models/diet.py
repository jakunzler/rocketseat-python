from database import db
from datetime import datetime, timezone

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_name = db.Column(db.String(80), unique=True, nullable=False)
    dish_description = db.Column(db.String(220), unique=False, nullable=False)
    datetime = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Campo de data e hora
    is_allowed = db.Column(db.Boolean, default=False)
    
    def to_dict(self):
        return {
            'id': self.id,
            'dish_name': self.dish_name,
            'dish_description': self.dish_description,
            'datetime': self.datetime,
            'is_allowed': self.is_allowed
        }