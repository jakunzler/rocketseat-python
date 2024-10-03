from pydantic import BaseModel
from datetime import datetime

class UserLogin(BaseModel):
    username: str
    password: str

class SessionResponse(BaseModel):
    id: int
    user_id: int
    latitude: float
    longitude: float
    created_at: datetime

    class Config:
        orm_mode = True