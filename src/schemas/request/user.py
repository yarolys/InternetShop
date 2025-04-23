from typing import Optional

from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class UserCreateSchema(BaseModel):
    email: EmailStr
    username: Optional[str] = Field(..., min_length=3, max_length=32)
    password: Optional[str]

    class Config:
        from_attributes = True