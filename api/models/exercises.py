from sqlalchemy import Column, Integer, String, Boolean, Date
from sqlalchemy.dialects.postgresql import UUID
import uuid

from db.session import Base

class Exercise(Base):
    __tablename__ = "exercises"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(256), nullable=True)