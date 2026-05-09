from app.database import db


def total_books_service():

    total = db.books.count_documents({})

    return {
        "total_books": total
    }


def total_members_service():

    total = db.members.count_documents({})

    return {
        "total_members": total
    }


def total_borrowed_books_service():

    total = db.borrow_records.count_documents(
        {"status": "BORROWED"}
    )

    return {
        "total_borrowed_books": total
    }


def low_stock_books_service():

    books = list(
        db.books.find(
            {"quantity": {"$lt": 5}},
            {"_id": 0}
        )
    )

    return books


def most_borrowed_books_service():

    pipeline = [
        {
            "$group": {
                "_id": "$book_isbn",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1}
        }
    ]

    result = list(
        db.borrow_records.aggregate(
            pipeline
        )
    )

    return result