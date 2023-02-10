from typing import Optional

from datetime import datetime, timedelta

from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext
from jose import jwt, JWTError

from features.authentication.schemas.token import TokenData

from shared.config import JWT_SECRET, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


credentials_exception = HTTPException(
    status_code=401,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def create_access_token(sub: str):
    payload = {}
    
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    payload['type'] = 'access_token'
    payload['exp'] = expire
    payload['iat'] = datetime.utcnow()
    payload['sub'] = str(sub)
    
    encoded_jwt = jwt.encode(payload, JWT_SECRET, algorithm=ALGORITHM)
    
    return encoded_jwt


def decode_token_data(token: str = Depends(oauth2_scheme)) -> Optional[str]:
    try:
        payload = jwt.decode(
            token,
            JWT_SECRET,
            algorithms=[ALGORITHM],
            options={"verify_aud": False},
        )
        username: str = payload.get("sub")
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception

    return token_data