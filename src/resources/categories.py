from datetime import UTC, datetime
from fastapi import HTTPException, status

from src.data_layer.alchemy.models.categories import Category
from src.resources.base import BaseEntity
from src.schemas.categories import CategoriesSchema
from src.schemas.request.categories import CategoriesCreateSchema

class CategoriesEntity(BaseEntity):
    db_object = Category

    @classmethod
    async def find(cls, categories_id: int) -> CategoriesSchema:
        categories = await cls.db_object.get_by_id(categories_id)
        if not categories:
            raise HTTPException(status_code=404, detail="Category not found")
        return CategoriesSchema.model_validate(categories)

    @classmethod
    async def check_is_exists(cls, categories_id: int) -> bool:
        return bool(await cls.db_object.get_by_id(categories_id))

    @classmethod
    async def create(cls, categories_data: CategoriesCreateSchema) -> CategoriesSchema:
        categories_schema = CategoriesSchema(
            name=categories_data.name,
            parent_id=categories_data.parent_id,
            created_at=datetime.now(UTC)
        )
        await cls.db_object.create(categories_schema)
        return categories_schema

    async def to_view(self) -> CategoriesSchema:
        return CategoriesSchema.model_validate(self.db_object)
    
    @classmethod
    async def delete(cls, categories_id: int) -> None:
        if not await cls.check_is_exists(categories_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mistake in ID or category alredy deleted"
            )
        await cls.db_object.delete(categories_id)
