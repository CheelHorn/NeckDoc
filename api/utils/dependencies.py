from typing import Optional
from fastapi import Depends

# SqlAlchemy models
from db.models import User

from utils.auth import decode_token_data, credentials_exception

# Service functions
from services.auth import AuthService, get_auth_service

def get_current_user(auth_service: AuthService = Depends(get_auth_service), token_data: str = Depends(decode_token_data)) -> Optional[User]:
    user: User = auth_service.get_user_by_email(token_data.username)
    if not user:
        raise credentials_exception
    return user
