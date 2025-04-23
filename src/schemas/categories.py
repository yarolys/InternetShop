from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CategoriesSchema(BaseModel):
    id: Optional[int] = Field(default=None)
    name: str  
    parent_id: Optional[int] = Field(default=None)
    created_at: datetime = Field(default=None)

    class Config:
        from_attributes = True
