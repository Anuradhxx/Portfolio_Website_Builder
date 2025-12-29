# app/services/skill_service.py

from sqlalchemy.orm import Session
from app.models.skill import Skill
from app.schemas.skill import SkillCreate, SkillUpdate
from fastapi import HTTPException, status
from app.models.user import User


def create_skill(db: Session, user: User, data: SkillCreate) -> Skill:
    """Create a new skill for a user."""
    skill = Skill(
        user_id=user.id,
        name=data.name,
        proficiency_level=data.proficiency_level,
        icon=data.icon
    )
    db.add(skill)
    db.commit()
    db.refresh(skill)
    return skill



def get_user_skills(db: Session, user: User):
    """Return all skills for a user."""
    skills= db.query(Skill).filter(Skill.user_id == user.id).all()

    if not skills:
        raise HTTPException(
            status_code=404,
            detail="No skills added yet. Add skills."
        )

    return skills




def update_skill(db: Session, skill_id: int, user: User, data: SkillUpdate):
    skill = db.query(Skill).filter(
        Skill.id == skill_id,
        Skill.user_id == user.id
    ).first()

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    if data.name is not None:
        skill.name = data.name
    if data.Proficiency_level is not None:
        skill.proficiency_level = data.Proficiency_level
    if data.icon is not None:
        skill.icon = data.icon

    db.commit()
    db.refresh(skill)
    return skill


def delete_skill(db: Session, skill_id: int, user: User):
    skill = db.query(Skill).filter(
        Skill.id == skill_id,
        Skill.user_id == user.id
    ).first()

    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")

    db.delete(skill)
    db.commit()

