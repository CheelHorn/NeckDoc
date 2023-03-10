from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from pydantic.types import UUID4

# Pydantic schemas
from features.training_plan.schemas.training_plan_exercise import TrainingPlanExercise, TrainingPlanExerciseCreate, TrainingPlanExerciseUpdate

# SQLAlchemy models
from db import models

# Service functions
from features.training_plan.services.training_plan_exercise import get_training_plan_exercise_service, TrainingPlanExerciseService

router = APIRouter(
    prefix="/training_plan_exercise",
    tags=["training_plan_exercise"],
)


@router.get("/", response_model=List[TrainingPlanExercise])
def list(
    skip: int = 0,
    limit: int = 100,
    training_plan_exercise_service: TrainingPlanExerciseService = Depends(get_training_plan_exercise_service),
) -> List[models.TrainingPlanExercise]:
    return training_plan_exercise_service.list(skip=skip, limit=limit)


@router.get("/{training_plan_exercise_id}", response_model=TrainingPlanExercise)
def get(
    training_plan_exercise_id: UUID4,
    training_plan_exercise_service: TrainingPlanExerciseService = Depends(get_training_plan_exercise_service),
) -> Optional[models.TrainingPlanExercise]:
    return training_plan_exercise_service.get(training_plan_exercise_id)


@router.get("/patient/{patient_id}", response_model=List[TrainingPlanExercise])
def get_by_patient_id(
    patient_id: UUID4,
    training_plan_exercise_service: TrainingPlanExerciseService = Depends(get_training_plan_exercise_service),
) -> List[models.TrainingPlan]:
    return training_plan_exercise_service.get_by_patient_id(patient_id)


@router.post("/", response_model=TrainingPlanExercise)
def create(
    training_plan_exercise: TrainingPlanExerciseCreate,
    training_plan_exercise_service: TrainingPlanExerciseService = Depends(get_training_plan_exercise_service),
) -> Optional[models.TrainingPlanExercise]:
    return training_plan_exercise_service.create(training_plan_exercise)


@router.patch("/{training_plan_exercise_id}", response_model=TrainingPlanExercise)
def update(
    training_plan_exercise_id: UUID4,
    training_plan_exercise: TrainingPlanExerciseUpdate,
    training_plan_exercise_service: TrainingPlanExerciseService = Depends(get_training_plan_exercise_service),
) -> Optional[models.TrainingPlanExercise]:
    return training_plan_exercise_service.update(training_plan_exercise_id, training_plan_exercise)


@router.delete("/{training_plan_exercise_id}", status_code=204)
def delete(
    training_plan_exercise_id: UUID4,
    training_plan_exercise_service: TrainingPlanExerciseService = Depends(get_training_plan_exercise_service),
) -> None:
    training_plan_exercise_service.delete(training_plan_exercise_id)

    