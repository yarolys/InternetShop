from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, Integer
from sqlalchemy.orm import Mapped, MappedColumn, relationship
from .base import Base

if TYPE_CHECKING:
    from .order import Order

class ProductOrder(Base):
    __tablename__ = "product_orders"

    product_id: Mapped[int] = MappedColumn(ForeignKey("products.id"), primary_key=True)
    order_id: Mapped[int] = MappedColumn(ForeignKey("orders.id"), primary_key=True)
    count: Mapped[int] = MappedColumn(Integer, nullable=False, default=1)

    order: Mapped["Order"] = relationship(back_populates="products")
    
    class Config:
        from_attributes = True