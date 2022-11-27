from src.connectors.gutendex_connector import GutendexConnector
from src.crud.reviews_crud import ReviewsManager

def test_gutendex_api():
    '''Test if the gutendex API is working'''

    result = GutendexConnector().get_book_by_id(84)

    assert result.title 

def test_postgres_connection():
    '''Check the postgres connection'''

    result = ReviewsManager().get_all()

    assert len(result) >= 0
