import requests
from src.schemas.gutendex_model import GutendexModel, GutendexDetails
from pydantic import parse_obj_as
from typing import List

class GutendexConnector:

    def __init__(self) -> None:
        self.base_url = "https://gutendex.com"

    def get_books_by_name(
        self,
        book_title: str
        ) -> List[GutendexModel]:
        '''Search a book by name'''

        url = self.base_url + "/books"
        params = {
            "search": book_title
        }

        response = requests.get(url,params=params)

        if response.status_code == 200:
            books = response.json()['results']
            return parse_obj_as(List[GutendexModel],books)

        else:
            raise Exception("Error consulting Gutendex API")

    def get_book_by_id(
        self,
        book_id: int
        ) -> GutendexDetails:
        '''Search a book by ID'''

        url = self.base_url + "/books"
        params = {
            "ids": book_id
        }

        response = requests.get(url,params=params)

        if response.status_code == 200:
            books = response.json()['results']
            return parse_obj_as(GutendexDetails,books[0])

        else:
            raise Exception("Error consulting Gutendex API")


