from datetime import datetime
from enum import Enum
from sqlalchemy import text, DateTime, ForeignKey
from app.db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class FileStatus(str, Enum):
    ACTIVE = "active"
    DELETED = "deleted"


class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    # profile_image / document / etc.
    file_category: Mapped[str]
    original_file_name: Mapped[str]
    file_name: Mapped[str]
    path: Mapped[str]
    mime_type: Mapped[str]
    # bytes
    file_size: Mapped[int]
    status: Mapped[FileStatus]
    created_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=text("TIMEZONE('utc', NOW())")
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=text("TIMEZONE('utc', NOW())"),
        onupdate=text("TIMEZONE('utc', NOW())"),
    )
