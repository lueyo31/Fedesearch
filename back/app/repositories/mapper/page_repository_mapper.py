from app.models.page_model import Page
from app.repositories.mapper.result_repository_mapper import ResultXNGMapper
from app.schemas.params_schema import QueryParamsDTO
from app.common.config import SEARCH_API_URL, API_VERSION, SELF_HOST


class PageXNGMapper:
    @staticmethod
    def map_searx_page(searx_data: dict, params: QueryParamsDTO) -> Page:
        print("Mapping page with data:", searx_data)
        results = [
            result
            for index, item in enumerate(searx_data.get("results", []), start=1)
            if (result := ResultXNGMapper.map_searx_result(item, params, index))
            is not None
        ]
        return Page(
            page=searx_data.get("pagination", {}).get("current", 1),
            results=results,
            totalResults=len(results),
            nsfw=not params.safesearch,
        )
