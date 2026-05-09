from datetime import datetime
from app.audit.audit_service import create_log
from app.database import db

def return_book_service(data):

    record = db.borrow_records.find_one(
        {
            "member_email": data["member_email"],
            "book_isbn": data["book_isbn"],
            "status": "BORROWED"
        }
    )

    if not record:

        return {
            "error": "Borrow record not found"
        }

    db.borrow_records.update_one(
        {"_id": record["_id"]},
        {
            "$set": {
                "status": "RETURNED",
                "return_date": str(datetime.now())
            }
        }
    )

    db.books.update_one(
        {"isbn": data["book_isbn"]},
        {
            "$inc": {"quantity": 1}
        }
    )

    create_log(
    "BOOK_RETURNED",
    data["member_email"]
) 
    return {
        "message": "Book Returned Successfully"
    }