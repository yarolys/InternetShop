from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class ReviewSchema(BaseModel):
    id: Optional[int] = Field(default=None, description="Уникальный идентификатор категории")
    product_id: Optional[int] = Field(default=None, description="ID связанного продукта")
    record: str = Field(..., description="Текстовая запись/описание категории")
    date: datetime = Field(..., description="Дата создания записи")
    created_at: datetime = Field(default=None)

    class Config:
        from_attributes = True