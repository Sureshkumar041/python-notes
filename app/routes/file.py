from pathlib import Path
from uuid import uuid4
from shutil import copyfileobj
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.services.file import upload_file_service

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
def upload_file(
    file: UploadFile,
    file_category: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    file_extension = Path(file.filename).suffix

    generated_file_name = f"{uuid4()}{file_extension}"

    file_path = STORAGE_DIR / generated_file_name

    with file_path.open("wb") as buffer:
        copyfileobj(file.file, buffer)

    file_size = file_path.stat().st_size

    result = upload_file_service(
        db,
        {
            "filename": file.filename,
            "generated_file_name": generated_file_name,
            "file_path": str(file_path),
            "content_type": file.content_type,
            "file_size": file_size,
            "file_category": file_category,
            "status": "active",
            "user_id": current_user.id,
        },
    )

    return {
        "message": f"File uploaded successfully",
        "data": {
            "original_file_name": result.original_file_name,
            "file_name": result.file_name,
            "path": result.path,
            "mime_type": result.mime_type,
            "file_size": result.file_size,
        },
    }
