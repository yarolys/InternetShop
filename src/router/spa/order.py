from typing import List
from fastapi import APIRouter

from src.depends.required_role import roles_required
from src.resources.order import OrderEntity
from src.schemas.enums.user import UserRole
from src.schemas.request.order import OrderGetSchema, OrderCreateSchema

router = APIRouter(
    prefix="/order",
    tags=["orders"],
)


@router.post(
    "",
    summary="Create new order",
    status_code=201
)
async def create(order_data: OrderCreateSchema):
    await OrderEntity.create(order_data)


@router.delete(
    "",
    summary="delete order",
    status_code=204,
    dependencies=[roles_required(allowed_roles=[UserRole.ADMIN, UserRole.SUPERADMIN])]
)
async def delete(order_id: int):
    await OrderEntity.delete(order_id=order_id)
    return


@router.get(
    "",
    response_model=List[OrderGetSchema], status_code=200,
    summary="Get all"
)
async def get_all_category():
    return await OrderEntity.get_all()