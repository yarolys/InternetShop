from typing import TYPE_CHECKING, List
from datetime import datetime, UTC
from sqlalchemy import ForeignKey, VARCHAR, DateTime, Float
from sqlalchemy.orm import Mapped, MappedColumn, relationship
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

    user: Mapped["User"] = relationship(back_populates="orders")
    products: Mapped[List["ProductOrder"]] = relationship(back_populates="order")

    class Config:
        from_attributes = True
