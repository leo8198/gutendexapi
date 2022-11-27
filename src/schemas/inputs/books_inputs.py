from pydantic import BaseModel

class ReviewBook(BaseModel):
    bookId: int 
    rating: int
    description: str