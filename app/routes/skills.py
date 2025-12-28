# app/routes/skills.py

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from typing import List
from app.schemas.skill import SkillCreate, SkillResponse, SkillUpdate
from app.services.skill_service import (
    create_skill,
    get_user_skills,
    update_skill,
    delete_skill
)
from app.database import get_db
from app.models.user import User
from app.core.dependencies import get_current_user  

router = APIRouter(
    prefix="/api/skills",
    tags=["Skills"]
)



# Add a new skill
@router.post("/", response_model=SkillResponse, status_code=201)
def add_skill(
    data: SkillCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_skill(db, current_user, data)




# Get all list of skills for the current user
@router.get("", response_model=list[SkillResponse])
def list_skills(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_user_skills(db, current_user)



# edit(Update) skill by ID
@router.put("/{skill_id}",operation_id="update_skill",response_model=SkillResponse)
def edit_skill(
    skill_id: int,
    data: SkillUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_skill(db, skill_id, current_user, data)



# Delete a skill
@router.delete("/{skill_id}", operation_id="Delete skill",status_code=204)
def remove_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    delete_skill(db, skill_id, current_user)
