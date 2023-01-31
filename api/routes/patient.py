from typing import Any, List, Optional

from fastapi import APIRouter, Depends

# Pydantic schemas
from schemas.user import Patient, PatientUpdate

# SQLAlchemy models
from db import models

# Service functions
from services import UserService, get_patient_service

router = APIRouter(
    prefix="/patient",
    tags=["patient"],
)

@router.get("/", response_model=List[Patient])
async def list(
    skip: int = 0,
    limit: int = 100,
    patient_service: UserService = Depends(get_patient_service),
) -> List[models.Patient]:
    return patient_service.list(skip=skip, limit=limit)