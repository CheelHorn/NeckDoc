from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

# Pydantic schemas
from schemas.user import TherapistUpdate, UserCreate

# SQLAlchemy models
from db.models import Therapist
from db.session import get_db

from .base import BaseService
from services.auth import AuthService, get_auth_service

class TherapistService(BaseService[Therapist, TherapistUpdate, UserCreate]):
    def __init__(self, auth_service: AuthService, db_session: Session):
        super(TherapistService, self).__init__(Therapist, db_session)

        self.auth_service = auth_service


    def create(self, obj: UserCreate) -> Therapist:
        return self.auth_service.signup(obj, Therapist)

def get_therapist_service(auth_service: AuthService = Depends(get_auth_service), db_session: Session = Depends(get_db)) -> TherapistService:
    return TherapistService(auth_service, db_session)