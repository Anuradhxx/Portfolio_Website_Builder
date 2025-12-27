# app/models/profile.py

from sqlalchemy import Column, String, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Profile(Base):
    __tablename__= 'profiles'

    
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey('users.id',ondelete='CASCADE'), unique=True, nullable=False)

    full_name = Column(String(100), nullable=False)
    bio = Column(Text, nullable=True)
    email = Column(String(255), nullable=True)

    phone = Column(String(20))
    location = Column(String(100), nullable=True)

    linkedin = Column(String(255), nullable= True)
    github = Column(String(255),nullable=True)

    profile_photo= Column(String(255))
    resume_pdf= Column(String(255), nullable=True)


    is_published = Column(Boolean, default=False)  


    user = relationship("User", back_populates="profile")
