from datetime import datetime, UTC
from typing import Optional

from pydantic import BaseModel, Field
from pydantic.networks import EmailStr

from src.schemas.enums.user import UserRole

class ProductCreateSchema(BaseModel):
    name: str
    description: Optional[str] = Field(..., min_length=3, max_length=32)
    cost: Optional[str]
