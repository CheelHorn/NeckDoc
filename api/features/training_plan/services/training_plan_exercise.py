from typing import Any, Optional

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, UploadFile

# Pydantic schemas
from features.training_plan.schemas.training_plan_exercise import TrainingPlanExerciseCreate, TrainingPlanExerciseUpdate

# SQLAlchemy models
from db.models import TrainingPlanExercise, TrainingPlan, Exercise, ExerciseDuration, ExerciseInterval
from db.session import get_db

from shared.base import BaseService

class TrainingPlanExerciseService(BaseService[TrainingPlanExercise, TrainingPlanExerciseCreate, TrainingPlanExerciseUpdate]):
    def __init__(self, db_session: Session):
        super(TrainingPlanExerciseService, self).__init__(TrainingPlanExercise, db_session)

    def create(self, obj: TrainingPlanExerciseCreate) -> TrainingPlanExercise:
        training_plan = self.db_session.query(TrainingPlan).get(obj.training_plan_id)
        exercise = self.db_session.query(Exercise).get(obj.exercise_id)
        exercise_duration = self.db_session.query(ExerciseDuration).get(obj.exercise_duration_id)
        exercise_interval = self.db_session.query(ExerciseInterval).get(obj.exercise_interval_id)

        if training_plan is None:
            raise HTTPException(
                status_code=400,
                detail=f"TrainingPlan with trainingPlanId = {obj.training_plan_id} not found.",
            )
        
        if exercise is None:
            raise HTTPException(
                status_code=400,
                detail=f"Exercise with exerciseId = {obj.exercise_id} not found.",
            )

        if exercise_duration is None:
            raise HTTPException(
                status_code=400,
                detail=f"ExerciseDuration with exerciseDurationId = {obj.exercise_duration_id} not found.",
            )
        
        if exercise_interval is None:
            raise HTTPException(
                status_code=400,
                detail=f"ExerciseInterval with exerciseIntervalId = {obj.exercise_interval_id} not found.",
            )

        return super(TrainingPlanExerciseService, self).create(obj)
    
    
def get_training_plan_exercise_service(db_session: Session = Depends(get_db)) -> TrainingPlanExerciseService:
    return TrainingPlanExerciseService(db_session)