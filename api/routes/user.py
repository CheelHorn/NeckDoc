from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic.types import UUID4

from utils.dependencies import get_current_user

# SQLAlchemy Models
from db import models

# Pydantic schema
from schemas.user import User, UserCreate, UserUpdate

# service functions for users
from services import UsersService, get_users_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/", response_model=List[User])
async def list(
    skip: int = 0,
    limit: int = 100,
    user_service: UsersService = Depends(get_users_service),
) -> List[models.User]:
    return user_service.list(skip=skip, limit=limit)


@router.get("/{user_id}", response_model=User)
async def get(
    user_id: UUID4,
    user_service: UsersService = Depends(get_users_service),
) -> Optional[models.User]:
    return user_service.get(user_id)


@router.patch("/{user_id}", response_model=User)
async def update(
    user_id: UUID4,
    user: UserUpdate,
    current_user: User = Depends(get_current_user),
    user_service: UsersService = Depends(get_users_service),
) -> Optional[models.User]:
    if user_id != current_user.id:
        raise HTTPException(status_code=401)
    return user_service.update(user_id, user)
