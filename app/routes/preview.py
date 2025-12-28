#app/routes/preview.py

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse 
from fastapi.requests import Request
from sqlalchemy.orm import Session

from app.database import get_db
from app.core.dependencies import get_current_user
from app.models.user import User
from app.templates import templates
from app.services.portfolio_service import get_portfolio_data
from app.templates import templates


router = APIRouter(
    prefix="/api/preview",
    tags=["Preview"]
)


@router.get("/", response_class=HTMLResponse)
def preview_portfolio(
    request: Request,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    data = get_portfolio_data(
        db=db,
        user_id=current_user.id,
        published_only=False
    )

    return templates.TemplateResponse(
        "portfolio.html",
        {
            "request": request,
            "user": current_user,
            **data,
            "preview": True,
        },
    )
