from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import get_db

from .users import UsersService

def get_users_service(db_session: Session = Depends(get_db)) -> UsersService:
    return UsersService(db_session)