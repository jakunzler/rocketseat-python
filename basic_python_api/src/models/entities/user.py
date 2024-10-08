import uuid
from sqlalchemy import Column, String, Boolean
from src.configs.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    # role_id = Column(BIGINT, ForeignKey("roles.id"))
    
    def __repr__(self):
        return (f"""User [
                id={self.id}, 
                first_name={self.first_name},
                last_name={self.last_name},
                username={self.username},
                email={self.email},
                is_admin={self.is_admin},
                ]""")
                # role_id={self.role_id}]