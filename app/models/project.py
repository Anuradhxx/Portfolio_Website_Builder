# app/models/project.py
from sqlalchemy import Column, String, Integer, Text, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class Project(Base):
    __tablename__= 'projects'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete='CASCADE'), nullable=False)

    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=True)
    tech_stack = Column(String(255), nullable=True)

    github_link = Column(String(255), nullable=True)
    demo_link = Column(String(255), nullable=True)

    image = Column(String(255), nullable=True)     
    is_featured = Column(Boolean, default=False)   
    order = Column(Integer, default=0)


    is_published = Column(Boolean, default=True)  


    user = relationship("User", back_populates="projects")

