from pydantic import BaseModel

class ReturnBook(BaseModel):

    member_email: str
    book_isbn: str