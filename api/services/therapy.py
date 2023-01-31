from sqlalchemy.orm import Session
from fastapi import HTTPException

# Pydantic schemas
from schemas.therapy import TherapyCreate, TherapyUpdate

# SQLAlchemy models
from db.models import Therapy, Patient, Therapist

from .base import BaseService

class TherapyService(BaseService[Therapy, TherapyCreate, TherapyUpdate]):
    def __init__(self, db_session: Session):
        super(TherapyService, self).__init__(Therapy, db_session)

    def create(self, obj: TherapyCreate, db_session: Session) -> Therapy:
        patient = db_session.query(Patient).get(obj.patient_id)
        therapist = self.db_session.query(Therapist).get(obj.therapist_id)

        if patient is None:
            raise HTTPException(
                status_code=400,
                detail=f"Patient with patientId = {obj.patient_id} not found.",
            )

        if therapist is None:
            raise HTTPException(
                status_code=400,
                detail=f"Therapist with therapistId = {obj.therapist_id} not found.",
            )

        return super(TherapyService, self).create(obj)