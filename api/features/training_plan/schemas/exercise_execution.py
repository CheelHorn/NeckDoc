from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

from datetime import datetime

from features.training_plan.schemas.training_plan_exercise import TrainingPlanExercise

class ExerciseExecutionBase(BaseModel):
    start_timestamp: Optional[datetime]
    end_timestamp: Optional[datetime]
    video_url: Optional[str]
    is_successful: Optional[bool]

class ExerciseExecutionCreate(ExerciseExecutionBase):
    training_plan_exercise_id: UUID4

class ExerciseExecutionUpdate(ExerciseExecutionBase):
    pass

    class Config:
        orm_mode = True

class ExerciseExecution(ExerciseExecutionBase):
    id: UUID4
    training_plan_exercise_id: UUID4

    class Config:
        orm_mode = True