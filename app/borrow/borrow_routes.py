from fastapi import APIRouter

from app.borrow.borrow_schema import BorrowBook

from app.borrow.borrow_service import (
    borrow_book_service
)

router = APIRouter(
    prefix="/borrow",
    tags=["Borrow"]
)

@router.post("/")
def borrow_book(data: BorrowBook):

    return borrow_book_service(
        data.dict()
    )