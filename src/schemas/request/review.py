from datetime import datetime

from pydantic import BaseModel


class ReviewCreateSchema(BaseModel):
    product_id: int
    record: str


class ReviewGetSchema(BaseModel):
    id: int
    product_id: int
    record: str
    created_at: datetime

    class Config:
        from_attributes = True