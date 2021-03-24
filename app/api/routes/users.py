from fastapi import APIRouter, Depends, HTTPException, status

from app.api.dependencies.database import get_repository
from app.models.schemas.users import UserIn, UserOut, UserReg
from app.db.repositories.users import UsersRepository
from app.db.errors import SimplePassword, EntityAlreadyExist
router = APIRouter()


@router.post("/create-user/", response_model=UserOut, name="users:create-user")
async def create_user(
        user: UserReg,
        users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> UserOut:
    try:
        users_row = await users_repo.create_user(
            user_name=user.user_name,
            full_name=user.full_name,
            email=user.email,
            password=user.password
        )
    except (SimplePassword, EntityAlreadyExist) as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
    return users_row


@router.post("/get-user/", response_model=UserOut, name="users:get-user")
async def get_user(
        user: UserIn,
        users_repo: UsersRepository = Depends(get_repository(UsersRepository))
) -> UserOut:
    users_row = await users_repo.get_user(
        user_name=user.user_name,
        password=user.password
    )
    return users_row
