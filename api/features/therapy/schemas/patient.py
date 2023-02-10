from typing import Optional, List
from pydantic import BaseModel

from features.authentication.schemas.user import User, UserCreate, UserUpdate
from features.therapy.schemas.therapy import Therapy

class PatientBase(BaseModel):
    social_security_number: Optional[str]

class PatientCreate(PatientBase, UserCreate):
    pass

class PatientUpdate(PatientBase, UserUpdate):
    pass

class Patient(PatientBase, User):
    therapies: List[Therapy]

    class Config:
        orm_mode = True
