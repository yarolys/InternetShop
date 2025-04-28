from typing import TYPE_CHECKING, List

from sqlalchemy import ForeignKey, Integer, select
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.schemas.product_orders import ProductOrderSchema
from .base import Base

if TYPE_CHECKING:
    from .order import Order

class ProductOrder(Base):
    __tablename__ = "product_orders"

    product_id: Mapped[int] = MappedColumn(ForeignKey("products.id"), primary_key=True)
    order_id: Mapped[int] = MappedColumn(ForeignKey("orders.id"), primary_key=True)
    count: Mapped[int] = MappedColumn(Integer, nullable=False, default=1)

    order: Mapped["Order"] = relationship(back_populates="products")

    @classmethod
    async def create(cls, prodorder: ProductOrderSchema) -> ProductOrderSchema:
        async with cls.get_session() as session:
            new_prodorder = cls(**prodorder.model_dump())
            session.add(new_prodorder)
            await session.commit()

            await session.refresh(new_prodorder)

            return ProductOrderSchema.model_validate(new_prodorder)


    @classmethod
    async def get_all(cls) -> List["ProductOrder"]:
        async with cls.get_session() as session:
            query = select(cls)
            result = await session.execute(query)
            return result.scalars().all()