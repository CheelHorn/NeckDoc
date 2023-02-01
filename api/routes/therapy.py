from typing import Any, List, Optional

from fastapi import APIRouter, Depends
from pydantic.types import UUID4

# Pydantic schemas
from schemas.therapy import Therapy, TherapyCreate, TherapyUpdate

# SQLAlchemy models
from db import models

# Service functions
from services.therapy import TherapyService, get_therapy_service

router = APIRouter(
    prefix="/therapy",
    tags=["therapy"],
)

@router.get("/", response_model=List[Therapy])
async def list(
    skip: int = 0,
    limit: int = 100,
    therapy_service: TherapyService = Depends(get_therapy_service),
) -> List[models.Therapy]:
    return therapy_service.list(skip=skip, limit=limit)

@router.get("/{therapy_id}", response_model=Therapy)
async def get(
    therapy_id: UUID4,
    therapy_service: TherapyService = Depends(get_therapy_service),
) -> Optional[models.Therapy]:
    return therapy_service.get(therapy_id)

@router.post("/", response_model=Therapy)
async def create(
    therapy: TherapyCreate,
    therapy_service: TherapyService = Depends(get_therapy_service),
) -> Optional[models.Therapy]:
    return therapy_service.create(therapy)

@router.patch("/{therapy_id}", response_model=Therapy)
async def update(
    therapy_id: UUID4,
    therapy: TherapyUpdate,
    therapy_service: TherapyService = Depends(get_therapy_service),
) -> Optional[models.Therapy]:
    return therapy_service.update(therapy_id, therapy)

@router.delete("/{therapy_id}", response_model=Therapy)
async def delete(
    therapy_id: UUID4,
    therapy_service: TherapyService = Depends(get_therapy_service),
) -> Any:
    return therapy_service.delete(therapy_id)