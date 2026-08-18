from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field


class CreateUser(BaseModel):
    first_name: str = Field(min_length=3)
    last_name: str = Field(min_length=3)
    email: str
    password: str = Field(min_length=6)
    status: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserDetailRes(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    status: str
    created_at: datetime


class UserLoginObj(BaseModel):
    token: str
    user_detail: UserDetailRes


class UserLoginRes(BaseModel):
    message: str
    data: UserLoginObj


class CreateUserObjRes(BaseModel):
    user_detail: UserDetailRes


class CreateUserRes(BaseModel):
    message: str
    data: CreateUserObjRes


class GetUserList(BaseModel):
    limit: int = 10
    status: str | None


class GetUserDetailRes(BaseModel):
    message: str
    data: UserDetailRes


class UserListObj(BaseModel):
    list: list[UserDetailRes]
    total: int | None
    page: int | None
    limit: int | None


class GetUserListRes(BaseModel):
    message: str
    data: UserListObj


class UpdateUser(CreateUser):
    id: int


class UpdateUserRes(BaseModel):
    message: str


class DeleteUser(BaseModel):
    id: int
    status: str


model_config = ConfigDict(from_attributes=True)

"""
Pydantic normally expects dictionary-style data.

from_attributes=True tells Pydantic:

"You can read values directly from an object's attributes."
"""

# 🏏 Next ball — User Service
