from pathlib import Path
from uuid import uuid4
from shutil import copyfileobj
from fastapi import APIRouter, Depends, HTTPException, status, UploadFile
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.file import GetUserFilesRes, UploadFileRes
from app.services.file import get_user_files_ser, upload_file_service
from app.services.user import update_user_profile_image

router = APIRouter(prefix="/files", tags=["Files"])

FILE_CATEGORY_PATHS = {
    "profile_image": "user/profile-images",
    "expense_receipt": "expenses/receipts",
}

STORAGE_ROOT = Path("storage")


@router.post(
    "",
    summary="Upload file",
    description="Upload a file to the server and return file information.",
)
def upload_file_test(file: UploadFile):
    return {"filename": file.filename, "content_type": file.content_type}


@router.post(
    "/upload", response_model=UploadFileRes, status_code=status.HTTP_201_CREATED
)
def upload_file(
    file: UploadFile,
    file_category: str,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    file_extension = Path(file.filename).suffix

    generated_file_name = f"{uuid4()}{file_extension}"

    relative_dir = FILE_CATEGORY_PATHS.get(file_category)

    if not relative_dir:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file category",
        )

    module_dir = STORAGE_ROOT / relative_dir

    module_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    file_extension = Path(file.filename).suffix
    generated_file_name = f"{uuid4()}{file_extension}"

    file_path = module_dir / generated_file_name

    with file_path.open("wb") as buffer:
        copyfileobj(file.file, buffer)

    file_size = file_path.stat().st_size
    relative_path = file_path.relative_to(STORAGE_ROOT)

    result = upload_file_service(
        db,
        {
            "filename": file.filename,
            "generated_file_name": generated_file_name,
            "file_path": str(relative_path),
            "content_type": file.content_type,
            "file_size": file_size,
            "file_category": file_category,
            "status": "active",
            "user_id": current_user.id,
        },
    )

    # Update profile id to user
    update_user = update_user_profile_image(
        db, {"user_id": result.user_id, "profile_image_id": result.id}
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


@router.get("/get_all", response_model=GetUserFilesRes, status_code=status.HTTP_200_OK)
def get_user_files(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    result = get_user_files_ser(db, {"user_id": current_user.id})
    return {"message": "Fetched user files successfully", "data": result}
