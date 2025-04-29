from app.schemas.type_schema import TypeDTO
from app.models.type_model import Type


class TypeDTOMapper:
    @staticmethod
    def to_dto(type_model: Type) -> TypeDTO:
        return TypeDTO(
            name=type_model.name,
            thumbnail=type_model.thumbnail,
            embedUrl=type_model.embedUrl,
        )

    @staticmethod
    def to_model(dto: TypeDTO) -> Type:
        return Type(
            name=dto.name,
            thumbnail=dto.thumbnail,
            embedUrl=dto.embedUrl,
        )
