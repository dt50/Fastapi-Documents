from databases import DatabaseURL
from pathlib import Path


DATABASE_URL: DatabaseURL = DatabaseURL('postgres://postgres:postgres@localhost:5432/postgres')

BASE_DIR = Path(__file__).resolve().parent.parent
FILE_DIR = BASE_DIR / "files"
