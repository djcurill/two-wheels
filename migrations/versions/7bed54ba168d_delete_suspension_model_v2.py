"""delete suspension model v2

Revision ID: 7bed54ba168d
Revises: ff84ec9f85ae
Create Date: 2022-01-24 15:24:39.451547

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7bed54ba168d'
down_revision = 'ff84ec9f85ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('model')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type', postgresql.ENUM('REAR', 'FRONT', name='suspensiontype'), autoincrement=False, nullable=True),
    sa.Column('value', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='model_pkey')
    )
    # ### end Alembic commands ###