# app/schemas/skill.py

from pydantic import BaseModel, ConfigDict,Field
from typing import Optional

class SkillCreate(BaseModel):
    name: str = Field(..., min_length=1)
    proficiency_level:int = Field(..., ge=1, le=5)
    icon: Optional[str] = None

class SkillUpdate(BaseModel):
    name: Optional[str]
    Proficiency_level: Optional[int] = Field(None, ge=1, le=10)
    icon: Optional[str]


class SkillResponse(SkillCreate):
    id: int
    name:str
    proficiency_level: int
    icon: Optional[str]

    model_config = ConfigDict(from_attributes=True)

