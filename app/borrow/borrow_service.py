from datetime import datetime
from app.audit.audit_service import create_log

from app.database import db

def borrow_book_service(data):

    member = db.members.find_one(
        {"email": data["member_email"]}
    )

    if not member:

        return {
            "error": "Member not found"
        }

    book = db.books.find_one(
        {"isbn": data["book_isbn"]}
    )

    if not book:

        return {
            "error": "Book not found"
        }

    if book["quantity"] <= 0:

        return {
            "error": "Book out of stock"
        }

    db.books.update_one(
        {"isbn": data["book_isbn"]},
        {
            "$inc": {"quantity": -1}
        }
    )

    borrow_record = {
        "member_email": data["member_email"],
        "book_isbn": data["book_isbn"],
        "borrow_date": str(datetime.now()),
        "status": "BORROWED"
    }

    db.borrow_records.insert_one(
        borrow_record
    )
    create_log(
    "BOOK_BORROWED",
    data["member_email"]
)

    return {
        "message": "Book Borrowed Successfully"
    }