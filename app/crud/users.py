from sqlalchemy.orm import Session

# SQlAlchemy model
from models import users as user_model

# Pydantic schema
from schemas import users as user_schema

from utils import auth

def get_user(db: Session, user_id: int):
    return db.query(user_model.User).filter(user_model.User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(user_model.User).filter(user_model.User.email == email).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: user_schema.UserCreate):
    hashed_password = auth.get_password_hash(user.password)
    db_user = user_model.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user: user_schema.UserUpdate):
    db_user = get_user(db, user_id=user_id)
    for var, value in vars(user).items():
        setattr(db_user, var, value) if value else None
    #db_user.modified = datetime.utcnow()
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user