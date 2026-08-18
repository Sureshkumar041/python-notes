from pathlib import Path
from sqlalchemy.orm import Session
from sqlalchemy import and_, func, select
from fastapi import Depends, File, HTTPException, status, UploadFile

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


def get_file_by_id_ser(db: Session, file_id: int, user_id: int):

    query_builder = select(FileModel).where(
        and_(FileModel.user_id == user_id, FileModel.id == file_id)
    )

    result = db.execute(query_builder).scalar_one_or_none()

    if not result:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"File with id {file_id} not found",
        )

    return result


def get_file_download_ser(db: Session, file_id: int, user_id: int):

    file_detail = get_file_by_id_ser(db, file_id, user_id)

    file_path = Path(file_detail.path)

    if not file_path.exists():
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Physical file not found",
        )

    return file_detail
