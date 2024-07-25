from datetime import datetime, timezone
from enum import StrEnum, auto

import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Colours(StrEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    ORANGE = auto()
    PURPLE = auto()
    BLACK = auto()
    WHITE = auto()


class Thing(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    colour: so.Mapped[str] = so.mapped_column(sa.Enum(Colours), index=True)
    quantity: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime,
        index=True,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: so.Mapped[datetime] = so.mapped_column(sa.DateTime, index=True, nullable=True)
