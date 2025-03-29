from typing import Optional

from pydantic import BaseModel, Field
from pydantic.networks import EmailStr


class UserLoginSchema(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = Field(None, min_length=3, max_length=32)
    password: Optional[str]
