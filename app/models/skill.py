# app/models/skill.py

from sqlalchemy import Column, String, Integer, Text, ForeignKey,Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Skill(Base):
    __tablename__= 'skills'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id',ondelete='CASCADE'), nullable=True)

    name = Column(String(50), nullable=False)
    proficiency_level = Column(Integer, nullable=False)  # 1-10
    icon = Column(String(255), nullable=True) 


    is_published = Column(Boolean, default=True)


    user = relationship("User", back_populates= "skills")

    