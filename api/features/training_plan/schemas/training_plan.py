from typing import Optional, List

from pydantic import BaseModel
from pydantic.types import UUID4

from datetime import date

from features.therapy.schemas.therapy import Therapy
from features.training_plan.schemas.training_plan_exercise import TrainingPlanExercise

class TrainingPlanBase(BaseModel):
    title: Optional[str]
    start_date: Optional[date]
    end_date: Optional[date]

class TrainingPlanCreate(TrainingPlanBase):
    therapy_id: UUID4

class TrainingPlanUpdate(TrainingPlanBase):
    pass

class TrainingPlan(TrainingPlanBase):
    id: UUID4
    therapy: Therapy
    training_plan_exercises: List[TrainingPlanExercise]

    class Config:
        orm_mode = True
