from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class OrderCreateSchema(BaseModel):
    user_id: Optional[int] = Field(default=None)
    total_price: Optional[float] = Field(default=None)
    status: str = Field(default="pending")

    class Config:
        from_attributes = True