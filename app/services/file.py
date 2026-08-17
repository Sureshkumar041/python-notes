from sqlalchemy.orm import Session
from fastapi import Depends, File, UploadFile

from app.db.database import get_db
from app.models.file import File as FileModel


def upload_file_service(db: Session, file: UploadFile):
    return True
    