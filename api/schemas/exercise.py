from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4, conint

class ExerciseBase(BaseModel):
    name: Optional[str]
    description: Optional[str]
    image_path: Optional[str]
    difficulty: Optional[conint(ge=0, le=5)]

class ExerciseCreate(ExerciseBase):
    name: str

class ExerciseUpdate(ExerciseBase):

    class Config:
        orm_mode = True

class Exercise(ExerciseBase):
    id: UUID4

    class Config:
        orm_mode = True