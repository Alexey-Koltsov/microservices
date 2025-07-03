"""add category data

Revision ID: 26c3d9d03513
Revises: 0111a3e4eefe
Create Date: 2025-06-23 02:21:42.553890

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


revision: str = '26c3d9d03513'
down_revision: Union[str, None] = '0111a3e4eefe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


category_data = [
    {'id': 1, 'name': 'овощи'},
    {'id': 2, 'name': 'фрукты'}
]


def upgrade():
    category_table = sa.Table('category', sa.MetaData(),
                              autoload_with=op.get_bind())
    op.bulk_insert(category_table, category_data)


def downgrade():
    op.execute("DELETE FROM category WHERE id IN (1, 2)")
