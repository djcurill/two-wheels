"""empty message

Revision ID: f06737b1ecbc
Revises: e730f3c1cc5b
Create Date: 2022-01-16 09:58:00.297930

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f06737b1ecbc'
down_revision = 'e730f3c1cc5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('frame_size',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('value', sa.String(length=5), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('value')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('frame_size')
    # ### end Alembic commands ###
