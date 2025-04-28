from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProductOrderCreateSchema(BaseModel):
    product_id: Optional[int] = Field(default=None)
    order_id: Optional[int] = Field(default=None)
    count: int

class ProductOrderGetSchema(ProductOrderCreateSchema):
    created_at: datetime

    class Config:
        from_attributes = True