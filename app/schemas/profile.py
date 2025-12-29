# app/schemas/profile.py

from pydantic import BaseModel, ConfigDict
from typing import Optional


class ProfileCreate(BaseModel):

    full_name: str
    bio: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    location: Optional[str] = None
    linkedin: Optional[str] = None
    github: Optional[str] = None



class ProfileResponse(ProfileCreate):
    # id = int
    profile_photo: Optional[str] = None
    resume_pdf: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)

