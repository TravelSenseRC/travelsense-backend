"""price column type changes

Revision ID: 65590d6f9ccd
Revises: 4a7172864e2f
Create Date: 2024-09-04 22:28:14.648123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '65590d6f9ccd'
down_revision: Union[str, None] = '4a7172864e2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('attractions', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=10, scale=2),
               nullable=False,
               existing_server_default=sa.text('0'))
    op.alter_column('hotels_and_restaurants', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Numeric(precision=10, scale=2),
               nullable=False,
               existing_server_default=sa.text('0'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('hotels_and_restaurants', 'price',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    op.alter_column('attractions', 'price',
               existing_type=sa.Numeric(precision=10, scale=2),
               type_=sa.INTEGER(),
               nullable=True,
               existing_server_default=sa.text('0'))
    # ### end Alembic commands ###
