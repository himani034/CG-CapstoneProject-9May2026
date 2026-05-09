from pydantic import BaseModel

class BorrowBook(BaseModel):

    member_email: str
    book_isbn: str