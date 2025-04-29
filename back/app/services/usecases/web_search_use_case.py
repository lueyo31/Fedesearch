from abc import ABC, abstractmethod
from app.services.page_service import PageService, IPageService  # Added IPageService
from app.models.page_model import Page
from app.schemas.params_schema import QueryParamsDTO
from app.api.mapper.page_dto_mapper import PageDTOMapper 
from app.schemas.page_schema import PageDTO 

class IWebSearchUseCase(ABC):
    @abstractmethod
    def exec(self, params: QueryParamsDTO) -> PageDTO:
        pass

class WebSearchUseCase(IWebSearchUseCase):
    def __init__(self, service: IPageService):  # Changed to use IPageService
        self.service = service

    def exec(self, params: QueryParamsDTO) -> PageDTO:
        print("WebSearchUseCase.exec called with params:", params.dict())
        page = self.service.search(params)
        print("Page object returned from service in use case:", page)
        return PageDTOMapper.to_dto(page)