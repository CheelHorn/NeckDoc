from typing import Optional, List

from pydantic import BaseModel, EmailStr
from pydantic.types import UUID4

from datetime import date

from features.therapy.schemas.therapy import Therapy

# User
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
    is_admin: bool
    type: str
    
    class Config:
        orm_mode = True

# Patient
class PatientBase(BaseModel):
    social_security_number: Optional[str]

class PatientUpdate(PatientBase, UserUpdate):
    pass

class Patient(PatientBase, User):
    class Config:
        orm_mode = True

class PatientDetail(Patient):
    therapies: List[Therapy]

    class Config:
        orm_mode = True

# Therapist
class TherapistBase(BaseModel):
    clinic: Optional[str]

class TherapistUpdate(TherapistBase, UserUpdate):
    pass

class Therapist(TherapistBase, User):    
    class Config:
        orm_mode = True
