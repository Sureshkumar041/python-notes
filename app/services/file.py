from sqlalchemy.orm import Session
from sqlalchemy import func, select
from fastapi import Depends, File, UploadFile

from app.db.database import get_db
from app.models.file import File as FileModel
from app.models.user import User


def upload_file_service(db: Session, file_detail):
    file = FileModel(
        user_id=1,
        file_category="profile_image",
        original_file_name=file_detail["filename"],
        file_name=file_detail["generated_file_name"],
        path=file_detail["file_path"],
        mime_type=file_detail["content_type"],
        file_size=file_detail["file_size"],
        status="active",
    )

    db.add(file)
    db.commit()
    db.refresh(file)

    return file


def get_user_files_ser(db: Session, payload):

    query_builder = select(FileModel).where(FileModel.user_id == payload["user_id"])

    # total count
    count_query = select(func.count()).select_from(query_builder.subquery())
    total_count = db.scalar(count_query)

    result = db.execute(query_builder)

    files = result.scalars().all()

    return {"list": files, "total_count": total_count}
