"""empty message

Revision ID: fdeafc03e008
Revises: 565b5066ffe5
Create Date: 2019-05-24 18:23:09.856974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fdeafc03e008'
down_revision = '565b5066ffe5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('username', table_name='person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('username', 'person', ['username'], unique=True)
    # ### end Alembic commands ###
