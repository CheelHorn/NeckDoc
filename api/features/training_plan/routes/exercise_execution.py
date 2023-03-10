from typing import List, Optional, Any

from fastapi import APIRouter, Depends, Response, File, UploadFile, WebSocket
from pydantic.types import UUID4

# Pydantic schemas
from features.training_plan.schemas.exercise_execution import ExerciseExecution, ExerciseExecutionCreate, ExerciseExecutionUpdate

# SQLAlchemy models
from db import models

# Service functions
from features.training_plan.services.exercise_execution import ExerciseExecutionService, get_exercise_execution_service

import requests

router = APIRouter(
    prefix="/exercise_execution",
    tags=["exercise_execution"],
)


@router.get("/", response_model=List[ExerciseExecution])
def list(
    skip: int = 0,
    limit: int = 100,
    exercise_execution_service: ExerciseExecutionService = Depends(get_exercise_execution_service),
) -> List[models.ExerciseExecution]:
    return exercise_execution_service.list(skip=skip, limit=limit)


@router.get("/{exercise_execution_id}", response_model=ExerciseExecution)
def get(
    exercise_execution_id: UUID4,
    exercise_execution_service: ExerciseExecutionService = Depends(get_exercise_execution_service),
) -> Optional[models.ExerciseExecution]:
    return exercise_execution_service.get(exercise_execution_id)


@router.post("/", response_model=ExerciseExecution)
def create(
    exercise_execution: ExerciseExecutionCreate,
    exercise_execution_service: ExerciseExecutionService = Depends(get_exercise_execution_service),
) -> Optional[models.ExerciseExecution]:
    return exercise_execution_service.create(exercise_execution)


@router.patch("/{exercise_execution_id}", response_model=ExerciseExecution)
def update(
    exercise_execution_id: UUID4,
    exercise_execution: ExerciseExecutionUpdate,
    exercise_execution_service: ExerciseExecutionService = Depends(get_exercise_execution_service),
) -> Optional[models.ExerciseExecution]:
    return exercise_execution_service.update(exercise_execution_id, exercise_execution)


@router.post("/{exercise_execution_id}/video")
def upload_video(
    exercise_execution_id: UUID4,
    video_file: UploadFile = File(...),
    exercise_execution_service: ExerciseExecutionService = Depends(get_exercise_execution_service),
) -> Any:
    return exercise_execution_service.upload_video(exercise_execution_id, video_file)


@router.get("/{exercise_execution_id}/video")
def get_video(
    exercise_execution_id: UUID4,
    exercise_execution_service: ExerciseExecutionService = Depends(get_exercise_execution_service),
) -> Any:
    exercise_execution: ExerciseExecution = exercise_execution_service.get(exercise_execution_id)

    data = {"video_url": "http://192.168.0.181:8081/assets/videos/exercise_execution/70002d4c-38c3-43fc-aebc-e9e260ffa265.mp4"}

    response = requests.post("http://192.168.0.161:8000/video_processing_sidehop", params=data)

    print(response.text)

    return response.text


@router.delete("/{exercise_execution_id}", status_code=204)
def delete(
    exercise_execution_id: UUID4,
    exercise_execution_service: ExerciseExecutionService = Depends(get_exercise_execution_service),
) -> None:
    exercise_execution_service.delete(exercise_execution_id)
    return Response(status_code=204)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")