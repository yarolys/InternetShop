from decimal import Decimal
from typing import Optional

from pydantic import BaseModel, Field


class ProductCreateSchema(BaseModel):
    name: str
    description: Optional[str] = Field(..., min_length=3, max_length=64)
    cost: Optional[Decimal] = Field(..., gt=0)
    quantity: Optional[int] = Field(1, ge=0)
    category_id: Optional[int] = Field(..., ge=1)
