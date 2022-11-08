import os
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer

from sqlalchemy.orm import Session
from passlib.context import CryptContext
from jose import jwt

from crud import users as user_crud

from utils.config import JWT_SECRET, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def authenticate_user(email: str, password: str, db: Session):
    user = user_crud.get_user_by_email(db, email)

    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None

    return user

def create_access_token(sub: str):
    payload = {}
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    payload['type'] = 'access_token'
    payload['exp'] = expire
    payload['iat'] = datetime.utcnow()
    payload['sub'] = str(sub)
    
    encoded_jwt = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    
    return encoded_jwt