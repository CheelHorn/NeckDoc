from sqlalchemy.orm import Session
from fastapi import Depends

# Pydantic schemas
from features.training_plan.schemas.exercise_interval import ExerciseIntervalCreate, ExerciseIntervalUpdate

# SQLAlchemy models
from db.models import ExerciseInterval
from db.session import get_db

from shared.base import BaseService

class ExerciseIntervalService(BaseService[ExerciseInterval, ExerciseIntervalCreate, ExerciseIntervalUpdate]):
    def __init__(self, db_session: Session):
        super(ExerciseIntervalService, self).__init__(ExerciseInterval, db_session)


def get_exercise_interval_service(db_session: Session = Depends(get_db)) -> ExerciseIntervalService:
    return ExerciseIntervalService(db_session)