from fastapi import APIRouter

from app.books.book_schema import BookCreate
from app.books.book_service import add_book_service, get_books_service, get_single_book_service, update_book_service, delete_book_service

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.post("/")
def add_book(book: BookCreate):

    result = add_book_service(book.dict())

    return result

@router.get("/")
def get_books():

    return get_books_service()

@router.get("/{isbn}")
def get_single_book(isbn: str):

    return get_single_book_service(isbn)

@router.put("/{isbn}")
def update_book(isbn: str, book: BookCreate):

    return update_book_service(
        isbn,
        book.dict()
    )

@router.delete("/{isbn}")
def delete_book(isbn: str):

    return delete_book_service(isbn)