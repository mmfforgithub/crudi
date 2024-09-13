"""m

Revision ID: f751516842e8
Revises: 
Create Date: 2024-09-13 16:06:00.408827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f751516842e8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('doacao',
    sa.Column('id_doacao', sa.Integer(), nullable=False),
    sa.Column('doador', sa.String(length=100), nullable=True),
    sa.Column('valor', sa.Float(precision=10, asdecimal=2), nullable=True),
    sa.Column('data', sa.Date(), nullable=True),
    sa.PrimaryKeyConstraint('id_doacao')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('doacao')
    # ### end Alembic commands ###
