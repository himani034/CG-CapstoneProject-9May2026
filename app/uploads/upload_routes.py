from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.uploads.upload_service import (
    upload_books_service
)

router = APIRouter(
    prefix="/upload",
    tags=["CSV Upload"]
)

@router.post("/")
def upload_books(
    file: UploadFile = File(...)
):

    return upload_books_service(file)