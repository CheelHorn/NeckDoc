from typing import Any

from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware

# SQLAlchemy Models
from db.models import User as UserModel

# Service functions for users
from services import UsersService, get_users_service

from routes import auth, user, exercise, training

from routes.training import TrainingRouter


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(exercise.router)
app.include_router(training.router)


# Change to login, only for swagger demonstration
@app.post("/token", responses={400: {"description": "Incorrect username or password"}},)
async def login_user(
    form_data: OAuth2PasswordRequestForm = Depends(),
    user_service: UsersService = Depends(get_users_service),
) -> Any:
    user: UserModel = user_service.authenticate_user(email=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(status_code=400)
    return {
        "access_token": auth.create_access_token(sub=user.email),
        "token_type": "bearer",
    }