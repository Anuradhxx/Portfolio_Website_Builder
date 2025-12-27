# app/models/theme.py
from sqlalchemy import Column, String, Integer, Text, ForeignKey,Boolean
from app.database import Base
from sqlalchemy.orm import relationship


class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)

   
    template = Column(String(50), default="classic")
    primary_color = Column(String(20), default="#2563eb")
    secondary_color = Column(String(20), default="#1e293b")
    font_family = Column(String(50), default="Inter")
    layout = Column(String(50), default="standard")
    cover_image = Column(String(255), nullable=True)
    profile_image = Column(String(255), nullable=True)


    user = relationship("User", back_populates="themes")  