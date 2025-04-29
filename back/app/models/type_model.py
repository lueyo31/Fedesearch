from pydantic import BaseModel, HttpUrl
from typing import Literal, Optional


class Type(BaseModel):
    name: Literal[
        "web", "image", "video", "new"
    ]  # Corresponds to the "name" field in Type
    thumbnail: Optional[HttpUrl] = None  # Optional, only for image, video, new
    embedUrl: Optional[HttpUrl] = None  # Optional, only for video
