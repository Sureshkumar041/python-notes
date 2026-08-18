from datetime import datetime
from sqlalchemy import text, DateTime, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.file import File


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str]
    last_name: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password_hash: Mapped[str]
    status: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=text("TIMEZONE('utc', NOW())")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("TIMEZONE('utc', NOW())"),
        onupdate=text("TIMEZONE('utc', NOW())"),
    )
    profile_image_id: Mapped[int | None] = mapped_column(
        ForeignKey("files.id"), nullable=True
    )
    profile_image: Mapped["File | None"] = relationship(
        "File",
        foreign_keys=[profile_image_id],
        uselist=False,
    )
