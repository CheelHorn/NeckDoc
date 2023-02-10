from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

class ExerciseDurationBase(BaseModel):
    title: Optional[str]
    number_of_sets: Optional[int]
    number_of_repetitions: Optional[int]
    time_in_seconds: Optional[int]
    type: str

class ExerciseDurationCreate(ExerciseDurationBase):
    title: str

class ExerciseDurationUpdate(ExerciseDurationBase):
    pass

class ExerciseDuration(ExerciseDurationBase):
    id: UUID4

    class Config:
        orm_mode = True