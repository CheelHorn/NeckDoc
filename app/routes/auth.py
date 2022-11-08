from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from utils import auth
from utils.dependencies import get_db, get_current_user

# Pydantic schema
from schemas import users as user_schema

# CRUD functions for users
from crud import users as user_crud

router = APIRouter(
    prefix="/auth",
    tags=["authentification"],
)


@router.post('/signup', response_model=user_schema.User, status_code=201)
def create_user(new_user: user_schema.UserCreate, db: Session = Depends(get_db)):
    user = user_crud.get_user_by_email(db, new_user.email)
    if user:
        raise HTTPException(
            status_code=400,
            detail="The user with this email already exists in the system",
        )
    user = user_crud.create_user(db, new_user)
    return user


# Change to login, only for swagger demonstration
@router.post("/login")
def login_user(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(email=form_data.username, password=form_data.password, db=db)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    return {
        "access_token": auth.create_access_token(sub=user.email),
        "token_type": "bearer",
    }


@router.get("/me", response_model=user_schema.User)
def get_current_user(current_user: user_schema.User = Depends(get_current_user)):
    user = current_user
    return user