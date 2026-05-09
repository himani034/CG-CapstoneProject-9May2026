from app.database import db

def get_available_books_service():

    books = list(
        db.books.find(
            {"quantity": {"$gt": 0}},
            {"_id": 0}
        )
    )

    return books


def get_out_of_stock_service():

    books = list(
        db.books.find(
            {"quantity": 0},
            {"_id": 0}
        )
    )

    return books


def get_low_stock_service():

    books = list(
        db.books.find(
            {"quantity": {"$lt": 5}},
            {"_id": 0}
        )
    )

    return books