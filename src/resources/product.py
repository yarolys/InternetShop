from sqlalchemy import select
from fastapi import HTTPException
from src.data_layer.alchemy.models.product import Product
from src.resources.base import BaseEntity
from src.schemas.enums.user import UserRole
from src.schemas.product import ProductSchema


class ProductEntity(BaseEntity):
    db_object = Product


    @classmethod
    async def find(cls, product_id: int) -> ProductSchema:
        async with cls.get_session() as session:
            query = select(Product).where(Product.id == product_id)
            result = await session.execute(query)
            product = result.scalar_one_or_none()

            if not product:
                raise HTTPException(status_code=404, detail="Product not found")
            
            return ProductSchema.model_validate(product)
             # метод на поиск нашего продукта
        

    @classmethod
    async def check_is_exists(cls, product_id: int) -> bool:
        async with cls.get_session() as session:
            query = select(Product.id).where(Product.id == product_id)
            result = await session.execute(query)
            return result.scalar_one_or_none() is not None # метод на проверку
      

    @classmethod
    async def create(cls, product_data: ProductSchema) -> ProductSchema:
        async with cls.get_session() as session:
            new_product = Product(
                name=product_data.name,
                description=product_data.description,
                cost=product_data.cost,
                category_id=product_data.category_id,
                role=UserRole.ADMIN or UserRole.SUPERADMIN,
                quantity=product_data.quantity
            )
            session.add(new_product)
            await session.commit()
            await session.refresh(new_product)
            return ProductSchema.model_validate(new_product) # метод на создание
        
    async def to_view(self) -> ProductSchema:
        return ProductSchema.model_validate(self.db_object)