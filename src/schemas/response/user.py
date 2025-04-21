from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

from src.schemas.enums.user import UserRole


class UserDetailSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    email: EmailStr
    username: str = Field(..., min_length=3, max_length=32)
    role: UserRole
    balance: int
    active_order_id: int
    created_at: datetime

    class Config:
        from_attributes = True
        extra = "ignore"