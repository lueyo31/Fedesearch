from pydantic import BaseModel, HttpUrl
from typing import Literal, Optional


class TypeDTO(BaseModel):
    name: Literal["web", "image", "video", "new"]
    thumbnail: Optional[HttpUrl] = None
    embedUrl: Optional[HttpUrl] = None

    @classmethod
    def from_type(cls, type_model):
        return cls(
            name=type_model.name,
            thumbnail=type_model.thumbnail,
            embedUrl=type_model.embedUrl,
        )
