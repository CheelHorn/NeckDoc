from typing import Optional, List
from pydantic import BaseModel

from features.authentication.schemas.user import User, UserCreate,UserUpdate
from features.therapy.schemas.therapy import Therapy

class TherapistBase(BaseModel):
    clinic: Optional[str]

class TherapistCreate(TherapistBase, UserCreate):
    pass

class TherapistUpdate(TherapistBase, UserUpdate):
    pass

class Therapist(TherapistBase, User):
    therapies: List[Therapy]

    class Config:
        orm_mode = True