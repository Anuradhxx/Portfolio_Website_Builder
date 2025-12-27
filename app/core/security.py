# app/core/security.py

from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext
import os
# from app.main import pwd_context
from dotenv import load_dotenv

load_dotenv() #

SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")   # use environment variable in production
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

# print("SECRET_KEY loaded:", SECRET_KEY)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    return pwd_context.verify(password, hashed_password)


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)