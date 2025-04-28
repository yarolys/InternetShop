from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ProductOrderSchema(BaseModel):
    product_id: Optional[int] = Field(default=None)
    order_id: Optional[int] = Field(default=None)
    count: Optional[int] = Field(default=None)
    created_at: datetime = Field(default=None)

    class Config:
        from_attributes = True
