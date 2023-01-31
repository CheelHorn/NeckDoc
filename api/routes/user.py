from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic.types import UUID4

from utils.dependencies import get_current_user

# Pydantic schemas
from schemas.user import User, UserCreate, UserUpdate

# SQLAlchemy models
from db import models

# service functions
from services import UserService, get_user_service

router = APIRouter(
    prefix="/user",
    tags=["user"],
)


@router.get("/", response_model=List[User])
async def list(
    skip: int = 0,
    limit: int = 100,
    user_service: UserService = Depends(get_user_service),
) -> List[models.User]:
    return user_service.list(skip=skip, limit=limit)


@router.get("/{user_id}", response_model=User)
async def get(
    user_id: UUID4,
    user_service: UserService = Depends(get_user_service),
) -> Optional[models.User]:
    return user_service.get(user_id)


@router.patch("/{user_id}", response_model=User)
async def update(
    user_id: UUID4,
    user: UserUpdate,
    user_service: UserService = Depends(get_user_service),
) -> Optional[models.User]:
    return user_service.update(user_id, user)
