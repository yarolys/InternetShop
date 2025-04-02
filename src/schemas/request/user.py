from datetime import datetime, UTC
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

from src.schemas.enums.user import UserRole

class UserCreateSchema(BaseModel):
    email: EmailStr
    username: Optional[str] = Field(..., min_length=3, max_length=32)
    password: Optional[str]
