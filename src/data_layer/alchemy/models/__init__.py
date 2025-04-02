from .base import Base
from .user import User
from .order import Order
from .product_orders import ProductOrder
from .product import Product
from .categories import Category
from .review import Review
from sqlalchemy.orm import relationship

# Явно конфигурируем отношения после определения всех моделей
def configure_relationships():
    User.orders = relationship("Order", back_populates="user", cascade="all, delete-orphan")
    Order.user = relationship("User", back_populates="orders")
    Order.products = relationship("ProductOrder", back_populates="order")
    ProductOrder.order = relationship("Order", back_populates="products")

# Вызываем функцию конфигурации
configure_relationships()

__all__ = ['Base', 'User', 'Order', 'ProductOrder', 'Product', 'Category', 'Review']