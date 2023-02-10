from sqlalchemy.orm import Session
from fastapi import Depends

# Pydantic schemas
from features.therapy.schemas.patient import PatientUpdate, UserCreate

# SQLAlchemy models
from db.models import Patient
from db.session import get_db

from shared.base import BaseService
from features.authentication.services.auth import AuthService, get_auth_service

class PatientService(BaseService[Patient, PatientUpdate, UserCreate]):
    def __init__(self, auth_service: AuthService, db_session: Session):
        super(PatientService, self).__init__(Patient, db_session)

        self.auth_service = auth_service

    def create(self, obj: UserCreate) -> Patient:
        return self.auth_service.signup(obj, Patient)

def get_patient_service(auth_service: AuthService = Depends(get_auth_service), db_session: Session = Depends(get_db)) -> PatientService:
    return PatientService(auth_service, db_session)