from fastapi import FastAPI

from src.router.spa.user import router as user_router
from src.router.spa.auth import router as auth_router
from src.router.spa.product import router as product_router
from src.router.spa.categories import router as category_router
from src.router.spa.order import router as order_router
from src.router.spa.review import router as review_router
from src.router.spa.product_orders import router as product_order_router


def init_routers(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(product_router)
    app.include_router(category_router)
    app.include_router(order_router)
    app.include_router(review_router)
    app.include_router(product_order_router)