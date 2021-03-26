from app.db.repositories.base import BaseRepository
from app.db.queries.queries import queries
from app.db.errors import EntityAlreadyExist
import asyncpg


class FilesRepository(BaseRepository):
    async def create_file(self, *, user_name: str, file_path: str):
        try:
            async with self.connection.transaction():
                await queries.create_file(
                    self.connection,
                    user_name=user_name,
                    file_path=file_path,
                )
        except asyncpg.exceptions.UniqueViolationError:
            raise EntityAlreadyExist('file exists')
