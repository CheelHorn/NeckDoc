from typing import List

from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from utils.dependencies import get_db, get_current_user

# Pydantic schema
from schemas import users as user_schema

# CRUD functions for users
from crud import users as user_crud


router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/", response_model=List[user_schema.User])
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = user_crud.get_users(db, skip=skip, limit=limit)
    return users


@router.get("/{user_id}", response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/{user_id}", response_model=user_schema.User)
def update_user(user_id: int, user: user_schema.UserUpdate, current_user: user_schema.User = Depends(get_current_user), db: Session = Depends(get_db)):
    if user_id != current_user.id:
        raise HTTPException(status_code=401, detail="No permission")
    db_user = user_crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user = user_crud.update_user(db, user_id, user)
    return db_user
