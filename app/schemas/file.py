from pydantic import BaseModel


class UpdateUserProfileImage(BaseModel):
    user_id: int
    profile_image_id: int
