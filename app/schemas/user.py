# app/schemas/user.py

from pydantic import BaseModel, Field, EmailStr, validator




class RegisterRequest(BaseModel):
    username: str
    email:EmailStr
    password:str = Field(min_length=8, max_length=72)  #8 character

    @validator("password")
    def password_min_length(cls, v):
        if len(v) < 8:
            raise ValueError("Fill at least 8 characters")
        return v

class LoginRequest (BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"    