"""empty message

Revision ID: 5a3ef7b3b82c
Revises: 429b14655dba
Create Date: 2014-02-22 20:38:43.097362

"""

# revision identifiers, used by Alembic.
revision = '5a3ef7b3b82c'
down_revision = '429b14655dba'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'password_hash')
    ### end Alembic commands ###
