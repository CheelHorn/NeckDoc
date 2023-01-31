from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from utils.auth import create_access_token
from utils.dependencies import get_current_user

# SQLAlchemy Models
from db import models

# Pydantic schema
from schemas.user import User, UserCreate, UserUpdate

# Service functions for users
from services import UsersService, get_users_service

router = APIRouter(
    prefix="/auth",
    tags=["authentification"],
)


@router.post('/signup', response_model=User, status_code=201)
async def create_user(
    new_user: UserCreate,
    user_service: UsersService = Depends(get_users_service),
) -> Optional[models.User]:
    return user_service.create(new_user)


# Change to login, only for swagger demonstration
@router.post("/login", responses={400: {"description": "Incorrect username or password"}},)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UsersService = Depends(get_users_service),
) -> Any:
    user: models.User = user_service.authenticate_user(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400)
    return {
        "access_token": create_access_token(sub=user.email),
        "token_type": "bearer",
    }


@router.get("/me", response_model=User)
async def get_me(
    current_user: models.User = Depends(get_current_user),
) -> Optional[models.User]:
    return current_user