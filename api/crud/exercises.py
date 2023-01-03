from sqlalchemy.orm import Session

from db.models import Exercise
from schemas.exercises import ExerciseCreate, ExerciseUpdate

from .base import BaseService


class ExcerciseService(BaseService[Exercise, ExerciseCreate, ExerciseUpdate]):
    def __init__(self, db_session: Session):
        super(ExcerciseService, self).__init__(Exercise, db_session)