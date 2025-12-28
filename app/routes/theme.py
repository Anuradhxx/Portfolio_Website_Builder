from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.core.dependencies import get_current_user
from app.schemas.theme import ThemeCreate, ThemeResponse
from app.services.theme_service import update_theme
from app.models.user import User

router = APIRouter(prefix="/theme", tags=["Theme"])

@router.put("/", response_model=ThemeResponse)
def update_user_theme(
    data: ThemeCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_theme(db, current_user.id, data)
