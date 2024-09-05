"""all things

Revision ID: 9180945a3f0f
Revises: 
Create Date: 2024-09-05 14:16:04.519361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9180945a3f0f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('name')
    )
    op.create_table('provinces',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('verified', sa.Boolean(), server_default='False', nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('added_by', sa.Integer(), server_default='1', nullable=False),
    sa.ForeignKeyConstraint(['added_by'], ['admins.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('districts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('province_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['province_id'], ['provinces.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index('idx_district_province_id', 'districts', ['province_id'], unique=False)
    op.create_table('user_itineraries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index('idx_activity_district_id', 'activities', ['district_id'], unique=False)
    op.create_table('attractions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), server_default='0.00', nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index('idx_attraction_district_id', 'attractions', ['district_id'], unique=False)
    op.create_table('hotels_and_restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.Column('cuisine', sa.String(), nullable=True),
    sa.Column('comfort', sa.String(), nullable=True),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('price', sa.Numeric(precision=10, scale=2), server_default='0.00', nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_index('idx_hotels_restaurants_district_id', 'hotels_and_restaurants', ['district_id'], unique=False)
    op.create_table('itineraries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_itinerary_id', sa.Integer(), nullable=False),
    sa.Column('district_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_itinerary_id'], ['user_itineraries.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transportation',
sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('district_id', sa.Integer, nullable=False),
    sa.Column('type', sa.String, nullable=False),
    sa.Column('origin', sa.String, default='Not specified'),
    sa.Column('destination', sa.String, default='Not specified'),
    sa.Column('description', sa.String, default='Not specified'),
    sa.Column('departure', sa.String, default='Not specified'),
    sa.Column('arrival', sa.String, default='Not specified'),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.func.now(), nullable=False),
    sa.ForeignKeyConstraint(['district_id'], ['districts.id'], ondelete='CASCADE')
    )
    op.create_index('idx_transportation_district_id', 'transportation', ['district_id'], unique=False)
    op.create_table('itinerary_activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itinerary_id', sa.Integer(), nullable=False),
    sa.Column('activity_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['activity_id'], ['activities.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['itinerary_id'], ['itineraries.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('itinerary_attractions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itinerary_id', sa.Integer(), nullable=False),
    sa.Column('attraction_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['attraction_id'], ['attractions.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['itinerary_id'], ['itineraries.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('itinerary_hotels_restaurants',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itinerary_id', sa.Integer(), nullable=False),
    sa.Column('hotel_restaurant_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hotel_restaurant_id'], ['hotels_and_restaurants.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['itinerary_id'], ['itineraries.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('itinerary_transportations',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('itinerary_id', sa.Integer(), nullable=False),
    sa.Column('transportation_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['itinerary_id'], ['itineraries.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['transportation_id'], ['transportation.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('itinerary_transportations')
    op.drop_table('itinerary_hotels_restaurants')
    op.drop_table('itinerary_attractions')
    op.drop_table('itinerary_activities')
    op.drop_index('idx_transportation_district_id', table_name='transportation')
    op.drop_table('transportation')
    op.drop_table('itineraries')
    op.drop_index('idx_hotels_restaurants_district_id', table_name='hotels_and_restaurants')
    op.drop_table('hotels_and_restaurants')
    op.drop_index('idx_attraction_district_id', table_name='attractions')
    op.drop_table('attractions')
    op.drop_index('idx_activity_district_id', table_name='activities')
    op.drop_table('activities')
    op.drop_table('user_itineraries')
    op.drop_index('idx_district_province_id', table_name='districts')
    op.drop_table('districts')
    op.drop_table('categories')
    op.drop_table('users')
    op.drop_table('provinces')
    op.drop_table('admins')
    # ### end Alembic commands ###
