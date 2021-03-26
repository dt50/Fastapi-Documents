from fastapi import APIRouter, Depends, HTTPException, status,  File, UploadFile
from shutil import copyfileobj
from app.api.dependencies.database import get_repository
from app.core.config import FILE_DIR
from app.db.repositories.files import FilesRepository

router = APIRouter()


@router.post("/uploadfile/")
async def create_upload_file(
        file: UploadFile = File(...),
        files_repo: FilesRepository = Depends(get_repository(FilesRepository))
):
    with open(f'{FILE_DIR / file.filename}', 'wb') as buffer:
        copyfileobj(file.file, buffer)
    await files_repo.create_file(
        user_name='test',
        file_path=str(FILE_DIR / file.filename)
    )
    return {"filename": file.filename}