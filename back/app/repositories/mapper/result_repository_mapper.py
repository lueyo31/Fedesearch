from datetime import datetime
from uuid import uuid4
from urllib.parse import urlparse
from app.models.result_model import Result
from app.models.type_model import Type
from app.schemas.params_schema import QueryParamsDTO


class ResultXNGMapper:
    @staticmethod
    def map_searx_result(item: dict, params: QueryParamsDTO, index: int) -> Result:
        print(f"Mapping result {index} with item:", item)
        try:
            # Handle missing or invalid publishedDate
            published_date = item.get("publishedDate")
            date = (
                datetime.fromisoformat(published_date)
                if published_date
                else datetime.now()
            )

            type_data = Type(
                name=(
                    params.category
                    if params.category == "web"
                    else params.category[:-1]
                ),
                thumbnail=(
                    item.get("thumbnail")
                    if params.category != "web" or item.get("thumbnail")
                    else None
                ),
                embedUrl=(
                    item.get("iframe_src") if params.category == "videos" else None
                ),
            )
            print(f"Type data mapped: {type_data}")
            result = Result(
                id=str(uuid4()),
                title=item["title"],
                description=item.get("content", ""),
                link=item["url"],
                linkPage=f"{urlparse(item['url']).scheme}://{urlparse(item['url']).netloc}",
                type=type_data,
                score=item.get("score", 0.0),
                position=index,
                page=params.page,
                date=date,
                motor=item.get("engine", "searx"),
            )
            print(f"Result mapped: {result}")
            return result
        except KeyError as e:
            print(f"Skipping result {index} due to missing required field: {e}")
            return None
        except ValueError as e:
            print(f"Skipping result {index} due to validation error: {e}")
            return None
