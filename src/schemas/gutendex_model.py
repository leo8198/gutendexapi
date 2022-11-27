from pydantic import BaseModel
from typing import List, Optional

class GutendexAuthorModel(BaseModel):
    name: str 
    birth_year: Optional[int] 
    death_year: Optional[int]

class GutendexModel(BaseModel):
    id: int 
    title: str 
    authors: List[GutendexAuthorModel]
    languages: List[str]
    download_count: int

class GutendexDetails(GutendexModel):
    rating: Optional[float]
    reviews: Optional[List[str]]