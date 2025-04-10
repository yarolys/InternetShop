from datetime import UTC, datetime

from pydantic import EmailStr
from fastapi import HTTPException
from src.data_layer.alchemy.models.order import Order
from src.resources.base import BaseEntity
from src.schemas.enums.user import UserRole
from src.schemas.request.user import UserCreateSchema
from src.schemas.user import UserSchema
from src.utills.hash_passwd import hash_password

class Entity(BaseEntity):
    db_object = Order