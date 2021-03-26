from fastapi import APIRouter
from app.api.routes.users import router as users_router
from app.api.routes.files import router as files_router

router = APIRouter()

router.include_router(users_router, tags=['User'], prefix='/users')
router.include_router(files_router, tags=['File'], prefix='/files')
