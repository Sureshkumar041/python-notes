from fastapi import APIRouter, UploadFile

router = APIRouter(prefix="/files", tags=["Files"])


@router.post("")
def upload_file(file: UploadFile):
    return {"filename": file.filename, "content_type": file.content_type}
