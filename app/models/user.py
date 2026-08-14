from datetime import datetime
from sqlalchemy import text, DateTime
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=text("TIMEZONE('utc', NOW())")
    )
