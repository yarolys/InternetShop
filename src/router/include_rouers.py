from fastapi import FastAPI

from src.router.spa.user import router as user_router
from src.router.spa.auth import router as auth_router
from src.router.spa.product import router as product_router


def init_routers(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(user_router)
    app.include_router(product_router)