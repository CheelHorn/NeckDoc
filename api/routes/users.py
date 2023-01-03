from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from pydantic.types import UUID4

from utils.dependencies import get_current_user

# SQLAlchemy Models
from db.models import User as UserModel

# Pydantic schema
from schemas.users import User, UserCreate, UserUpdate

# CRUD functions for users
from crud import UsersService, get_users_service

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/", response_model=List[User])
async def get_users(
    skip: int = 0,
    limit: int = 100,
    user_service: UsersService = Depends(get_users_service),
) -> List[UserModel]:
    return user_service.list(skip=skip, limit=limit)


@router.get("/{user_id}", response_model=User, responses={404: {"description": "User not found"}})
async def get_user(
    user_id: UUID4,
    user_service: UsersService = Depends(get_users_service),
) -> Optional[UserModel]:
    return user_service.get(user_id)


@router.patch("/{user_id}", response_model=User, responses={401: {"description": "No permission"}, 404: {"description": "User not found"}})
async def update_user(
    user_id: UUID4,
    user: UserUpdate,
    current_user: User = Depends(get_current_user),
    user_service: UsersService = Depends(get_users_service),
) -> Optional[UserModel]:
    if user_id != current_user.id:
        raise HTTPException(status_code=401)
    return user_service.update(user_id, user)
