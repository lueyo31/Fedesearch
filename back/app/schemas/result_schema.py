from pydantic import BaseModel, HttpUrl
from typing import Literal
from datetime import datetime
from app.schemas.type_schema import TypeDTO


class ResultDTO(BaseModel):
    id: str
    title: str
    description: str
    link: HttpUrl
    linkPage: HttpUrl
    type: TypeDTO
    score: float
    position: int
    page: int
    date: datetime
    motor:str

    @classmethod
    def from_result(cls, result):
        return cls(
            id=result.id,
            title=result.title,
            description=result.description,
            link=result.link,
            linkPage=result.linkPage,
            type=TypeDTO.from_type(result.type),
            score=result.score,
            position=result.position,
            page=result.page,
            date=result.date,
        )
