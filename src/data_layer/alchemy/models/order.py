from typing import TYPE_CHECKING

from datetime import datetime, UTC
from typing import List

from sqlalchemy import ForeignKey, VARCHAR, DateTime, Float
from sqlalchemy.orm import Mapped, MappedColumn, relationship


from src.data_layer.alchemy.models.user import User
from src.data_layer.alchemy.models.product_orders import ProductOrder

from .base import Base

if TYPE_CHECKING:
    from .user import User

class Order(Base):
    __tablename__ = "orders"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = MappedColumn(ForeignKey("users.id"), nullable=False)
    total_price: Mapped[float] = MappedColumn(Float, nullable=False)
    status: Mapped[str] = MappedColumn(nullable=False, default="pending")

    user: Mapped["User"] = relationship("User", back_populates="orders")

    class Config:
        from_attributes = True