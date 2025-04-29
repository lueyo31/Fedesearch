from pydantic import BaseModel, HttpUrl
from typing import List, Optional
from app.schemas.result_schema import ResultDTO


class PageDTO(BaseModel):
    page: int
    results: List[ResultDTO]
    next: Optional[HttpUrl] = None  # Make optional with a default value of None
    previous: Optional[HttpUrl] = None  # Make optional with a default value of None
    totalResults: int
    nsfw: bool

    @classmethod
    def from_page(cls, page):
        """
        Converts a page object into a PageDTO.
        """
        return cls(
            page=page.page,
            results=[ResultDTO.from_result(result) for result in page.results],
            next=page.next,
            previous=page.previous,
            totalResults=page.totalResults,
            nsfw=page.nsfw,
        )
