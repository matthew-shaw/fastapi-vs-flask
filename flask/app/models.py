from datetime import datetime, timezone

import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Thing(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    quantity: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    created_at: so.Mapped[datetime] = so.mapped_column(
        sa.DateTime,
        index=True,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at: so.Mapped[datetime] = so.mapped_column(sa.DateTime, index=True, nullable=True)
