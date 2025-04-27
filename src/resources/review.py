from datetime import datetime, UTC
from typing import List

from src.data_layer.alchemy.models.review import Review
from src.resources.base import BaseEntity
from src.schemas.request.review import ReviewCreateSchema, ReviewGetSchema
from src.schemas.review import ReviewSchema


class ReviewEntity(BaseEntity):
    db_object = Review

    @classmethod
    async def find(cls, review_id: int) -> ReviewSchema:
        review = await cls.db_object.get_by_id(review_id)
        return ReviewSchema.model_validate(review)

    @classmethod
    async def check_is_exists(cls, review_id: int) -> bool:
        return bool(await cls.db_object.get_by_id(review_id))

    @classmethod
    async def create(cls, review_data: ReviewCreateSchema) -> ReviewSchema:
        review_schema = ReviewSchema(
            product_id=review_data.product_id,
            record=review_data.record,
            created_at=datetime.now(UTC)
        )
        await cls.db_object.create(review_schema)
        return review_schema

    async def to_view(self) -> ReviewSchema:
        return ReviewSchema.model_validate(self.db_object)

    @classmethod
    async def delete(cls, review_id: int) -> None:
        await cls.db_object.delete(review_id)

    @classmethod
    async def get_all(cls) -> List[ReviewGetSchema]:
        review = await cls.db_object.get_all()
        return [ReviewGetSchema.model_validate(c) for c in review]