import os

from fastapi import Depends, HTTPException, status

from sqlalchemy.orm import Session

from jose import JWTError, jwt


from db.session import SessionLocal

from utils.auth import oauth2_scheme

from schemas import token as token_schema

from crud import users as user_crud

from utils.config import JWT_SECRET, ALGORITHM

# DB Session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Get currently logged in User
def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")
        token_data = token_schema.TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = user_crud.get_user_by_email(db, token_data.username)

    if user is None:
        raise credentials_exception
    return user