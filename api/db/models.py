from typing import Any
from sqlalchemy import Column, String, Integer, SmallInteger, Boolean, Date, JSON, DateTime
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base: Any = declarative_base()

class User(Base):
    __tablename__ = "user"
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
        "polymorphic_identity": "user",
        "polymorphic_on": "type",
    }

class Patient(User):
    __tablename__ = "patient"
    id = Column(ForeignKey("user.id"), primary_key=True)
    social_security_number = Column(String(256), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "patient",
    }

class Therapist(User):
    __tablename__ = "therapist"
    id = Column(ForeignKey("user.id"), primary_key=True)
    clinic = Column(String(256), nullable=True)

    __mapper_args__ = {
        "polymorphic_identity": "therapist",
    }

class Therapy(Base):
    __tablename__ = "therapy"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    patient_id = Column(ForeignKey("patient.id"))
    therapist_id = Column(ForeignKey("therapist.id"))
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)

    patient = relationship("Patient", backref="therapies")
    therapist = relationship("Therapist", backref="therapies")

class Exercise(Base):
    __tablename__ = "exercise"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String(256), nullable=False)
    description = Column(String, nullable=True)
    video_url = Column(String(256), nullable=True)

class ExerciseImage(Base):
    __tablename__ = "exercise_image"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    position = Column(SmallInteger, nullable=False)
    exercise_id = Column(ForeignKey("exercise.id"))
    image_url = Column(String(256), nullable=False)

    exercise = relationship("Exercise", backref="exercise_images")

class TrainingPlan(Base):
    __tablename__ = "training_plan"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    therapy_id = Column(ForeignKey("therapy.id"))
    title = Column(String(256), nullable=True)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)

    therapy = relationship("Therapy", backref="training_plans")

class ExerciseInterval(Base):
    __tablename__ = "exercise_interval"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String(256), nullable=True)
    time_in_days = Column(Integer, nullable=True)

class ExerciseDuration(Base):
    __tablename__ = "exercise_duration"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String(256), nullable=True)
    number_of_sets = Column(Integer, nullable=False, default=1)
    number_of_repetitions = Column(Integer, nullable=True)
    time_in_seconds = Column(Integer, nullable=True)
    type = Column(String(30))

class TrainingPlanExercise(Base):
    __tablename__ = "training_plan_exercise"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    training_plan_id = Column(ForeignKey("training_plan.id"))
    exercise_id = Column(ForeignKey("exercise.id"))
    exercise_interval_id = Column(ForeignKey("exercise_interval.id"))
    exercise_duration_id = Column(ForeignKey("exercise_duration.id"))

    training_plan = relationship("TrainingPlan", backref="training_plan_exercises")
    exercise = relationship("Exercise", backref="training_plan_exercises")
    exercise_interval = relationship("ExerciseInterval", backref="training_plan_exercises")
    exercise_duration = relationship("ExerciseDuration", backref="training_plan_exercises")

class ExerciseExecution(Base):
    __tablename__ = "exercise_execution"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    training_plan_exercise_id = Column(ForeignKey("training_plan_exercise.id"))
    start_timestamp = Column(DateTime, nullable=True)
    end_timestamp = Column(DateTime, nullable=True)
    video_url = Column(String(256), nullable=True)
    is_successful = Column(Boolean, nullable=True)

    training_plan_exercise = relationship("TrainingPlanExercise", backref="exercise_executions")
    exercise_execution_result = relationship("ExerciseExecutionResult", back_populates="exercise_execution", uselist=False)
    exercise_execution_feedback = relationship("ExerciseExecutionFeedback", back_populates="exercise_execution", uselist=False)

class ExerciseExecutionResult(Base):
    __tablename__ = "exercise_execution_result"
    exercise_execution_id = Column(ForeignKey("exercise_execution.id"), primary_key=True)
    result = Column(JSON, nullable=False)

    exercise_execution = relationship("ExerciseExecution", back_populates="exercise_execution_result", uselist=False)

class ExerciseExecutionFeedback(Base):
    __tablename__ = "exercise_execution_feedback"
    exercise_execution_id = Column(ForeignKey("exercise_execution.id"), primary_key=True)
    feedback = Column(JSON, nullable=False)

    exercise_execution = relationship("ExerciseExecution", back_populates="exercise_execution_feedback", uselist=False)