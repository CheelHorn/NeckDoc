from typing import Any
from sqlalchemy import Column, String, Integer, SmallInteger, Boolean, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base: Any = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    firstname = Column(String(256), nullable=True)
    lastname = Column(String(256), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(256), nullable=False)
    description = Column(String, nullable=True)
    image_path = Column(String(256), nullable=True)
    difficulty = Column(SmallInteger, nullable=True)