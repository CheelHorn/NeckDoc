from typing import Optional, List

from pydantic import BaseModel
from pydantic.types import UUID4

from features.exercise.schemas.exercise_image import ExerciseImage

class ExerciseBase(BaseModel):
    title: Optional[str]
    description: Optional[str]
    video_url: Optional[str]

class ExerciseCreate(ExerciseBase):
    title: str

class ExerciseUpdate(ExerciseBase):

    class Config:
        orm_mode = True

class Exercise(ExerciseBase):
    id: UUID4
    exercise_images: List[ExerciseImage]

    class Config:
        orm_mode = True