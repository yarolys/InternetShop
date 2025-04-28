from datetime import UTC, datetime
from typing import List

from src.data_layer.alchemy.models.product_orders import ProductOrder
from src.resources.base import BaseEntity
from src.schemas.product_orders import ProductOrderSchema
from src.schemas.request.product_orders import ProductOrderCreateSchema, ProductOrderGetSchema


class ProductOrderEntity(BaseEntity):
    db_object = ProductOrder


    @classmethod
    async def create(cls, prodorder_data: ProductOrderCreateSchema) -> ProductOrderSchema:

        prodorder_schema = ProductOrderSchema(
            product_id=prodorder_data.product_id,
            order_id=prodorder_data.order_id,
            count=prodorder_data.count,
            created_at=datetime.now(UTC)
        )
        await cls.db_object.create(prodorder_schema)
        return prodorder_schema

    async def to_view(self) -> ProductOrderSchema:
        return ProductOrderSchema.model_validate(self.db_object)


    @classmethod
    async def get_all(cls) -> List[ProductOrderGetSchema]:
        prodorder = await cls.db_object.get_all()
        return [ProductOrderGetSchema.model_validate(c) for c in prodorder]