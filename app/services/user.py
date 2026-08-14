from sqlalchemy.orm import Session
from sqlalchemy import func, select, update

from app.models.user import User
from app.schemas.user import CreateUser, DeleteUser, GetUserList, UpdateUser

from fastapi import HTTPException, status


def create_user_service(db: Session, payload: CreateUser):
    user = User(
        first_name=payload.first_name,
        last_name=payload.last_name,
        status=payload.status,
    )

    # SQLAlchemy, I want to insert this
    # Still not permanently saved.
    db.add(user)

    # This is where the transaction is committed to PostgreSQL.
    db.commit()

    # This is important because PostgreSQL generated values such as:
    # id
    # created_at
    db.refresh(user)

    return user


def get_user_profile_ser(db: Session, user_id):
    result = db.execute(select(User).where(User.id == user_id))

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User detail with id {user_id} not found",
        )

    return user


def get_user_list_ser(db: Session, page: int, limit: int, status: str | None = None):
    off_set = (page - 1) * limit
    # base query
    query = select(User)

    if status:
        query = query.where(User.status == status)

    # total count
    count_query = select(func.count()).select_from(query.subquery())

    total_count = db.scalar(count_query)

    # pagination
    if page and limit:
        query = query.offset(off_set).limit(limit)

    result = db.execute(query)

    users = result.scalars().all()

    return {"list": users, "total": total_count, "page": page, "limit": limit}


def update_user_ser(db: Session, payload: UpdateUser):
    user_id = payload.id
    result = db.execute(select(User).where(User.id == user_id))

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User detail with id {user_id} not found",
        )

    stmt = (
        update(User)
        .where(User.id == user_id)
        .values(
            {
                "first_name": payload.first_name,
                "last_name": payload.last_name,
                "status": payload.status,
            }
        )
    )

    db.execute(stmt)
    db.commit()
    return True


def update_user_status_ser(db: Session, payload: DeleteUser):
    user_id = payload.id
    result = db.execute(select(User).where(User.id == user_id))

    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User detail with id {user_id} not found",
        )

    stmt = (
        update(User)
        .where(User.id == user_id)
        .values(
            {
                "status": payload.status,
            }
        )
    )

    db.execute(stmt)
    db.commit()
    return True
