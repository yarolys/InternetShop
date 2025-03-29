from typing import Optional

from fastapi import Depends, HTTPException, status

from src.depends.get_current_token import get_current_token
from src.schemas.enums.user import UserRole
from src.schemas.token import TokenPayloadSchema


def roles_required(*, allowed_roles: Optional[list[UserRole]] = None, check_any_role: bool = False):
    """
    Check user roles or any role, if check_any_role is True
    !!! works only with keyword arguments !!!
    Args:
        allowed_roles:
        check_any_role:

    Returns: None

    Raises:
        HTTPException(HTTP_403_FORBIDDEN)

    """
    def wrapper(token_data: TokenPayloadSchema = Depends(get_current_token)):
        if check_any_role:
            return
        if token_data.role in allowed_roles or not allowed_roles:
            return
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="forbidden")

    return Depends(wrapper)