from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from utils.auth import create_access_token
from utils.dependencies import get_current_user

# Pydantic schemas
from schemas.user import User, UserCreate, UserUpdate, Patient, Therapist

# SQLAlchemy models
from db import models

# Service functions for users
from services import UserService, get_user_service, get_patient_service, get_therapist_service

router = APIRouter(
    prefix="/auth",
    tags=["authentification"],
)


@router.post('/signup/patient', response_model=Patient, status_code=201)
async def signup_patient(
    new_patient: UserCreate,
    patient_service: UserService = Depends(get_patient_service),
) -> Optional[models.Patient]:
    return patient_service.create(new_patient)

@router.post('/signup/therapist', response_model=Therapist, status_code=201)
async def signup_therapist(
    new_therapist: UserCreate,
    therapist_service: UserService = Depends(get_therapist_service),
) -> Optional[models.Therapist]:
    return therapist_service.create(new_therapist)

@router.post("/login", responses={400: {"description": "Incorrect username or password"}},)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UserService = Depends(get_user_service),
) -> Any:
    user: models.User = user_service.authenticate_user(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400)
    return {
        "access_token": create_access_token(sub=user.email),
        "token_type": "bearer",
    }


@router.get("/me", response_model=User)
async def me(
    current_user: models.User = Depends(get_current_user),
) -> Optional[models.User]:
    return current_user