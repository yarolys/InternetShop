from datetime import UTC, datetime
from typing import List

from src.data_layer.alchemy.models.order import Order
from src.resources.base import BaseEntity
from src.schemas.order import OrderSchema
from src.schemas.request.order import OrderCreateSchema, OrderGetSchema


class OrderEntity(BaseEntity):
    db_object = Order

    @classmethod
    async def find(cls, order_id: int) -> OrderSchema:
        category = await cls.db_object.get_by_id(order_id)
        return OrderSchema.model_validate(category)

    @classmethod
    async def check_is_exists(cls, category_id: int) -> bool:
        return bool(await cls.db_object.get_by_id(category_id))

    @classmethod
    async def create(cls, order_data: OrderCreateSchema) -> OrderSchema:
        order_schema = OrderSchema(
            user_id=order_data.user_id,
            total_price=order_data.total_price,
            status=order_data.status,
            created_at=datetime.now(UTC)
        )
        await cls.db_object.create(order_schema)
        return order_schema

    async def to_view(self) -> OrderSchema:
        return OrderSchema.model_validate(self.db_object)

    @classmethod
    async def delete(cls, order_id: int) -> None:
        await cls.db_object.delete(order_id)

    @classmethod
    async def get_all(cls) -> List[OrderGetSchema]:
        category = await cls.db_object.get_all()
        return [OrderGetSchema.model_validate(c) for c in category]