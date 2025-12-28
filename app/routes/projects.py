# app/routes/projects.py

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.project import ProjectCreate, ProjectResponse
from app.services.project_service import (
    get_user_projects,
    get_project,
    add_project,
    update_project,
    update_project_image,
    delete_project
)
from app.database import get_db
from app.utils.file_upload import save_file

from app.models.user import User
from app.core.dependencies import get_current_user  


router = APIRouter(
    prefix="/api/projects",
    tags=["Projects"]
)


# Get all projects for current user
@router.get("/", response_model=List[ProjectResponse])
def read_projects(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Return all projects for the logged-in user."""
    return get_user_projects(db, current_user.id)



# Get a single project by ID
@router.get("/{project_id}", response_model=ProjectResponse)
def read_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Return a specific project for the logged-in user."""
    project = get_project(db, project_id, current_user.id)
    return project



# Add a new project
@router.post("/", response_model=ProjectResponse)
def add_new_project(
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Add a new project for the logged-in user."""
    return add_project(db, current_user.id, project_data)



# Update an existing project (or add if not exist)
@router.put("/{project_id}", response_model=ProjectResponse)
def update_existing_project(
    project_id: int,
    project_data: ProjectCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Update a project, or add it if it doesn't exist."""
    return update_project(db, project_id, current_user.id, project_data)


# project image
@router.post("/{project_id}/image", response_model=ProjectResponse)
def upload_project_image(
    project_id: int,
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    project = get_project(db, project_id, current_user.id)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid image type")

    path = save_file(file, "projects", ["image/jpeg", "image/png"])
    project.image = path

    db.commit()
    db.refresh(project)
    return project





# Delete a project
@router.delete("/{project_id}")
def delete_existing_project(
    project_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Delete a project for the logged-in user."""
    return delete_project(db, project_id, current_user.id)
