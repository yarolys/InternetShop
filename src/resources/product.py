from datetime import UTC, datetime
from decimal import Decimal

from fastapi import HTTPException, status

from src.data_layer.alchemy.models.product import Product
from src.resources.base import BaseEntity
from src.schemas.product import ProductSchema
from src.schemas.request.product import ProductCreateSchema


class ProductEntity(BaseEntity):
    db_object = Product

    @classmethod
    async def find(cls, product_id: int) -> ProductSchema:
        product = await cls.db_object.get_by_id(product_id)
        if not product:
            raise HTTPException(status_code=404, detail="Product not found")
        return ProductSchema.model_validate(product)

    @classmethod
    async def check_is_exists(cls, product_id: int) -> bool:
        return bool(await cls.db_object.get_by_id(product_id))

    @classmethod
    async def create(cls, product_data: ProductCreateSchema) -> ProductSchema:
        product_schema = ProductSchema(
            name=product_data.name,
            description=product_data.description,
            cost=Decimal(product_data.cost) if product_data.cost else Decimal('0.0'),
            category_id=product_data.category_id,
            quantity=product_data.quantity,
            created_at=datetime.now(UTC)
        )
        await cls.db_object.create(product_schema)
        return product_schema

    async def to_view(self) -> ProductSchema:
        return ProductSchema.model_validate(self.db_object)
    
    @classmethod
    async def delete(cls, product_id: int) -> None:
        if not await cls.check_is_exists(product_id):
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Mistake in ID or product already deleted"
            )
        await cls.db_object.delete(product_id)
