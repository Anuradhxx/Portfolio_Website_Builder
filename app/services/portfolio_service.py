from sqlalchemy.orm import Session
from app.models import Profile, Skill, Project

def get_portfolio_data(db: Session, user_id: int, published_only: bool):
    profile_query = db.query(Profile).filter(Profile.user_id == user_id)
    skill_query = db.query(Skill).filter(Skill.user_id == user_id)
    project_query = db.query(Project).filter(Project.user_id == user_id)

    if published_only:
        profile_query = profile_query.filter(Profile.is_published == True)
        skill_query = skill_query.filter(Skill.is_published == True)
        project_query = project_query.filter(Project.is_published == True)

    return {
        "profile": profile_query.first(),
        "skills": skill_query.all(),
        "projects": project_query
            .order_by(Project.is_featured.desc(), Project.order.asc())
            .all()
    }
