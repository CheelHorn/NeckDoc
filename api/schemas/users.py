from typing import Optional

from pydantic import BaseModel

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

    class Config:
        orm_mode = True

class User(UserBase):
    id: int
    firstname: Optional[str] = None
    surname: Optional[str] = None
    date_of_birth: Optional[date] = None
    is_active: bool

    class Config:
        orm_mode = True