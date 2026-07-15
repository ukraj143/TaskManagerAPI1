from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ---------- USER ----------

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True


# ---------- TOKEN ----------

class Token(BaseModel):
    access_token: str
    token_type: str


# ---------- TASK ----------

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    completed: bool
    created_at: datetime
    user_id: int

    class Config:
        from_attributes = True
        