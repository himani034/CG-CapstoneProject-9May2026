import pandas as pd

from app.database import db
from app.audit.audit_service import create_log

def upload_books_service(file):

    df = pd.read_csv(file.file)

    books = df.to_dict(
        orient="records"
    )

    db.books.insert_many(books)
    create_log(
    "CSV_UPLOADED",
    "ADMIN"
)

    return {
        "message": "CSV Uploaded Successfully"
    }