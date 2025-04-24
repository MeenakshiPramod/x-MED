from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str
    phone: str
    place: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True