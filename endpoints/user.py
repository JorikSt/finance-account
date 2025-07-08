from fastapi import APIRouter, status
from schemas.auth import UserCreate


router = APIRouter()


@router.post('/register', status_code=status.HTTP_201_CREATED)
def register_user(user: UserCreate):
    return {
            "status": "success",
            "user": user
            }
