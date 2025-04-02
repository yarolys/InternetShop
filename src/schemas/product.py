from datetime import datetime, UTC
from typing import Optional

from pydantic import BaseModel, Field
from decimal import Decimal

from src.schemas.enums.user import UserRole


class ProductSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str  
    description: str = Field(..., min_length=3, max_length=128)
    cost: Optional[Decimal]
    role: UserRole
    category_id: Optional[int] = Field(default=0)
    quantity: Optional[int] = Field(default=None)

    created_at: Optional[datetime] = Field(default=None)

    class Config:
        from_attributes = True

