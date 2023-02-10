from typing import List, Optional

from fastapi import APIRouter, Depends, Response
from pydantic.types import UUID4

# Pydantic schemas
from features.training_plan.schemas.exercise_duration import ExerciseDuration, ExerciseDurationCreate, ExerciseDurationUpdate

# SQLAlchemy models
from db import models

# Service functions
from features.training_plan.services.exercise_duration import ExerciseDurationService, get_exercise_duration_service

router = APIRouter(
    prefix="/exercise_duration",
    tags=["exercise_duration"],
)


@router.get("/", response_model=List[ExerciseDuration])
def list(
    skip: int = 0,
    limit: int = 100,
    exercise_duration_service: ExerciseDurationService = Depends(get_exercise_duration_service),
) -> List[models.ExerciseDuration]:
    return exercise_duration_service.list(skip=skip, limit=limit)


@router.get("/{exercise_duration_id}", response_model=ExerciseDuration)
def get(
    exercise_duration_id: UUID4,
    exercise_duration_service: ExerciseDurationService = Depends(get_exercise_duration_service),
) -> Optional[models.ExerciseDuration]:
    return exercise_duration_service.get(exercise_duration_id)


@router.post("/", response_model=ExerciseDuration)
def create(
    exercise_duration: ExerciseDurationCreate,
    exercise_duration_service: ExerciseDurationService = Depends(get_exercise_duration_service),
) -> Optional[models.ExerciseDuration]:
    return exercise_duration_service.create(exercise_duration)


@router.patch("/{exercise_duration_id}", response_model=ExerciseDuration)
def update(
    exercise_duration_id: UUID4,
    exercise_duration: ExerciseDurationUpdate,
    exercise_duration_service: ExerciseDurationService = Depends(get_exercise_duration_service),
) -> Optional[models.ExerciseDuration]:
    return exercise_duration_service.update(exercise_duration_id, exercise_duration)


@router.delete("/{exercise_duration_id}", status_code=204)
def delete(
    exercise_duration_id: UUID4,
    exercise_duration_service: ExerciseDurationService = Depends(get_exercise_duration_service),
) -> None:
    exercise_duration_service.delete(exercise_duration_id)
    return Response(status_code=204)