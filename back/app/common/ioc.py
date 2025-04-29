from fastapi import Depends
from app.repositories.xng_repository import XngRepository, IXngRepository
from app.services.page_service import PageService, IPageService
from app.services.usecases.web_search_use_case import WebSearchUseCase, IWebSearchUseCase
from app.services.usecases.full_search_use_case import FullSearchUseCase, IFullSearchUseCase
from app.services.config_service import ConfigService  # Added import
from app.services.usecases.update_config_use_case import UpdateConfigUseCase  # Added import

# Singleton instances
_xng_repository_instance = None
_page_service_instance = None
_web_search_use_case_instance = None
_full_search_use_case_instance = None
_config_service_instance = None  # Added for ConfigService
_update_config_use_case_instance = None  # Added for UpdateConfigUseCase

def get_xng_repository() -> IXngRepository:
    global _xng_repository_instance
    if _xng_repository_instance is None:
        _xng_repository_instance = XngRepository()
    return _xng_repository_instance

def get_page_service(repository: IXngRepository = Depends(get_xng_repository)) -> IPageService:
    global _page_service_instance
    if _page_service_instance is None:
        _page_service_instance = PageService(repository)
    return _page_service_instance

def get_web_search_use_case(service: IPageService = Depends(get_page_service)) -> IWebSearchUseCase:
    global _web_search_use_case_instance
    if _web_search_use_case_instance is None:
        _web_search_use_case_instance = WebSearchUseCase(service)
    return _web_search_use_case_instance

def get_full_search_use_case(service: IPageService = Depends(get_page_service)) -> IFullSearchUseCase:
    global _full_search_use_case_instance
    if _full_search_use_case_instance is None:
        _full_search_use_case_instance = FullSearchUseCase(service)
    return _full_search_use_case_instance

def get_config_service() -> ConfigService:  # Added function
    global _config_service_instance
    if _config_service_instance is None:
        _config_service_instance = ConfigService()
    return _config_service_instance

def get_update_config_use_case(service: ConfigService = Depends(get_config_service)) -> UpdateConfigUseCase:  # Added function
    global _update_config_use_case_instance
    if _update_config_use_case_instance is None:
        _update_config_use_case_instance = UpdateConfigUseCase(service)
    return _update_config_use_case_instance