from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4, date

from datetime import date

class TherapyBase(BaseModel):
    start_date: Optional[date]
    end_date: Optional[date]
    is_active: Optional[bool]

class TherapyCreate(TherapyBase):
    patient_id: UUID4
    therapist_id: UUID4

class TherapyUpdate(TherapyBase):
    pass

class Therapy(TherapyBase):
    id: UUID4
    patient_id: UUID4
    therapist_id: UUID4

    class Config:
        orm_mode = True
