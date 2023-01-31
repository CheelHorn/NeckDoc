from fastapi import Depends

from sqlalchemy.orm import Session

from .user import UserService
from .exercise import ExcerciseService
from .training import TrainingService

from db.session import get_db

def get_user_service(db_session: Session = Depends(get_db)) -> UserService:
    return UserService(db_session)

def get_exercise_service(db_session: Session = Depends(get_db)) -> ExcerciseService:
    return ExcerciseService(db_session)

def get_training_service(db_session: Session = Depends(get_db)) -> TrainingService:
    return TrainingService(db_session)