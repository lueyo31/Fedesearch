from app.schemas.page_schema import PageDTO
from app.models.page_model import Page
from app.api.mapper.result_dto_mapper import ResultDTOMapper


class PageDTOMapper:
    @staticmethod
    def to_dto(page: Page) -> PageDTO:
        return PageDTO(
            page=page.page,
            results=[ResultDTOMapper.to_dto(result) for result in page.results],
            totalResults=page.totalResults,
            nsfw=page.nsfw,
        )

    @staticmethod
    def to_model(dto: PageDTO) -> Page:
        return Page(
            page=dto.page,
            results=[ResultDTOMapper.to_model(result) for result in dto.results],
            totalResults=dto.totalResults,
            nsfw=dto.nsfw,
        )
