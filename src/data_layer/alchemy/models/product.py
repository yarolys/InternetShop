from typing import TYPE_CHECKING

from sqlalchemy import VARCHAR, select, Integer, Float, Text, ForeignKey
from sqlalchemy.orm import Mapped, MappedColumn, relationship

from src.schemas.product import ProductSchema
from src.data_layer.alchemy.models.categories import Category
from src.data_layer.alchemy.models.review import Review

from .base import Base


if TYPE_CHECKING:
    from src.data_layer.alchemy.models.categories import Category
    from src.data_layer.alchemy.models.review import Review

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = MappedColumn(primary_key=True, autoincrement=True)
    name: Mapped[str] = MappedColumn(VARCHAR(255), nullable=False, index=True)
    description: Mapped[str] = MappedColumn(Text, nullable=False)
    cost: Mapped[float] = MappedColumn(Float, nullable=False)
    category_id: Mapped[int] = MappedColumn(ForeignKey("categories.id"), nullable=False)
    quantity: Mapped[int] = MappedColumn(Integer, default=0)

    category: Mapped["Category"] = relationship(back_populates="products")
    reviews: Mapped[list["Review"]] = relationship(back_populates="product", cascade="all, delete-orphan")

    class Config:
        from_attributes = True

    @classmethod
    async def create(cls, product: ProductSchema) -> "Product":
        async with cls.get_session() as session:
            new_product = cls(
                name=product.name,
                description=product.description,
                cost=product.cost,
                category_id=product.category_id,
                quantity=product.quantity
            )
            session.add(new_product)
            await session.commit()
            await session.refresh(new_product)
            return new_product

    @classmethod
    async def get_by_id(cls, product_id: int) -> "Product | None":
        async with cls.get_session() as session:
            query = select(cls).where(cls.id == product_id)
            result = await session.execute(query)
            return result.scalar_one_or_none()