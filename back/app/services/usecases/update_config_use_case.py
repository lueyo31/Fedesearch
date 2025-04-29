from app.services.config_service import ConfigService
from app.schemas.user_config_schema import UserConfigDTO
from abc import ABC, abstractmethod

class IUpdateConfigUseCase(ABC):
    @abstractmethod
    def exec(self, config: UserConfigDTO):
        pass

class UpdateConfigUseCase(IUpdateConfigUseCase):
    def __init__(self, service: ConfigService):
        self.service = service

    def exec(self, config: UserConfigDTO):
        config_data = config.dict(exclude_unset=True)  
        self.service.update_config(config_data)
