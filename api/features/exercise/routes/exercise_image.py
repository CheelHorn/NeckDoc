from typing import Any, List, Optional

from fastapi import APIRouter, Depends, Response, File, UploadFile
from pydantic.types import UUID4

# Pydantic schemas
from features.exercise.schemas.exercise_image import ExerciseImage, ExerciseImageCreate, ExerciseImageUpdate
from pydantic.types import UUID4

# SQLAlchemy models
from db import models

# Service functions
from features.exercise.services.exercise_image import ExerciseImageService, get_exercise_image_service


router = APIRouter(
    prefix="/exercise_image",
    tags=["exercise_image"],
)


@router.get("/", response_model=List[ExerciseImage])
def list(
    skip: int = 0,
    limit: int = 100,
    exercise_image_service: ExerciseImageService = Depends(get_exercise_image_service),
) -> List[models.ExerciseImage]:
    return exercise_image_service.list(skip=skip, limit=limit)


@router.get("/{exercise_image_id}", response_model=ExerciseImage)
def get(
    exercise_image_id: UUID4,
    exercise_image_service: ExerciseImageService = Depends(get_exercise_image_service),
) -> Optional[models.ExerciseImage]:
    return exercise_image_service.get(exercise_image_id)


@router.post("/", response_model=ExerciseImage)
def create(
    exercise_image: ExerciseImageCreate,
    exercise_image_service: ExerciseImageService = Depends(get_exercise_image_service),
) -> Optional[models.ExerciseImage]:
    return exercise_image_service.create(exercise_image)


@router.patch("/{exercise_image_id}", response_model=ExerciseImage)
def update(
    exercise_image_id: UUID4,
    exercise_image: ExerciseImageUpdate,
    exercise_image_service: ExerciseImageService = Depends(get_exercise_image_service),
) -> Optional[models.ExerciseImage]:
    return exercise_image_service.update(exercise_image_id, exercise_image)


@router.delete("/{exercise_image_id}")
def delete(
    exercise_image_id: UUID4,
    exercise_image_service: ExerciseImageService = Depends(get_exercise_image_service),
) -> None:
    return exercise_image_service.delete(exercise_image_id)


@router.post("/{exercise_image_id}/image", response_model=ExerciseImage)
def upload_image(
    exercise_image_id: UUID4,
    image_file: UploadFile = File(...),
    exercise_image_service: ExerciseImageService = Depends(get_exercise_image_service),
) -> Optional[models.ExerciseImage]:
    return exercise_image_service.upload_image(exercise_image_id, image_file)