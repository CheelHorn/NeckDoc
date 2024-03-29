from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from utils import create_access_token

# Pydantic schemas
from schemas.user import User, UserCreate, UserUpdate, Patient, Therapist

# SQLAlchemy models
from db import models

# Service functions for users
from authentication.services.auth import AuthService, get_auth_service
from therapy.services.patient import PatientService, get_patient_service
from therapy.services.therapist import TherapistService, get_therapist_service

from utils import decode_token_data

router = APIRouter(
    prefix="",
    tags=["authentification"],
)


@router.post('/signup/patient', response_model=Patient, status_code=201)
async def signup_patient(
    new_patient: UserCreate,
    patient_service: PatientService = Depends(get_patient_service),
) -> Optional[models.Patient]:
    return patient_service.create(new_patient)


@router.post('/signup/therapist', response_model=Therapist, status_code=201)
async def signup_therapist(
    new_therapist: UserCreate,
    therapist_service: TherapistService = Depends(get_therapist_service),
) -> Optional[models.Therapist]:
    return therapist_service.create(new_therapist)


@router.post("/login", responses={400: {"description": "Incorrect username or password"}},)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service),
) -> Any:
    user: models.User = auth_service.authenticate(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400)
    return {
        "access_token": create_access_token(sub=user.email),
        "token_type": "bearer",
    }


@router.get("/users", response_model=list[User])
async def get_users(
    user_service: AuthService = Depends(get_auth_service),
) -> Optional[list[models.User]]:
    return user_service.list_all_users()


@router.get("/me", response_model=User)
async def me(
    token_data: str = Depends(decode_token_data),
    auth_service: AuthService = Depends(get_auth_service),
) -> Optional[models.User]:
    return auth_service.get_current_user(token_data)