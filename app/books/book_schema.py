from pydantic import BaseModel

class BookCreate(BaseModel):

    title: str
    author: str
    isbn: str
    category: str
    quantity: int