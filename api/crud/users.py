from typing import Any, Optional

import sqlalchemy
from sqlalchemy.orm import Session
from fastapi import HTTPException

from db.models import User
from schemas.users import UserCreate, UserUpdate

from .base import BaseService

from utils.auth import get_password_hash, verify_password


class UsersService(BaseService[User, UserCreate, UserUpdate]):
    def __init__(self, db_session: Session):
        super(UsersService, self).__init__(User, db_session)

    def create(self, obj: UserCreate) -> User:
        db_obj: User = self.model(email=obj.email, hashed_password=get_password_hash(obj.password))
        self.db_session.add(db_obj)
        try:
            self.db_session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            self.db_session.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Conflict Error")
            else:
                raise e
        return db_obj


    def get_by_email(self, email: Any) -> Optional[User]:
        obj: Optional[User] = self.db_session.query(User).filter(User.email == email).first()
        if obj is None:
            raise HTTPException(status_code=404, detail="Not Found")
        return obj


    def authenticate_user(self, email: str, password: str) -> Optional[User]:
        db_obj: User = self.get_by_email(email)
        if not db_obj:
            return None
        if not verify_password(password, db_obj.hashed_password):
            return None
        return db_obj