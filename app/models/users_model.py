from sqlalchemy import Column, String, Integer, DateTime
from datetime import datatime

from app.db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String, unique=True, nullable=False, index=True)

    email = Column(String, unique=True, nullable=False, index=True)

    hashed_password = Column(String, nullable=False)

    created_at = Column(DateTime, default=datatime.utcnow)