from fastapi import Depends

from sqlalchemy.orm import Session

from .user import UserService
from .exercise import ExcerciseService
from .training import TrainingService
from .therapy import TherapyService
from .patient import PatientService

from db.session import get_db
from db import models

def get_user_service(db_session: Session = Depends(get_db)) -> UserService:
    return UserService(models.User, db_session)

def get_patient_service(db_session: Session = Depends(get_db)) -> PatientService:
    return PatientService(db_session)

def get_therapist_service(db_session: Session = Depends(get_db)) -> UserService:
    return UserService(models.Therapist, db_session)

def get_exercise_service(db_session: Session = Depends(get_db)) -> ExcerciseService:
    return ExcerciseService(db_session)

def get_training_service(db_session: Session = Depends(get_db)) -> TrainingService:
    return TrainingService(db_session)

def get_therapy_service(db_session: Session = Depends(get_db)) -> TherapyService:
    return TherapyService(db_session)

