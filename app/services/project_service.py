# app/services/project_service.py

from sqlalchemy.orm import Session
from app.models.project import Project
from app.schemas.project import ProjectCreate, ProjectUpdate
from fastapi import UploadFile, HTTPException

def get_user_projects(db: Session, user_id: int):
    """Return all projects for a user."""
    projects= db.query(Project).filter(Project.user_id == user_id).order_by(Project.is_featured.desc(), Project.order.asc()).all()

    return projects


def get_project(db: Session, project_id: int, user_id: int):
    """Return a specific project for a user, or None if not found."""
    return db.query(Project).filter(Project.id == project_id, Project.user_id == user_id).first()


def add_project(db: Session, user_id: int, project_data: ProjectCreate) -> Project:
    """Add a new project for a user."""
    new_project = Project(
        user_id=user_id,
        title=project_data.title,
        description=project_data.description,
        tech_stack=project_data.tech_stack,
        github_link=project_data.github_link,
        demo_link=project_data.demo_link
    )
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


def update_project(db: Session, project_id: int, user_id: int, project_data: ProjectCreate) -> Project:
    """Update an existing project, or add it if it doesn't exist."""
    project = get_project(db, project_id, user_id)
    if not project:
        return add_project(db, user_id, project_data)
    
    project.title = project_data.title
    project.description = project_data.description
    project.tech_stack = project_data.tech_stack
    project.github_link = project_data.github_link
    project.demo_link = project_data.demo_link
    
    db.commit()
    db.refresh(project)
    return project


def update_project_image(db: Session, project_id: int, user_id: int, data: ProjectUpdate):
    project = get_project(db, project_id, user_id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(project, key, value)

    db.commit()
    db.refresh(project)
    return project



def delete_project(db: Session, project_id: int, user_id: int):
    """Delete a project for a user, or do nothing if it doesn't exist."""
    project = get_project(db, project_id, user_id)
    if project:
        db.delete(project)
        db.commit()
    return {"detail": "Project deleted successfully"}
