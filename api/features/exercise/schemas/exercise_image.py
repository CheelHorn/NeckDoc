from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

class ExerciseImageBase(BaseModel):
    position: Optional[int]
    image_url: Optional[str]

class ExerciseImageCreate(ExerciseImageBase):
    position: int
    exercise_id: UUID4

class ExerciseImageUpdate(ExerciseImageBase):
    
    class Config:
        orm_mode = True

class ExerciseImage(ExerciseImageBase):
    id: UUID4
    exercise_id: UUID4
    
    class Config:
        orm_mode = True
