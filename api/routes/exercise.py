from typing import Any, List, Optional

from fastapi import APIRouter, Depends, Response, File, UploadFile, HTTPException
from fastapi.responses import FileResponse
from pydantic.types import UUID4

# Pydantic schemas
from schemas.exercise import Exercise, ExerciseCreate, ExerciseUpdate

# SQLAlchemy models
from db import models

# Service functions
from services.exercise import ExcerciseService, get_exercise_service

from utils.file_handling import image_whitelist

router = APIRouter(
    prefix="/exercise",
    tags=["exercise"],
)


@router.get("/", response_model=List[Exercise])
async def list(
    skip: int = 0,
    limit: int = 100,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> List[models.Exercise]:
    return exercise_service.list(skip=skip, limit=limit)


@router.get("/{exercise_id}", response_model=Exercise)
async def get(
    exercise_id: UUID4,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> Optional[models.Exercise]:
    return exercise_service.get(exercise_id)


@router.post("/", response_model=Exercise, status_code=201)
async def create(
    exercise: ExerciseCreate,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> models.Exercise:
    return exercise_service.create(exercise)


@router.patch("/{exercise_id}", response_model=Exercise)
async def update(
    exercise_id: UUID4,
    exercise: ExerciseUpdate,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> Optional[models.Exercise]:
    return exercise_service.update(exercise_id, exercise)

@router.delete("/{exercise_id}", status_code=204)
async def delete(
    exercise_id: UUID4,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> Any:
    exercise_service.delete(exercise_id)
    return Response(status_code=204)

@router.get("/{exercise_id}/image", response_class=FileResponse)
async def get_image(
    exercise_id: UUID4,
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> Optional[FileResponse]:
    image_path: Exercise = exercise_service.get_image_path(exercise_id)
    return image_path


@router.post("/{exercise_id}/image", response_model=Exercise, responses={400: {"description": "Invalid document type"}})
async def upload_image(
    exercise_id: UUID4,
    image_file: UploadFile = File(...),
    exercise_service: ExcerciseService = Depends(get_exercise_service),
) -> Optional[models.Exercise]:
    if image_file.content_type not in image_whitelist:
        raise HTTPException(400)
    return exercise_service.update_image(exercise_id, image_file)


