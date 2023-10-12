"""add column to posts table

Revision ID: cbfaa7309765
Revises: 22c7705a9b0f
Create Date: 2023-10-09 16:21:48.992689

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cbfaa7309765'
down_revision: Union[str, None] = '22c7705a9b0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None



def upgrade() -> None:
    # op.add_column\
    # ("posts",
    #   sa.Column("time_Created",sa.DateTime(),server_default="now()")
    # )
    #add constraint to posts
    pass
    
    


def downgrade() -> None:
    # op.drop_column("posts","time_Created")
    pass
