from abc import ABC, abstractmethod
from app.repositories.xng_repository import IXngRepository
from app.models.page_model import Page
from app.schemas.params_schema import QueryParamsDTO


class IPageService(ABC):
    @abstractmethod
    def search(self, params: QueryParamsDTO) -> Page:

        pass
    @abstractmethod
    def full_search(self, params: QueryParamsDTO) -> list[Page]:
        pass


class PageService(IPageService):
    def __init__(self, repository: IXngRepository):
        self.repository = repository

    def search(self, params: QueryParamsDTO) -> Page:
        print("PageService.search called with params:", params.dict())
        if params.category == "images":
            page: Page = self.repository.search_images(params)
        elif params.category == "videos":
            page: Page = self.repository.search_videos(params)
        elif params.category == "news":
            page: Page = self.repository.search_news(params)
        else:
            page: Page = self.repository.search(params)
        page.page = params.page
        return page

    def full_search(self, params: QueryParamsDTO) -> list[Page]:
        print("PageService.full_search called with params:", params.dict())
        all_pages: list[Page] = []
        while True:
            try:
                pages = self.repository.search(params)
                if not pages:
                    break
                all_pages.extend(pages)
                params.page += 1
            except Exception as e:
                print(f"Error during search: {e}")
                break
        return all_pages
