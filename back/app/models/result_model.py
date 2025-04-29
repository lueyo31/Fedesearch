from pydantic import BaseModel, HttpUrl
from typing import Literal
from datetime import datetime
from app.models.type_model import Type


class Result(BaseModel):
    id: str  # UUID generated
    title: str  # Map of title
    description: str  # Map of content
    link: HttpUrl  # URL map of url
    linkPage: HttpUrl  # URL to the main page
    type: Type  # Map to the Type model
    score: float  # Double map of score
    position: int  # Position in the results
    page: int  # Page number
    date: datetime  # Date of the result
    motor: str  # Search engine name
