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
                    user_name=user_name,
                    full_name=full_name,
                    email=email,
                    password=password
                )
        except asyncpg.exceptions.UniqueViolationError:
            raise EntityAlreadyExist('user with login={0} or email={1} already exists'.format(user_name, email))
        return UserOut(**dict(user_row))

    async def get_user(self, *, user_name: str, password: str) -> UserOut:
        user_row = await queries.get_user(
            self.connection,
            user_name=user_name,
            password=password
        )
        print(user_row)
        if user_row:
            return UserOut(**dict(user_row))

        raise EntityDoesNotExist(
            "user with username {0} does not exist".format(user_name),
        )
