from typing import Optional

from pydantic import BaseModel, Field


class CategoriesCreateSchema(BaseModel):
    name: str
    parent_id: Optional[int] = Field(default=None) 