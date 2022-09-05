"""create_recipes_table

Revision ID: a555a99c3854
Revises: 
Create Date: 2022-08-31 17:51:17.169614

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a555a99c3854'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('recipes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('favourite_amount', sa.Integer(), nullable=False),
    sa.Column('preparation_time', sa.Integer(), nullable=False),
    sa.Column('cover', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recipes')
    # ### end Alembic commands ###
