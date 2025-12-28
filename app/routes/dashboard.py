from fastapi import APIRouter, Request, Depends, Response
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from app.templates import templates
from app.database import get_db
from app.core.dependencies import get_current_user
from app.services.portfolio_service import get_portfolio_data



router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/", response_class=HTMLResponse)
def dashboard(
    request: Request,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    
    return templates.TemplateResponse(
        "dashboard.html",
        {
            "request": request,
            "user": current_user
        }
    )



    # data = get_portfolio_data(db, current_user.id, published_only=False)
    # return templates.TemplateResponse(
    #     "dashboard.html",
    #     {"request": request, "user": current_user, **data}
    # )
