from typing import List
from fastapi import APIRouter

from src.resources.product_orders import ProductOrderEntity
from src.schemas.request.product_orders import ProductOrderCreateSchema, ProductOrderGetSchema

router = APIRouter(
    prefix="/product_order",
    tags=["product order"],
)


@router.post(
    "",
    summary="Create new product order",
    status_code=201
)
async def create(prodorder_data: ProductOrderCreateSchema):
    await ProductOrderEntity.create(prodorder_data)


@router.get(
    "/{get_all}",
    response_model=List[ProductOrderGetSchema], status_code=200,
    summary="get all"
)
async def get_all_category():
    return await ProductOrderEntity.get_all()