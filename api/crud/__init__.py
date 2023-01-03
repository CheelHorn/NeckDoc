from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_db

from .users import UsersService
from .exercises import ExcerciseService

def get_users_service(db_session: Session = Depends(get_db)) -> UsersService:
    return UsersService(db_session)

def get_exercise_service(db_session: Session = Depends(get_db)) -> ExcerciseService:
    return ExcerciseService(db_session)