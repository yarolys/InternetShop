from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, VARCHAR
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from .base import Base

if TYPE_CHECKING:
    from .product import Product

class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    name: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False, unique=True)
    parent_id: Mapped[int] = MappedColumn(ForeignKey("categories.id"), nullable=True)

    products: Mapped[list["Product"]] = relationship(back_populates="category")

    class Config:
        from_attributes = True