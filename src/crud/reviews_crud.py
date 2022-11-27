from src.connectors.postgres_connector import BasicCrud
from src.models.reviews import Reviews
from typing import List
from src.schemas.gutendex_model import GutendexModel
from sqlalchemy.sql import func

class ReviewsManager(BasicCrud):

    def __init__(self):
        super().__init__(Reviews)

    def get_by_book_id(self, book_id: int) -> GutendexModel:
        return self.db.query(
            self.model
        ).filter(
            self.model.bookId == book_id
        ).all()

    def get_average_rating(self, book_id: int) -> int:
        return self.db.query(
            func.avg(self.model.rating)
        ).filter(
            self.model.bookId == book_id
        ).first()[0]