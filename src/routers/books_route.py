from typing import List
from fastapi import APIRouter
from src.connectors.gutendex_connector import GutendexConnector
from src.schemas.gutendex_model import GutendexModel
from src.schemas.inputs.books_inputs import ReviewBook

# Endpoint to handle the health check
router = APIRouter(
    prefix='/api/v1/books'
)

# Search Book endpoint
@router.get("")
async def search_book_by_title(
    title: str
) -> List[GutendexModel]:

    # Get the book from the Gutendex API
    books = GutendexConnector().get_book_by_name(title)
    
    return {
        "status": "ok",
        "books": books
    }

# Review some book
@router.post("/{book_id}/review")
async def search_book_by_title(
    book_id: int,
    review: ReviewBook
) -> List[GutendexModel]:

    # Save the rating in the database

    return {
        "status": "ok",
        "data": review
    }
