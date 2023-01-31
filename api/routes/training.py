from typing import Any, List, Optional

from fastapi import APIRouter, Depends
from pydantic.types import UUID4

# Pydantic schemas
from schemas.training import Training, TrainingCreate, TrainingUpdate

# SQLAlchemy models
from db import models

# Service functions
from services import TrainingService, get_training_service

router = APIRouter(
    prefix="/training",
    tags=["training"],
)

@router.get("/", response_model=List[Training])
async def list(
    skip: int = 0,
    limit: int = 100,
    training_service: TrainingService = Depends(get_training_service),
) -> List[models.Training]:
    return training_service.list(skip=skip, limit=limit)

@router.get("/{training_id}", response_model=Training)
async def get(
    training_id: UUID4,
    training_service: TrainingService = Depends(get_training_service),
) -> Optional[models.Training]:
    return training_service.get(training_id)

@router.post("/", response_model=Training)
async def create(
    training: TrainingCreate,
    training_service: TrainingService = Depends(get_training_service),
) -> Optional[models.Training]:
    return training_service.create(training)

@router.patch("/{training_id}", response_model=Training)
async def update(    
    training_id: UUID4,
    training: TrainingUpdate,
    training_service: TrainingService = Depends(get_training_service),
) -> Optional[models.Training]:
    return training_service.update(training_id, training)

@router.delete("/{training_id}", response_model=Training)
async def delete(
    training_id: UUID4,
    training_service: TrainingService = Depends(get_training_service),
) -> Any:
    return training_service.delete(training_id)