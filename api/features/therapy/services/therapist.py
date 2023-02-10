from sqlalchemy.orm import Session
from fastapi import Depends

# Pydantic schemas
from features.therapy.schemas.therapist import TherapistUpdate, TherapistCreate

# SQLAlchemy models
from db.models import Therapist
from db.session import get_db

from shared.base import BaseService
from features.authentication.services.auth import AuthService, get_auth_service

class TherapistService(BaseService[Therapist, TherapistUpdate, TherapistCreate]):
    def __init__(self, auth_service: AuthService, db_session: Session):
        super(TherapistService, self).__init__(Therapist, db_session)

        self.auth_service = auth_service

    def create(self, obj: TherapistCreate) -> Therapist:
        return self.auth_service.signup(obj, Therapist)

def get_therapist_service(auth_service: AuthService = Depends(get_auth_service), db_session: Session = Depends(get_db)) -> TherapistService:
    return TherapistService(auth_service, db_session)