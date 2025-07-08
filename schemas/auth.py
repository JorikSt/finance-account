from pydantic import BaseModel
from typing import Optional


class UserCreate(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: str


class EmailConfirm(BaseModel):
    email: str
    code: str

class Config:
    orm_mode = True