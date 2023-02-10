from typing import Any, Optional

from sqlalchemy.orm import Session
from fastapi import Depends

# Pydantic schemas
from features.exercise.schemas.exercise import ExerciseCreate, ExerciseUpdate

# SqlAlchemy models
from db.models import Exercise
from db.session import get_db

from shared.base import BaseService

class ExcerciseService(BaseService[Exercise, ExerciseCreate, ExerciseUpdate]):
    def __init__(self, db_session: Session):
        super(ExcerciseService, self).__init__(Exercise, db_session)

def get_exercise_service(db_session: Session = Depends(get_db)) -> ExcerciseService:
    return ExcerciseService(db_session)
