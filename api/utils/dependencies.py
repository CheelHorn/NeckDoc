from typing import Optional

from fastapi import Depends

# SQLAlchemy Models
from db.models import User as UserModel

# CRUD functions for users
from crud import UsersService, get_users_service

from utils.auth import decode_token_data, credentials_exception

def get_current_user(user_service: UsersService = Depends(get_users_service), token_data: str = Depends(decode_token_data)) -> Optional[UserModel]:
    user: UserModel = user_service.get_by_email(token_data.username)
    if not user:
        raise credentials_exception
    return user