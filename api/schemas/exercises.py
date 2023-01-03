from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

from datetime import date

class ExerciseBase(BaseModel):
    name: str

class ExerciseCreate(ExerciseBase):
    pass

class ExerciseUpdate(ExerciseBase):
    pass

class Exercise(ExerciseBase):
    id: UUID4

    class Config:
        orm_mode = True