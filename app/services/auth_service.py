# app/services/auth_service.py

from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.models.user import User
from app.core.security import pwd_context, hash_password, pwd_context
from fastapi import HTTPException
from app.schemas.user import RegisterRequest
from pydantic import EmailStr


def authenticate_user(db: Session, email: EmailStr, password: str) -> None:
    """
    Check if the user exists and the password is correct.
    Returns the User object if authentication succeeds, None otherwise.
    """
    user = db.query(User).filter(User.email == email).first()
    if not user or not pwd_context.verify(password, user.password_hash):
        return None
    return user


def register_user(db: Session, data: RegisterRequest):
    """
    Registers a new user with hashed password.
    Raises 400 if username or email already exists.
    """
    hashed_password = hash_password(data.password)
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status_code=400, detail="Username already exists")
    
    
    if db.query(User).filter(User.email == data.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")
 
    
    # hashed_pw = hash_password(data.password)

    user = User(
        username=data.username,
        email=data.email,
        password_hash=pwd_context.hash(data.password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"message": "User registered successfully"}


def check_email_availability(db: Session, email: EmailStr) -> dict:
    """
    Checks if an email is already registered.
    """
    user = db.query(User).filter(User.email == email).first()
    if user:
        return {"available": False, "message": "Already registered with this email"}
    
    return {"available": True, "message": "email is available"}







