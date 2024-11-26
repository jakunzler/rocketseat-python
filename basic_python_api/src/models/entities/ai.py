import uuid
from sqlalchemy import Column, String, DateTime
from src.configs.base import Base

class AI(Base):
    __tablename__ = "ai"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    model = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    
    def __repr__(self):
        return (f"""AI [
                id={self.id}, 
                name={self.name},
                model={self.model},
                created_at={self.created_at},
                updated_at={self.updated_at},
                deleted_by={self.deleted_by},
                deleted_at={self.deleted_at},
                ]""")
        
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "model": self.model,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_by": self.deleted_by,
            "deleted_at": self.deleted_at,
        }