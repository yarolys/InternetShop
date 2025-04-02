from datetime import datetime, UTC
from sqlalchemy import ForeignKey, DateTime, Text
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.data_layer.alchemy.models.product import Product

from .base import Base

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = MappedColumn(ForeignKey("products.id"), nullable=False)
    record: Mapped[str] = MappedColumn(Text, nullable=False)
    date: Mapped[datetime] = MappedColumn(DateTime, default=datetime.now(UTC))

    product: Mapped["Product"] = relationship(back_populates="reviews")

    class Config:
        from_attributes = True