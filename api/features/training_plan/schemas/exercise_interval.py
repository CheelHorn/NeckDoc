from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

class ExerciseIntervalBase(BaseModel):
    title: Optional[str]
    time_in_days: Optional[int]

class ExerciseIntervalCreate(ExerciseIntervalBase):
    title: str

class ExerciseIntervalUpdate(ExerciseIntervalBase):
    pass

class ExerciseInterval(ExerciseIntervalBase):
    id: UUID4

    class Config:
        orm_mode = True