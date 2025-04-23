from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CategoriesCreateSchema(BaseModel):
    name: str
    parent_id: Optional[int] = Field(default=None) 

class CategoriesGetSchema(BaseModel):
    id: int
    name: str
    parent_id: Optional[int] = Field(default=None)
    created_at: datetime

    class Config:
        from_attributes = True