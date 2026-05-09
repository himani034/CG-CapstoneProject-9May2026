from fastapi import APIRouter

from app.borrow.return_schema import ReturnBook

from app.borrow.return_service import return_book_service


router = APIRouter(
    prefix="/return",
    tags=["Return"]
)


@router.post("/")
def return_book(data: ReturnBook):

    return return_book_service(
        data.dict()
    )