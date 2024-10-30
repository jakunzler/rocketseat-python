import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from src.configs.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    # role_id = Column(BIGINT, ForeignKey("roles.id"))
    
    def __repr__(self):
        return (f"""User [
                id={self.id}, 
                first_name={self.first_name},
                last_name={self.last_name},
                username={self.username},
                email={self.email},
                is_admin={self.is_admin},
                created_at={self.created_at},
                updated_at={self.updated_at},
                deleted_by={self.deleted_by},
                deleted_at={self.deleted_at},
                ]""")
                # role_id={self.role_id}]