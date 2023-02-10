from typing import Any, List, Optional

from fastapi import APIRouter, Depends, Response
from pydantic.types import UUID4

# Pydantic schemas
from features.training_plan.schemas.exercise_interval import ExerciseInterval, ExerciseIntervalCreate, ExerciseIntervalUpdate

# SQLAlchemy models
from db import models

# Service functions
from features.training_plan.services.exercise_interval import ExerciseIntervalService, get_exercise_interval_service

router = APIRouter(
    prefix="/exercise_interval",
    tags=["exercise_interval"],
)


@router.get("/", response_model=List[ExerciseInterval])
def list(
    skip: int = 0,
    limit: int = 100,
    exercise_interval_service: ExerciseIntervalService = Depends(get_exercise_interval_service),
) -> List[models.ExerciseInterval]:
    return exercise_interval_service.list(skip=skip, limit=limit)


@router.get("/{exercise_interval_id}", response_model=ExerciseInterval)
def get(
    exercise_interval_id: UUID4,
    exercise_interval_service: ExerciseIntervalService = Depends(get_exercise_interval_service),
) -> Optional[models.ExerciseInterval]:
    return exercise_interval_service.get(exercise_interval_id)


@router.post("/", response_model=ExerciseInterval)
def create(
    exercise_interval: ExerciseIntervalCreate,
    exercise_interval_service: ExerciseIntervalService = Depends(get_exercise_interval_service),
) -> Optional[models.ExerciseInterval]:
    return exercise_interval_service.create(exercise_interval)


@router.patch("/{exercise_interval_id}", response_model=ExerciseInterval)
def update(
    exercise_interval_id: UUID4,
    exercise_interval: ExerciseIntervalUpdate,
    exercise_interval_service: ExerciseIntervalService = Depends(get_exercise_interval_service),
) -> Optional[models.ExerciseInterval]:
    return exercise_interval_service.update(exercise_interval_id, exercise_interval)


@router.delete("/{exercise_interval_id}", status_code=204)
def delete(
    exercise_interval_id: UUID4,
    exercise_interval_service: ExerciseIntervalService = Depends(get_exercise_interval_service),
) -> None:
    exercise_interval_service.delete(exercise_interval_id)
    return Response(status_code=204)