from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session

from app.database import get_db
from app.templates import templates
from app.services.portfolio_service import get_portfolio_data

router = APIRouter(
    prefix="/u",
    tags=["Public Portfolio"]
)


@router.get("/{user_id}", response_class=HTMLResponse)
def public_portfolio(
    request: Request,
    user_id: int,
    db: Session = Depends(get_db),
):
    data = get_portfolio_data(
        db=db,
        user_id=user_id,
        published_only=True
    )

    return templates.TemplateResponse(
        "portfolio.html",
        {
            "request": request,
            **data,
            "preview": False,
        },
    )
