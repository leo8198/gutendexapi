from src.connectors.postgres_connector import BasicCrud
from src.models.reviews import Reviews
from typing import List
from src.schemas.gutendex_model import GutendexModel


class ReviewsManager(BasicCrud):

    def __init__(self):
        super().__init__(Reviews)

    def get_by_book_id(self, book_id: int) -> GutendexModel:
        return self.db.query(
            self.model
        ).filter(
            self.model.bookId == book_id
        ).all()