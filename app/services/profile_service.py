# app/services/profile_service.py


# for profile update
import os
from fastapi import HTTPException
from sqlalchemy.orm import Session
from fastapi import UploadFile
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate
from app.utils.file_upload import save_file


def update_profile_data(db: Session, user_id: int, data: ProfileCreate) -> Profile:
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()

    if not profile:
        profile = Profile(
            user_id=user_id,
            full_name=data.full_name, 
            bio=data.bio,
            email=data.email,
            location= data.location,
            phone=data.phone,
            linkedin=data.linkedin,
            github=data.github,
        )
        db.add(profile)
    else:
        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(profile, key, value)

    db.commit()
    db.refresh(profile)
    return profile



# def update_profile_photo(db: Session, user_id: int, file: UploadFile) -> str:
#     """Upload a profile photo and update the profile."""
#     profile = get_or_create_profile(db, user_id)
#     path = save_file(file, "photos", allowed_types=["image/jpeg", "image/png"])
#     profile.profile_photo = path
#     db.commit()
#     db.refresh(profile)
#     return path


def update_profile_photo(db: Session, user_id: int, file: UploadFile) -> str:
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if not profile:
        raise HTTPException(400, "Create profile first")

    path = save_file(file, "photos", ["image/jpeg", "image/png"])
    profile.profile_photo = path
    db.commit()
    return path


def update_profile_resume(db: Session, user_id: int, file: UploadFile) -> str:
    """Upload a resume PDF and update the profile."""
    profile =db.query(Profile). filter(Profile.user_id == user_id).first()
    if not profile:
        raise HTTPException(400, "Create profile first")
    
    path = save_file(file, "resumes", ["application/pdf"])
    profile.resume_pdf = path
    db.commit()
    db.refresh(profile)
    return path


def get_resume_path(db: Session, user_id: int) -> str:
    profile = db.query(Profile).filter(Profile.user_id == user_id).first()
    if not profile or not profile.resume_pdf:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    if not os.path.exists(profile.resume_pdf):
        raise HTTPException(status_code=404, detail="Resume file not found on server")

    return profile.resume_pdf
