"""add content column

Revision ID: 22c7705a9b0f
Revises: f736e2c8064e
Create Date: 2023-10-09 15:26:11.607221

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '22c7705a9b0f'
down_revision: Union[str, None] = 'f736e2c8064e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.add_column("posts",sa.Column("content",sa.String()))
    pass


def downgrade() -> None:
    # op.drop_column("posts","content")
    pass
