# from app.database import db

# def add_book_service(book_data):

#     db.books.insert_one(book_data)

#     return {"message": "Book Added Successfully"}

# def get_books_service():

#     books = list(
#         db.books.find({}, {"_id": 0})
#     )

#     return books

# def get_single_book_service(isbn):

#     book = db.books.find_one(
#         {"isbn": isbn},
#         {"_id": 0}
#     )

#     return book

# def update_book_service(isbn, updated_data):

#     db.books.update_one(
#         {"isbn": isbn},
#         {"$set": updated_data}
#     )

#     return {"message": "Book Updated Successfully"}

# def delete_book_service(isbn):

#     db.books.delete_one(
#         {"isbn": isbn}
#     )

#     return {"message": "Book Deleted Successfully"}



from app.database import db
from app.audit.audit_service import create_log

def add_book_service(book_data):

    existing_book = db.books.find_one(
        {"isbn": book_data["isbn"]}
    )

    if existing_book:

        return {
            "error": "Book with this ISBN already exists"
        }

    db.books.insert_one(book_data)
    create_log(
    "BOOK_ADDED",
    "ADMIN"
)

    return {
        "message": "Book Added Successfully"
    }

def get_books_service():

    books = list(
        db.books.find({}, {"_id": 0})
    )

    return books

def get_single_book_service(isbn):

    book = db.books.find_one(
        {"isbn": isbn},
        {"_id": 0}
    )

    return book

def update_book_service(isbn, updated_data):

    db.books.update_one(
        {"isbn": isbn},
        {"$set": updated_data}
    )

    return {
        "message": "Book Updated Successfully"
    }

def delete_book_service(isbn):

    db.books.delete_one(
        {"isbn": isbn}
    )

    return {
        "message": "Book Deleted Successfully"
    }