from pathlib import Path
from uuid import uuid4
from shutil import copyfileobj
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from app.db.database import get_db

router = APIRouter(prefix="/files", tags=["Files"])

STORAGE_DIR = Path("storage/files")
STORAGE_DIR.mkdir(parents=True, exist_ok=True)


@router.post(
    "",
    summary="Upload file",
    description="Upload a file to the server and return file information.",
)
def upload_file_test(file: UploadFile):
    return {"filename": file.filename, "content_type": file.content_type}


@router.post("/upload")
def upload_file(file: UploadFile, db: Session = Depends(get_db)):
    file_extension = Path(file.filename).suffix

    generated_file_name = f"{uuid4()}{file_extension}"

    file_path = STORAGE_DIR / generated_file_name

    with file_path.open("wb") as buffer:
        copyfileobj(file.file, buffer)

    file_size = file_path.stat().st_size

    return {
        "original_file_name": file.filename,
        "file_name": generated_file_name,
        "path": str(file_path),
        "mime_type": file.content_type,
        "file_size": file_size,
    }
