"""creat first table

Revision ID: f736e2c8064e
Revises: 
Create Date: 2023-10-09 14:43:14.406406

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
    

# revision identifiers, used by Alembic.
revision: str = 'f736e2c8064e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # op.create_table\
    # ("posts",
    # sa.Column("id",sa.Integer(),nullable= False , primary_key=True),
    # sa.Column("titile",sa.String())
    # )
    pass


def downgrade() -> None:
    # op.drop_table("posts")
    pass
