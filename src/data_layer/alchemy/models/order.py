from typing import TYPE_CHECKING, List
from sqlalchemy import ForeignKey, VARCHAR, Float, select
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.schemas.order import OrderSchema
from .base import Base

if TYPE_CHECKING:
    from .user import User
    from .product_orders import ProductOrder

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = MappedColumn(ForeignKey("users.id"), nullable=False)
    total_price: Mapped[float] = MappedColumn(Float, nullable=False)
    status: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False, default="pending")

    # Используем строковые аннотации
    user: Mapped["User"] = relationship(back_populates="orders")
    products: Mapped[list["ProductOrder"]] = relationship(back_populates="order")

    @classmethod
    async def create(cls, order: OrderSchema) -> OrderSchema:
        async with cls.get_session() as session:
            new_order = cls(**order.model_dump())
            session.add(new_order)
            await session.commit()

            await session.refresh(new_order)

            return OrderSchema.model_validate(new_order)

    @classmethod
    async def delete(cls, order_id: int):
        async with cls.get_session() as session:
            order = await cls.get_by_id(order_id)
            if not order:
                return
            await session.delete(order)
            await session.commit()

    @classmethod
    async def get_by_id(cls, order_id: int) -> "Order | None":
        async with cls.get_session() as session:
            query = select(cls).where(cls.id == order_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()

    @classmethod
    async def get_all(cls) -> List["Order"]:
        async with cls.get_session() as session:
            query = select(cls)
            result = await session.execute(query)
            return result.scalars().all()
