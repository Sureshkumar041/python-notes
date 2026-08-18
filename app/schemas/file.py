from datetime import datetime
from pydantic import BaseModel


class UpdateUserProfileImage(BaseModel):
    user_id: int
    profile_image_id: int


class FileDetail(BaseModel):
    id: int
    file_name: str
    original_file_name: str
    created_at: datetime
    mime_type: str
    status: str


class FileListObj(BaseModel):
    list: list[FileDetail]
    total_count: int


class GetUserFilesRes(BaseModel):
    message: str
    data: FileListObj


class UploadFileRes(BaseModel):
    message: str
    data: FileDetail
