from typing import Any, List, Optional

from fastapi import APIRouter, Depends, Response
from pydantic.types import UUID4

# Pydantic schemas
from features.exercise.schemas.exercise import Exercise, ExerciseCreate, ExerciseUpdate
from pydantic.types import UUID4

# SQLAlchemy models
from db import models

# Service functions
from features.exercise.services.exercise import ExcerciseService, get_exercise_service

router = APIRouter(
    prefix="/exercise",
    tags=["exercise"],
)


@router.get("/", response_model=List[Exercise])
def list(
    skip: int = 0,
    limit: int = 100,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> List[models.Exercise]:
    return exercise_service.list(skip=skip, limit=limit)


@router.get("/{exercise_id}", response_model=Exercise)
def get(
    exercise_id: UUID4,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> Optional[models.Exercise]:
    return exercise_service.get(exercise_id)


@router.post("/", response_model=Exercise, status_code=201)
def create(
    exercise: ExerciseCreate,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> models.Exercise:
    return exercise_service.create(exercise)


@router.patch("/{exercise_id}", response_model=Exercise)
def update(
    exercise_id: UUID4,
    exercise: ExerciseUpdate,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> Optional[models.Exercise]:
    return exercise_service.update(exercise_id, exercise)


@router.delete("/{exercise_id}", status_code=204)
def delete(
    exercise_id: UUID4,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> None:
    exercise_service.delete(exercise_id)
    return Response(status_code=204)