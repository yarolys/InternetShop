from datetime import UTC, datetime
from typing import List
from fastapi import HTTPException, status
from sqlalchemy import select

from src.data_layer.alchemy.models.categories import Category
from src.resources.base import BaseEntity
from src.schemas.categories import CategoriesSchema
from src.schemas.request.categories import CategoriesCreateSchema, CategoriesGetSchema

class CategoriesEntity(BaseEntity):
    db_object = Category

    @classmethod
    async def find(cls, category_id: int) -> CategoriesSchema:
        category = await cls.db_object.get_by_id(category_id)
        return CategoriesSchema.model_validate(category)

    @classmethod
    async def check_is_exists(cls, category_id: int) -> bool:
        return bool(await cls.db_object.get_by_id(category_id))

    @classmethod
    async def create(cls, category_data: CategoriesCreateSchema) -> CategoriesSchema:
        category_schema = CategoriesSchema(
            name=category_data.name,
            parent_id=category_data.parent_id,
            created_at=datetime.now(UTC)
        )
        await cls.db_object.create(category_schema)
        return category_schema

    async def to_view(self) -> CategoriesSchema:
        return CategoriesSchema.model_validate(self.db_object)
    
    @classmethod
    async def delete(cls, category_id: int) -> None:
        await cls.db_object.delete(category_id)


    @classmethod
    async def get_all(cls) -> List[CategoriesGetSchema]:
        category = await cls.db_object.get_all()
        return [CategoriesGetSchema.model_validate(c) for c in category]