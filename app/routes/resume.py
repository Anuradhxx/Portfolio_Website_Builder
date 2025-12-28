import os
from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.dependencies import get_current_user
from app.models.profile import Profile

UPLOAD_ROOT = "uploads"

router = APIRouter(
    prefix="/resume",
    tags=["Resume"]
)


@router.get("/download")
def download_resume(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    profile = (
        db.query(Profile)
        .filter(Profile.user_id == current_user.id)
        .first()
    )

    if not profile or not profile.resume_pdf:
        raise HTTPException(status_code=404, detail="Resume not found")

    file_path = os.path.join(UPLOAD_ROOT, profile.resume_pdf)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return FileResponse(
        path=file_path,
        filename=os.path.basename(file_path),
        media_type="application/pdf",
    )
