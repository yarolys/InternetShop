"""initial

Revision ID: 9d54c8441b86
Revises: 
Create Date: 2025-03-29 23:14:00.683836

"""
from datetime import UTC
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import ENUM

# revision identifiers, used by Alembic.
revision: str = '9d54c8441b86'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    userrole = ENUM('USER', 'ADMIN', 'SUPERADMIN', 'BANNED', name='userrole', create_type=False)
    userrole.create(op.get_bind(), checkfirst=True)
    

    op.create_table('users',
        sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
        sa.Column('email', sa.VARCHAR(length=255), nullable=False),
        sa.Column('username', sa.VARCHAR(length=32), nullable=False),
        sa.Column('hashed_password', sa.String(), nullable=False),
        sa.Column('role', userrole, nullable=False),
        sa.Column('balance', sa.Integer(), nullable=False),
        sa.Column('active_order_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(timezone=UTC), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    
    userrole = ENUM('USER', 'ADMIN', 'SUPERADMIN', 'BANNED', name='userrole')
    userrole.drop(op.get_bind(), checkfirst=True)
