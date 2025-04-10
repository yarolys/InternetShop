from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReviewCreateSchema(BaseModel):
    product_id: Optional[int] = Field(default=None, description="ID связанного продукта")
    record: str = Field(..., description="Текстовая запись/описание категории")
    date: datetime = Field(..., description="Дата создания записи")

    class Config:
        from_attributes = True