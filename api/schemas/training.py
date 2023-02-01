from typing import Any, Optional

from pydantic import BaseModel, Json
from pydantic.types import UUID4

from .exercise import Exercise

class TrainingBase(BaseModel):
    video_path: Optional[str]
    results: Optional[Json[Any]]
    is_successful: Optional[bool]


class TrainingCreate(TrainingBase):
    patient_id: UUID4
    exercise_id: UUID4


class TrainingUpdate(TrainingBase):
    class Config:
        orm_mode = True

        
class Training(TrainingBase):
    id: UUID4
    patient_id: UUID4
    exercise: Exercise

    class Config:
        orm_mode = True