from typing import Any, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from utils.auth import create_access_token
from utils.dependencies import get_current_user

# SQLAlchemy Models
from db.models import User as UserModel

# Pydantic schema
from schemas.users import User, UserCreate, UserUpdate

# CRUD functions for users
from crud import UsersService, get_users_service

router = APIRouter(
    prefix="/auth",
    tags=["authentification"],
)


@router.post('/signup', response_model=User, status_code=201, responses={409: {"description": "Conflict Error"}},)
async def create_user(
    new_user: UserCreate,
    user_service: UsersService = Depends(get_users_service),
) -> Optional[UserModel]:
    return user_service.create(new_user)


# Change to login, only for swagger demonstration
@router.post("/login", responses={400: {"description": "Incorrect username or password"}},)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UsersService = Depends(get_users_service),
) -> Any:
    user: UserModel = user_service.authenticate_user(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400)
    return {
        "access_token": create_access_token(sub=user.email),
        "token_type": "bearer",
    }


@router.get("/me", response_model=User)
async def get_me(
    current_user: UserModel = Depends(get_current_user),
) -> Optional[UserModel]:
    return current_user