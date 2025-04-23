from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class OrderSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    user_id: Optional[int] = Field(default=None)
    total_price: Optional[float] = Field(default=None)
    status: str = Field(default="pending")
    created_at: datetime = Field(default=None)

    class Config:
        from_attributes = True