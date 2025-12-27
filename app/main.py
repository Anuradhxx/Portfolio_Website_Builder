# app/main.py

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
# from app import models
import os
from fastapi.staticfiles import StaticFiles
from app.templates import templates

# from app.routes import skills, pages


# Routers
from app.routes.auth import router as auth_router
from app.routes.profile import router as profile_router
from app.routes.skills import router as skills_router
from app.routes.projects import router as projects_router
from app.routes.preview import router as preview_router
from app.routes.pages import router as pages_router
from app.routes.dashboard import router as dashboard_router



# Create database tables

Base.metadata.create_all(bind=engine)


# App instance
app = FastAPI(
    title="Portfolio API",
    description="API for managing Users profiles, skills, and projects",
    version="1.0.0",
)


app.mount("/static", StaticFiles(directory="app/static"), name="static")


# CORS (frontend support)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],  # only frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure the uploads folder exists (optional safety)
os.makedirs("uploads", exist_ok=True)
#static files(uploads)
app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")

 


# Register routers
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(skills_router)
app.include_router(projects_router)
app.include_router(preview_router)
app.include_router(pages_router)
app.include_router(dashboard_router)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "home.html",
        {"request": request}
    )


# Health check
# @app.get("/")
# def root():
#     return {"status": "Portfolio API is running"}
