import uuid
from sqlalchemy import Column, String, Boolean, DateTime
from flask_login import UserMixin
from src.configs.base import Base

class User(Base, UserMixin):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    given_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    family_name = Column(String, nullable=True)
    personal_id = Column(String, unique=True, nullable=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)
    first_login_date = Column(DateTime, nullable=True)
    last_login_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, nullable=False)
    updated_at = Column(DateTime, nullable=True)
    deleted_by = Column(String, nullable=True)
    deleted_at = Column(DateTime, nullable=True)
    # role_id = Column(BIGINT, ForeignKey("roles.id"))
    
    
    def __repr__(self):
        return (f"""User [
                id={self.id}, 
                given_name={self.given_name},
                middle_name={self.middle_name},
                family_name={self.family_name},
                username={self.username},
                email={self.email},
                is_admin={self.is_admin},
                first_login_date={self.first_login_date},
                last_login_date={self.last_login_date},
                created_at={self.created_at},
                updated_at={self.updated_at},
                deleted_by={self.deleted_by},
                deleted_at={self.deleted_at},
                ]""")
                # role_id={self.role_id}]
                
    def to_dict(self):
        return {
            "id": self.id,
            "given_name": self.given_name,
            "middle_name": self.middle_name,
            "family_name": self.family_name,
            "username": self.username,
            "email": self.email,
            "is_admin": self.is_admin,
            "first_login_date": self.first_login_date,
            "last_login_date": self.last_login_date,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "deleted_by": self.deleted_by,
            "deleted_at": self.deleted_at,
        }