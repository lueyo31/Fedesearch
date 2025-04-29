from app.schemas.result_schema import ResultDTO
from app.models.result_model import Result
from app.api.mapper.type_dto_mapper import TypeDTOMapper


class ResultDTOMapper:
    @staticmethod
    def to_dto(result: Result) -> ResultDTO:
        return ResultDTO(
            id=result.id,
            title=result.title,
            description=result.description,
            link=result.link,
            linkPage=result.linkPage,
            type=TypeDTOMapper.to_dto(result.type),
            score=result.score,
            position=result.position,
            page=result.page,
            date=result.date,
            motor=result.motor,
        )

    @staticmethod
    def to_model(dto: ResultDTO) -> Result:
        return Result(
            id=dto.id,
            title=dto.title,
            description=dto.description,
            link=dto.link,
            linkPage=dto.linkPage,
            type=TypeDTOMapper.to_model(dto.type),
            score=dto.score,
            position=dto.position,
            page=dto.page,
            date=dto.date,
            motor=dto.motor,
        )
