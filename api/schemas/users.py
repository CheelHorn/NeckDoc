from typing import Optional

from pydantic import BaseModel, EmailStr
from pydantic.types import UUID4

from datetime import date

class UserBase(BaseModel):
    email: Optional[EmailStr]
    firstname: Optional[str]
    lastname: Optional[str]
    date_of_birth: Optional[date]
    is_active: Optional[bool]

class UserCreate(UserBase):
    password: str

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: UUID4
    
    class Config:
        orm_mode = True