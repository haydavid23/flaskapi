"""empty message

Revision ID: 48652df030d3
Revises: 9267002731f6
Create Date: 2019-05-24 14:47:04.299050

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '48652df030d3'
down_revision = '9267002731f6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('cart_id', sa.String(length=80), nullable=False),
    sa.Column('product_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=False),
    sa.Column('price', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cart_id'], ['cart.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['quantity'], ['person.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cart_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('cart_item')
    # ### end Alembic commands ###