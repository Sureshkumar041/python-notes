from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.schemas.user import (
    CreateUser,
    CreateUserRes,
    DeleteUser,
    GetUserDetailRes,
    GetUserListRes,
    UpdateUser,
    UpdateUserRes,
)
from app.services.user import (
    create_user_service,
    get_user_list_ser,
    get_user_profile_ser,
    update_user_ser,
    update_user_status_ser,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post("", response_model=CreateUserRes, status_code=status.HTTP_201_CREATED)
def create_user(payload: CreateUser, db: Session = Depends(get_db)):
    user = create_user_service(db, payload)
    return {"message": "User created successfully", "data": {"user_detail": user}}


@router.get("/get-all", response_model=GetUserListRes, status_code=status.HTTP_200_OK)
def get_user_list(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1),
    status: str | None = None,
    db: Session = Depends(get_db),
):
    result = get_user_list_ser(db, page, limit, status)
    return {"message": "Fetched user list successfully", "data": result}


@router.get(
    "/{user_id}", response_model=GetUserDetailRes, status_code=status.HTTP_200_OK
)
def get_user_profile(user_id: int, db: Session = Depends(get_db)):
    user = get_user_profile_ser(db, user_id)
    return {"message": "Fetched user profile successfully", "data": user}


@router.put("", response_model=UpdateUserRes, status_code=status.HTTP_200_OK)
def update_user(payload: UpdateUser, db: Session = Depends(get_db)):
    update_user_ser(db, payload)
    return {"message": "Updated user detail successfully"}


@router.put(
    "/update-user-status", response_model=UpdateUserRes, status_code=status.HTTP_200_OK
)
def update_user_status(payload: DeleteUser, db: Session = Depends(get_db)):
    update_user_status_ser(db, payload)
    return {"message": f"Updated user status successfully"}
