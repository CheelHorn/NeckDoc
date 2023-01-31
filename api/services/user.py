from typing import Any, Optional

import sqlalchemy
from sqlalchemy.orm import Session
from fastapi import HTTPException

from db.models import User
from schemas.user import UserCreate, UserUpdate

from .base import BaseService

from utils.auth import get_password_hash, verify_password


class UserService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self, db_session: Session):
        super(UserService, self).__init__(User, db_session)

    def create(self, obj: UserCreate) -> User:
        user: User = self.model(email=obj.email, hashed_password=get_password_hash(obj.password))
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


    def get_by_email(self, email: Any) -> Optional[User]:
        user: Optional[User] = self.db_session.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(status_code=404, detail="Not Found")
        return user


    def authenticate_user(self, email: Any, password: str) -> Optional[User]:
        user: Optional[User] = self.get_by_email(email)
        if not user:
            raise HTTPException(status_code=404, detail="Not Found")
        if not verify_password(password, user.hashed_password):
            return None
        return user