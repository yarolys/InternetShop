from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, VARCHAR, Float
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

    # Используем строковые аннотации
    user: Mapped["User"] = relationship(back_populates="orders")
    products: Mapped[list["ProductOrder"]] = relationship(back_populates="order")

    class Config:
        from_attributes = True
