from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from pydantic.types import UUID4

# Pydantic schemas
from features.training_plan.schemas.training_plan import TrainingPlan, TrainingPlanCreate, TrainingPlanUpdate

# SQLAlchemy models
from db import models

# Service functions
from features.training_plan.services.training_plan import TrainingPlanService, get_training_plan_service

router = APIRouter(
    prefix="/training_plan",
    tags=["training_plan"],
)


@router.get("/", response_model=List[TrainingPlan])
def list(
    skip: int = 0,
    limit: int = 100,
    training_plan_service: TrainingPlanService = Depends(get_training_plan_service),
) -> List[models.TrainingPlan]:
    return training_plan_service.list(skip=skip, limit=limit)


@router.get("/{training_plan_id}", response_model=TrainingPlan)
def get(
    training_plan_id: UUID4,
    training_plan_service: TrainingPlanService = Depends(get_training_plan_service),
) -> Optional[models.TrainingPlan]:
    return training_plan_service.get(training_plan_id)


@router.get("/patient/{patient_id}", response_model=List[TrainingPlan])
def get_by_patient_id(
    patient_id: UUID4,
    training_plan_service: TrainingPlanService = Depends(get_training_plan_service),
) -> List[models.TrainingPlan]:
    return training_plan_service.get_by_patient_id(patient_id)


@router.post("/", response_model=TrainingPlan)
def create(
    training_plan: TrainingPlanCreate,
    training_plan_service: TrainingPlanService = Depends(get_training_plan_service),
) -> Optional[models.TrainingPlan]:
    return training_plan_service.create(training_plan)


@router.patch("/{training_plan_id}", response_model=TrainingPlan)
def update(
    training_plan_id: UUID4,
    training_plan: TrainingPlanUpdate,
    training_plan_service: TrainingPlanService = Depends(get_training_plan_service),
) -> Optional[models.TrainingPlan]:
    return training_plan_service.update(training_plan_id, training_plan)


@router.delete("/{training_plan_id}", status_code=204)
def delete(
    training_plan_id: UUID4,
    training_plan_service: TrainingPlanService = Depends(get_training_plan_service),
) -> None:
    training_plan_service.delete(training_plan_id)
    return Response(status_code=204)