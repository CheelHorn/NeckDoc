from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

# Pydantic schemas
from features.training_plan.schemas.exercise_duration import ExerciseDurationCreate, ExerciseDurationUpdate

# SQLAlchemy models
from db.models import ExerciseDuration
from db.session import get_db

from shared.base import BaseService

class ExerciseDurationService(BaseService[ExerciseDuration, ExerciseDurationCreate, ExerciseDurationUpdate]):
    def __init__(self, db_session: Session):
        super(ExerciseDurationService, self).__init__(ExerciseDuration, db_session)

def get_exercise_duration_service(db_session: Session = Depends(get_db)) -> ExerciseDurationService:
    return ExerciseDurationService(db_session)