# app/routes/auth.py

# from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status, Response
# from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
# from app.database import get_db
from app.services.auth_service import authenticate_user, check_email_availability, register_user
from app.schemas.user import RegisterRequest, LoginRequest
from app.core.security import create_access_token
from app.core.dependencies import get_current_user
from app.database import get_db
from app.models import User
from pydantic import EmailStr
# from app.schemas.user import LoginRequest
# from app.core.security import create_access_token, pwd_context



router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register", status_code=201)
def register(data: RegisterRequest, db: Session = Depends(get_db)): # register a new user with hashpassword
    return register_user(db, data)



@router.get("/register/check-email")
def check_email(email: EmailStr, db: Session = Depends(get_db)): # check email is available
    return check_email_availability(db, email)


@router.post("/login")
def login(data: LoginRequest, response: Response, db: Session = Depends(get_db)):
    """
    Authenticate user and set JWT in cookie.
    """
    user = authenticate_user(db, data.email, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Create JWT token
    access_token = create_access_token({"sub": user.email})

    # Set token in HttpOnly cookie
    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="lax",  # adjust as needed for frontend
        secure=False,    # True if using HTTPS
        path="/"
    )

    return {"message": "Login successful"}



@router.post("/logout")
def logout(response: Response):
    response.delete_cookie(
        "access_token",
        path="/",
        httponly=True
    )
    return {"message": "Logged out"}


@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):   #Return details of the logged-in user.
    return {
        "username": current_user.username,
        "email": current_user.email
    }

