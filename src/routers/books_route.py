from typing import List
from fastapi import APIRouter
from src.connectors.gutendex_connector import GutendexConnector
from src.crud.reviews_crud import ReviewsManager
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
async def post_review_book(
    book_id: int,
    review: ReviewBook
):

    # Save the rating in the database
    result =  ReviewsManager().create(review.dict())

    return {
        "status": "ok",
        "data": result
    }


# Get book details
@router.get("/{book_id}")
async def get_book_details(
    book_id: int,
):
    return