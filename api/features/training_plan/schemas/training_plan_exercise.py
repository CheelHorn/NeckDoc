from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

from features.exercise.schemas.exercise import Exercise
from features.training_plan.schemas.exercise_duration import ExerciseDuration
from features.training_plan.schemas.exercise_interval import ExerciseInterval

class TrainingPlanExerciseBase(BaseModel):
    pass

class TrainingPlanExerciseCreate(TrainingPlanExerciseBase):
    exercise_id: UUID4
    training_plan_id: UUID4
    exercise_duration_id: UUID4
    exercise_interval_id: UUID4

class TrainingPlanExerciseUpdate(TrainingPlanExerciseBase):
    exercise_duration_id: Optional[UUID4]
    exercise_interval_id: Optional[UUID4]

class TrainingPlanExercise(TrainingPlanExerciseBase):
    id: UUID4
    exercise: Exercise
    training_plan_id: UUID4
    exercise_duration: Optional[ExerciseDuration]
    exercise_interval: Optional[ExerciseInterval]

    class Config:
        orm_mode = True
