# app/routes/profile.py
# end points,logic

from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from app.schemas import ProfileCreate, ProfileResponse
from app.services.profile_service import (
    update_profile_data,
    update_profile_photo,
    update_profile_resume
)
from app.database import get_db
from app.models.user import User
from app.models.profile import Profile
from app.core.dependencies import get_current_user 
import os
from fastapi.responses import FileResponse 

router = APIRouter(
    prefix="/api/profile",
    tags=["Profile"]
)


# Update profile text fields
@router.put("/", response_model=ProfileResponse)
def update_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update the logged-in user's profile data (text fields only).
    """
    updated_profile = update_profile_data(db, current_user.id, profile_data)
    return updated_profile



# Upload profile photo
@router.post("/photo", response_model=ProfileResponse)
def upload_profile_photo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload or update the user's profile photo.
    """
    if file.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(status_code=400, detail="Invalid file type")
    
    update_profile_photo(db, current_user.id, file)
    # Return the updated profile
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    return profile



# Upload resume
@router.post("/resume", response_model=ProfileResponse)
def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload or update the user's resume PDF.
    """
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Invalid file type")

    update_profile_resume(db, current_user.id, file)
    # Return the profile after updation
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    return profile



# Download resume
@router.get("/resume/download")
def download_resume(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Download the logged-in user's resume."""
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    
    if not profile or not profile.resume_pdf:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    # Ensure the file exists on disk
    if not os.path.exists(profile.resume_pdf):
        raise HTTPException(status_code=404, detail="Resume file not found")
    
        # Return the file for download
    return FileResponse(
    path=profile.resume_pdf,
    filename=os.path.basename(profile.resume_pdf),
    media_type="application/pdf"
)


# Publish portfolio
@router.post("/publish")
def publish_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    profile.is_published = True
    db.commit()
    db.refresh(profile)

    return {"message": "Portfolio published"}


# Unpublish portfolio
@router.post("/unpublish")
def unpublish_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()

    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    profile.is_published = False
    db.commit()
    db.refresh(profile)

    return {"message": "Portfolio unpublished"}
