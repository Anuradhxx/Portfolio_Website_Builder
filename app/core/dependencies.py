# app/core/dependencies.py

from fastapi import Depends, HTTPException, Request
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from app.schemas.user import EmailStr
from fastapi.responses import RedirectResponse

from app.database import get_db
from app.models.user import User
from app.core.security import SECRET_KEY, ALGORITHM



def get_current_user(request: Request, db: Session = Depends(get_db)) -> User:
    token = request.cookies.get("access_token")
    if not token:
        return RedirectResponse("/login", status_code=302)
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: EmailStr | None = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or Expire token")
    
    user = db.query(User).filter(User.email == email).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user