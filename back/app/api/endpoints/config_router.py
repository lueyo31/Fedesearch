from fastapi import APIRouter, Depends
from app.schemas.user_config_schema import UserConfigDTO
from app.services.usecases.update_config_use_case import UpdateConfigUseCase
from app.common.ioc import get_update_config_use_case

router = APIRouter()

@router.patch(
    "",
    summary="Update configuration",
    description="Endpoint to update the configuration settings of the application.",
    response_description="A message confirming the configuration update.",
    response_model=dict,
    response_model_exclude_unset=True,
)
async def config(
    config: UserConfigDTO,
    use_case: UpdateConfigUseCase = Depends(get_update_config_use_case),
):

    config_data = config.dict(exclude_unset=True)
    print("Received configuration update:", config_data) 
    use_case.exec(config)
    return {"message": "Configuration updated successfully"}