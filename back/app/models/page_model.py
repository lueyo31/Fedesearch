from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from app.models.result_model import Result


class Page(BaseModel):
    page: int  # Page number
    results: List[Result]  # List of results
    totalResults: int  # Total number of results
    nsfw: bool  # Boolean map of safesearch
