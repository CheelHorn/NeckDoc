from typing import Any, Optional, List, Type, TypeVar

import sqlalchemy
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

# Pydantic schemas
from schemas.user import UserCreate, UserUpdate

# SQLAlchemy models
from db.models import User
from db.session import get_db

from utils.auth import get_password_hash, verify_password, decode_token_data

UserModelType = TypeVar("UserModelType", bound=User)

class AuthService():
    def __init__(self, db_session: Session):
        self.db_session = db_session


    def get_user_by_id(self, id: Any) -> Optional[User]:
        obj: Optional[User] = self.db_session.query(User).get(id)
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj


    def get_user_by_email(self, email: Any) -> Optional[User]:
        obj: Optional[User] = self.db_session.query(User).filter(User.email == email).first()
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj


    def list_all_users(self, skip: int = 0, limit: int = 100) -> List[User]:
        objs: List[User] = self.db_session.query(User).offset(skip).limit(limit).all()
        return objs


    def signup(self, obj: UserCreate, model: Type[UserModelType]) -> User:
        user = model(email=obj.email, hashed_password=get_password_hash(obj.password))
        self.db_session.add(user)
        try:
            self.db_session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self.db_session.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Conflict Error")
            else:
                raise e
        return user


    def authenticate(self, email: Any, password: str) -> Optional[User]:
        user: Optional[User] = self.get_user_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="Not Found")
        if not verify_password(password, user.hashed_password):
            return None
        return user

    
    def get_current_user(self, token_data: str) -> Optional[User]:
        user: User = self.get_user_by_email(token_data.username)
        if not user:
            raise HTTPException(status_code=404, detail="Not Found")
        return user


def get_auth_service(db_session: Session = Depends(get_db)) -> AuthService:
    return AuthService(db_session)