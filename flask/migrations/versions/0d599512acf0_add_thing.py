"""add thing

Revision ID: 0d599512acf0
Revises:
Create Date: 2024-07-25 14:25:48.708940

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0d599512acf0"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "thing",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.String(length=64), nullable=False),
        sa.Column(
            "colour",
            sa.Enum(
                "RED",
                "GREEN",
                "BLUE",
                "YELLOW",
                "ORANGE",
                "PURPLE",
                "BLACK",
                "WHITE",
                name="colours",
            ),
            nullable=False,
        ),
        sa.Column("quantity", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    with op.batch_alter_table("thing", schema=None) as batch_op:
        batch_op.create_index(
            batch_op.f("ix_thing_colour"),
            ["colour"],
            unique=False,
        )
        batch_op.create_index(
            batch_op.f("ix_thing_created_at"),
            ["created_at"],
            unique=False,
        )
        batch_op.create_index(
            batch_op.f("ix_thing_name"),
            ["name"],
            unique=True,
        )
        batch_op.create_index(
            batch_op.f("ix_thing_quantity"),
            ["quantity"],
            unique=False,
        )
        batch_op.create_index(
            batch_op.f("ix_thing_updated_at"),
            ["updated_at"],
            unique=False,
        )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("thing", schema=None) as batch_op:
        batch_op.drop_index(batch_op.f("ix_thing_updated_at"))
        batch_op.drop_index(batch_op.f("ix_thing_quantity"))
        batch_op.drop_index(batch_op.f("ix_thing_name"))
        batch_op.drop_index(batch_op.f("ix_thing_created_at"))
        batch_op.drop_index(batch_op.f("ix_thing_colour"))

    op.drop_table("thing")
    # ### end Alembic commands ###