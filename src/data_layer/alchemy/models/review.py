from typing import List

from datetime import datetime, UTC
from sqlalchemy import ForeignKey, DateTime, Text, select
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.data_layer.alchemy.models.product import Product
from src.schemas.review import ReviewSchema

from .base import Base

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    product_id: Mapped[int] = MappedColumn(ForeignKey("products.id"), nullable=False)
    record: Mapped[str] = MappedColumn(Text, nullable=False)

    product: Mapped["Product"] = relationship(back_populates="reviews")

    @classmethod
    async def create(cls, review: ReviewSchema) -> ReviewSchema:
        async with cls.get_session() as session:
            new_review = cls(**review.model_dump())
            session.add(new_review)
            await session.commit()

            await session.refresh(new_review)

            return ReviewSchema.model_validate(new_review)

    @classmethod
    async def delete(cls, review_id: int):
        async with cls.get_session() as session:
            review = await cls.get_by_id(review_id)
            if not review:
                return
            await session.delete(review)
            await session.commit()

    @classmethod
    async def get_by_id(cls, review_id: int) -> "Review | None":
        async with cls.get_session() as session:
            query = select(cls).where(cls.id == review_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls) -> List["Review"]:
        async with cls.get_session() as session:
            query = select(cls)
            result = await session.execute(query)
            return result.scalars().all()
