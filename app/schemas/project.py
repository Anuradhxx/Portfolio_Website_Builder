# app/schemas/project.py

from pydantic import BaseModel, ConfigDict,Field
from typing import Optional


class ProjectCreate(BaseModel):
    title: str = Field(..., min_length=1)
    description: Optional[str] = None
    tech_stack: Optional[str] = None
    github_link: Optional[str] = None
    demo_link: Optional[str] = None
    is_featured: bool = False
    order:int = 0


class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    tech_stack: Optional[str] = None
    github_link: Optional[str] = None
    demo_link: Optional[str] = None
    is_featured: Optional[bool] = None
    order: Optional[int] = None


class ProjectResponse(ProjectCreate):
    id: int
    title: str
    description: Optional[str]
    tech_stack: Optional[str]
    github_link: Optional[str]
    demo_link: Optional[str]
    image: Optional[str]
    is_featured: bool
    order: int

    model_config = ConfigDict(from_attributes=True)
