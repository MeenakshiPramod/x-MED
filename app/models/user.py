from pydantic import BaseModel
from typing import Optional  # Add this import

# For profile updates (all fields optional except email)
class UserUpdate(BaseModel):
    name: Optional[str] = None
    phone: Optional[str] = None
    place: Optional[str] = None
    profile_pic_url: Optional[str] = None

# Keep the original User model for responses
class User(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    place: str
    profile_pic_url: Optional[str] = None

class UserCreate(UserUpdate):
    pass

class User(UserUpdate):
    id: int
    
    class Config:
        orm_mode = True