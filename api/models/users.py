from sqlalchemy import Column, Integer, String, Boolean, Date

from db.session import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    firstname = Column(String(256), nullable=True)
    surname = Column(String(256), nullable=True)
    date_of_birth = Column(Date, nullable=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
