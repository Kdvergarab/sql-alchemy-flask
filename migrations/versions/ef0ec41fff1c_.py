"""empty message

Revision ID: ef0ec41fff1c
Revises: 15791a4b1d49
Create Date: 2022-04-20 00:06:04.704214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef0ec41fff1c'
down_revision = '15791a4b1d49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('people',
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('height', sa.Integer(), nullable=False),
    sa.Column('mass', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('uid'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('people')
    # ### end Alembic commands ###
