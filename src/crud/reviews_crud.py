from src.connectors.postgres_connector import BasicCrud
from src.models.reviews import Reviews

class ReviewsManager(BasicCrud):

    def __init__(self):
        super().__init__(Reviews)