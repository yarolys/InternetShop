from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

from src.schemas.enums.user import UserRole


class UserSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=32)
    hashed_password: Optional[str]
    role: UserRole
    balance: Optional[int] = Field(default=0)
    active_order_id: Optional[int] = Field(default=None)

    created_at: datetime = Field(default=None)

    class Config:
        from_attributes = True