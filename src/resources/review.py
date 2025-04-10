from datetime import UTC, datetime

from fastapi import HTTPException

from src.data_layer.alchemy.models.review import Review
from src.resources.base import BaseEntity
from src.schemas.request.user import UserCreateSchema
from src.schemas.user import UserSchema
from src.utills.hash_passwd import hash_password

class ReviewEntity(BaseEntity):
    db_object = Review