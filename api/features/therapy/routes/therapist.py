from typing import Any, List, Optional

from fastapi import APIRouter, Depends, Response
from pydantic.types import UUID4

# Pydantic schemas
from features.therapy.schemas.therapist import Therapist, TherapistUpdate

# SQLAlchemy models
from db import models

# Service functions
from features.therapy.services.therapist import TherapistService, get_therapist_service


router = APIRouter(
    prefix="/therapist",
    tags=["therapist"],
)

@router.get("/", response_model=List[Therapist])
def get(
    therapist_service: TherapistService = Depends(get_therapist_service),
) -> Optional[list[models.Therapist]]:
    return therapist_service.list()


@router.get("/{therapist_id}", response_model=Therapist)
def get(
    therapist_id: UUID4,
    therapist_service: TherapistService = Depends(get_therapist_service),
) -> Optional[models.Therapist]:
    return therapist_service.get(therapist_id)


@router.patch("/{therapist_id}", response_model=Therapist)
def update(
    therapist_id: UUID4,
    therapist: TherapistUpdate,
    therapist_service: TherapistService = Depends(get_therapist_service),
) -> Optional[models.Therapist]:
    return therapist_service.update(therapist_id, therapist)


@router.delete("/{therapist_id}", status_code=204)
def delete(
    therapist_id: UUID4,
    therapist_service: TherapistService = Depends(get_therapist_service),
) -> None:
    therapist_service.delete(therapist_id)
    return Response(status_code=204)