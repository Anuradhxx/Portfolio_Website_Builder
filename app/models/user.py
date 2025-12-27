# app/models/user.py

from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from app.database import Base

from app.models.theme import Theme

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(150), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    

    profile = relationship(
        "Profile",
        back_populates="user",
        uselist=False,
        cascade="all, delete-orphan"
    )

    skills = relationship(
        "Skill",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    projects = relationship(
        "Project",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    themes = relationship(
        "Theme",
        back_populates="user",
        cascade="all, delete-orphan"
    )

