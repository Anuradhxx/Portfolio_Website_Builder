# app/routes/pages.py

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
# from fastapi.templating import Jinja2Templates

from app.core.dependencies import get_current_user
from app.models.user import User
from app.templates import templates

# from app.models.skill import Skill
# from app.models.project import Project

router = APIRouter(tags=["Pages"])


@router.get("/home", response_class=HTMLResponse)
def home_page(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )


@router.get("/login", response_class=HTMLResponse)
def login_page(request: Request):
    return templates.TemplateResponse(
        "auth/login.html",
        {"request": request}
    )


@router.get("/register", response_class=HTMLResponse)
def register_page(request: Request):
    return templates.TemplateResponse(
        "auth/register.html",
        {"request": request}
    )



@router.get("/skills")
def skills_page(request: Request):
    return templates.TemplateResponse(
        "skills.html",
        {"request": request}
    )


@router.get("/projects")
def projects_page(request: Request):
    return templates.TemplateResponse(
        "projects.html",
        {"request": request}
    )


@router.get("/preview")
def skills_page(request: Request):
    return templates.TemplateResponse(
        "preview.html",
        {"request": request}
    )


@router.get("/profiles")
def skills_page(request: Request):
    return templates.TemplateResponse(
        "profile.html",
        {"request": request}
    )







# @router.get("/dashboard", response_class=HTMLResponse)
# def dashboard(
#     request: Request,
#     current_user: User = Depends(get_current_user)
# ):
#     return templates.TemplateResponse(
#         "dashboard.html",
#         {
#             "request": request,
#             "user": current_user
#         }
#     )
