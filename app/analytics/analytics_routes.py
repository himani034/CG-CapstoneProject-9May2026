from fastapi import APIRouter

from app.analytics.analytics_service import (
    total_books_service,
    total_members_service,
    total_borrowed_books_service,
    low_stock_books_service,
    most_borrowed_books_service
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/total-books")
def total_books():

    return total_books_service()


@router.get("/total-members")
def total_members():

    return total_members_service()


@router.get("/borrowed-books")
def borrowed_books():

    return total_borrowed_books_service()


@router.get("/low-stock")
def low_stock_books():

    return low_stock_books_service()


@router.get("/most-borrowed")
def most_borrowed_books():

    return most_borrowed_books_service()