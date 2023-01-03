from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

from datetime import date

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[str] = None
    firstname: Optional[str] = None
    surname: Optional[str] = None
    date_of_birth: Optional[date] = None

class User(UserBase):
    id: UUID4
    firstname: Optional[str] = None
    surname: Optional[str] = None
    date_of_birth: Optional[date] = None
    is_active: bool

    class Config:
        orm_mode = True