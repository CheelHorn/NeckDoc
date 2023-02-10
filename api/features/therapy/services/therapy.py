from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

# Pydantic schemas
from features.therapy.schemas.therapy import TherapyCreate, TherapyUpdate
from pydantic.types import UUID4

# SQLAlchemy models
from db.models import Therapy, Patient, Therapist
from db.session import get_db

from shared.base import BaseService

class TherapyService(BaseService[Therapy, TherapyCreate, TherapyUpdate]):
    def __init__(self, db_session: Session):
        super(TherapyService, self).__init__(Therapy, db_session)

    def create(self, obj: TherapyCreate) -> Therapy:
        patient = self.db_session.query(Patient).get(obj.patient_id)
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
    

    def get_by_patient_id(self, patient_id: UUID4) -> Therapy:
        return self.db_session.query(Therapy).filter(Therapy.patient_id == patient_id).first()


def get_therapy_service(db_session: Session = Depends(get_db)) -> TherapyService:
    return TherapyService(db_session)