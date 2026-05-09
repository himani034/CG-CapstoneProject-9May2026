from fastapi import FastAPI

from app.books.book_routes import (
    router as book_router
)

from app.members.member_routes import (
    router as member_router
)

from app.borrow.borrow_routes import (
    router as borrow_router
)

from app.borrow.return_routes import (
    router as return_router
)
from app.inventory.inventory_routes import (
    router as inventory_router
)
from app.uploads.upload_routes import (
    router as upload_router
)
from app.analytics.analytics_routes import (
    router as analytics_router
)
# from app.auth.auth_routes import (
#     router as auth_router
# )

app = FastAPI(
    title="LibTrack API Platform"
)

# Books Module
app.include_router(book_router)

# Members Module
app.include_router(member_router)

# Borrow Module
app.include_router(borrow_router)

# Return Module
app.include_router(return_router)

app.include_router(inventory_router)

app.include_router(upload_router)

# app.include_router(auth_router)

app.include_router(analytics_router)


@app.get("/")
def home():

    return {
        "message": "LibTrack API Running Successfully"
    }