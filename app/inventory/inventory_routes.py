from fastapi import APIRouter

from app.inventory.inventory_service import (
    get_available_books_service,
    get_out_of_stock_service,
    get_low_stock_service
)

router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)

@router.get("/available")
def available_books():

    return get_available_books_service()


@router.get("/out-of-stock")
def out_of_stock_books():

    return get_out_of_stock_service()


@router.get("/low-stock")
def low_stock_books():

    return get_low_stock_service()