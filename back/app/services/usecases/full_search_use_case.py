from abc import ABC, abstractmethod
from app.services.page_service import PageService
from app.models.page_model import Page
from app.schemas.params_schema import QueryParamsDTO
from app.api.mapper.page_dto_mapper import PageDTOMapper  # Import the mapper
from app.schemas.page_schema import PageDTO  # Import the DTO

class IFullSearchUseCase(ABC):
    @abstractmethod
    def exec(self, params: QueryParamsDTO) -> list[PageDTO]:  # Return list of PageDTO
        pass

class FullSearchUseCase(IFullSearchUseCase):
    def __init__(self, service: PageService):
        self.service = service

    def exec(self, params: QueryParamsDTO) -> list[PageDTO]:  # Return list of PageDTO
        print("FullSearchUseCase.exec called with params:", params.dict())
        pages = self.service.full_search(params)
        return [PageDTOMapper.to_dto(page) for page in pages]  # Map each Page to PageDTO