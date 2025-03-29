from datetime import datetime

from pydantic import BaseModel, Field

from src.schemas.enums.user import UserRole


class TokenPayloadSchema(BaseModel):
    user_id: int = Field(alias="sub")
    role: UserRole
    iat: datetime
    exp: datetime

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str