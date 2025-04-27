"""remove date from reviews

Revision ID: a6823939e30e
Revises: 6fefe246f0f1
Create Date: 2025-04-27 22:26:19.797168

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a6823939e30e'
down_revision: Union[str, None] = '6fefe246f0f1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column('reviews', 'date')

def downgrade() -> None:
    op.add_column('reviews', sa.Column('date', sa.DateTime(), nullable=True))