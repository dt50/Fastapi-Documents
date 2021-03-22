from app.db.repositories.base import BaseRepository
from app.db.queries.queries import queries
from app.models.schemas.users import UserOut
from app.db.errors import EntityDoesNotExist, SimplePassword, EntityAlreadyExist
import asyncpg
import re


class UsersRepository(BaseRepository):

    @staticmethod
    def password_validation(password):
        return re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', password)

    async def create_user(self, *, user_name: str, full_name: str, email: str, password: str) -> UserOut:
        if not self.password_validation(password):
            raise SimplePassword('password is too simple')
        try:
            async with self.connection.transaction():
                user_row = await queries.create_user(
                    self.connection,
                    username=user_name,
                    fullname=full_name,
                    email=email,
                    password=password
                )
        except asyncpg.exceptions.UniqueViolationError:
            raise EntityAlreadyExist('user with login={0} already exists'.format(user_name))
        return UserOut(**dict(user_row))

    async def get_user_id(self, *, user_name: str, password: str) -> UserOut:
        user_row = await queries.get_user_id(
            self.connection,
            username=user_name,
            password=password
        )
        if user_row:
            return UserOut(**dict(user_row))

        raise EntityDoesNotExist(
            "user with username {0} does not exist".format(user_name),
        )
