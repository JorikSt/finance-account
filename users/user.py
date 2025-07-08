from pydantic import BaseModel, HttpUrl, ValidationError
from typing import Optional



class UserUpdate(BaseModel):
    first_name: str
    last_name: Optional[str] = None
    bio: Optional[str] = None
    avatar_url: Optional[str]= None # to-path


class UserProfile(UserUpdate):
    id: str
    email: str
    confirmed: bool
    created_at: str