from pydantic import BaseModel, ConfigDict
from typing import Optional

class ThemeCreate(BaseModel):
    template: Optional[str] = "classic"
    primary_color: Optional[str]
    secondary_color: Optional[str]
    font_family: Optional[str]
    layout: Optional[str]
    dark_mode: Optional[bool]

class ThemeResponse(ThemeCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
