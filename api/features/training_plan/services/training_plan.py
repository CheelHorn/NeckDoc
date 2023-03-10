from typing import List

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

# Pydantic schemas
from features.training_plan.schemas.training_plan import TrainingPlanCreate, TrainingPlanUpdate
from pydantic.types import UUID4

# SQLAlchemy models
from db.models import TrainingPlan, Therapy
from db.session import get_db

from shared.base import BaseService

class TrainingPlanService(BaseService[TrainingPlan, TrainingPlanCreate, TrainingPlanUpdate]):
    def __init__(self, db_session: Session):
        super(TrainingPlanService, self).__init__(TrainingPlan, db_session)

    def create(self, obj: TrainingPlanCreate) -> TrainingPlan:
        therapy = self.db_session.query(Therapy).get(obj.therapy_id)

        if therapy is None:
            raise HTTPException(
                status_code=400,
                detail=f"Therapy with therapyId = {obj.therapy_id} not found.",
            )

        return super(TrainingPlanService, self).create(obj)
    

    def get_by_patient_id(self, patient_id: UUID4) -> List[TrainingPlan]:
        return self.db_session.query(TrainingPlan).join(Therapy).filter(Therapy.patient_id == patient_id).all()
    

def get_training_plan_service(db_session: Session = Depends(get_db)) -> TrainingPlanService:
    return TrainingPlanService(db_session)