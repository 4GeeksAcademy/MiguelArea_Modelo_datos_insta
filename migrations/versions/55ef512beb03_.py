"""empty message

Revision ID: 55ef512beb03
Revises: 1099b4ac6d41
Create Date: 2025-07-05 15:40:38.736656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55ef512beb03'
down_revision = '1099b4ac6d41'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('follower',
    sa.Column('user_from_id', sa.Integer(), nullable=False),
    sa.Column('user_to_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_from_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_to_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_from_id', 'user_to_id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment_text', sa.String(length=255), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(length=20), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(length=10), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('media')
    op.drop_table('comment')
    op.drop_table('follower')
    # ### end Alembic commands ###
