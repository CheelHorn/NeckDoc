from typing import Any, List, Optional

from fastapi import APIRouter, Depends, Response
from pydantic.types import UUID4

# Pydantic schemas
from schemas.user import Patient, PatientUpdate

# SQLAlchemy models
from db import models

# Service functions
from services.patient import PatientService, get_patient_service

router = APIRouter(
    prefix="/patient",
    tags=["patient"],
)

@router.get("/", response_model=List[Patient])
async def get(
    patient_service: PatientService = Depends(get_patient_service),
) -> Optional[list[models.Patient]]:
    return patient_service.list()


@router.get("/{patient_id}", response_model=Patient)
async def get(
    patient_id: UUID4,
    patient_service: PatientService = Depends(get_patient_service),
) -> Optional[models.Patient]:
    return patient_service.get(patient_id)


@router.patch("/{patient_id}", response_model=Patient)
async def update(
    patient_id: UUID4,
    patient: PatientUpdate,
    patient_service: PatientService = Depends(get_patient_service),
) -> Optional[models.Patient]:
    return patient_service.update(patient_id, patient)


@router.delete("/{patient_id}", status_code=204)
async def delete(
    patient_id: UUID4,
    patient_service: PatientService = Depends(get_patient_service),
) -> None:
    patient_service.delete(patient_id)
    return Response(status_code=204)