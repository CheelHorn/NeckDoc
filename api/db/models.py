from typing import Any
from sqlalchemy import Column, String, Integer, SmallInteger, Boolean, Date, JSON
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
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
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    type = Column(String(20))

    __mapper_args__ = {
        "polymorphic_identity": "users",
        "polymorphic_on": "type",
    }

class Patient(User):
    __tablename__ = "patients"
    id = Column(ForeignKey("users.id"), primary_key=True)
    social_security_number = Column(String(256), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "patients",
    }


class Therapist(User):
    __tablename__ = "therapists"
    id = Column(ForeignKey("users.id"), primary_key=True)
    clinic = Column(String(256), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "therapists",
    }

class Therapy(Base):
    __tablename__ = "therapies"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    patient_id = Column(ForeignKey("patients.id"))
    patient = relationship("Patient", backref="therapies")
    therapist_id = Column(ForeignKey("therapists.id"))
    therapist = relationship("Therapist", backref="therapies")
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)

class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(256), nullable=False)
    description = Column(String, nullable=True)
    image_path = Column(String(256), nullable=True)
    difficulty = Column(SmallInteger, nullable=True)

class Training(Base):
    __tablename__ = "trainings"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    patient_id = Column(ForeignKey("patients.id"))
    patient = relationship("Patient", backref="trainings")
    exercise_id = Column(ForeignKey("exercises.id"))
    exercise = relationship("Exercise", backref="trainings")
    video_path = Column(String(256), nullable=True)
    results = Column(JSON, nullable=True)
    is_successful = Column(Boolean)