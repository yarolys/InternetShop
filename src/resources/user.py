from datetime import UTC, datetime

from pydantic import EmailStr
from fastapi import HTTPException
from src.data_layer.alchemy.models.user import User
from src.resources.base import BaseEntity
from src.schemas.enums.user import UserRole
from src.schemas.request.user import UserCreateSchema
from src.schemas.user import UserSchema
from src.utills.hash_passwd import hash_password
class UserEntity(BaseEntity):
    db_object = User

    @classmethod
    async def find(cls, *, user_id: int = None, email: EmailStr = None, username: str = None):
        user = await cls.db_object.get_db_obj(user_id=user_id, email=email, username=username)
        return cls(db_object=user)

    @classmethod
    async def create(cls, user: UserCreateSchema):
        hashed_password = hash_password(user.password)
        if not (await cls.find(email=user.email) or await cls.find(username=user.username)):
            raise HTTPException(status_code=400, detail="User already exists")
        await User.create(
            UserSchema(
                email=user.email,
                username=user.username,
                hashed_password=hashed_password,
                role=UserRole.USER,
                created_at=datetime.now(UTC)
            )
        )
    async def to_view(self):
        return UserSchema.model_validate(self.db_object)