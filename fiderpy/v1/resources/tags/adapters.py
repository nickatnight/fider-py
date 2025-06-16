from fiderpy.v1.resources.tags.response import CreateTagResponse, Tag
from fiderpy.v1.utils.interfaces import IAdapter
from fiderpy.v1.utils.types import FiderAPIResponseType


class TagAdapter(IAdapter[FiderAPIResponseType, Tag]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> Tag:
        return Tag(
            id=obj["id"],
            name=obj["name"],
            slug=obj["slug"],
            color=obj["color"],
            is_public=obj["isPublic"],
        )


class CreateTagResponseAdapter(IAdapter[FiderAPIResponseType, CreateTagResponse]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> CreateTagResponse:
        return CreateTagResponse(
            id=obj["id"],
            name=obj["name"],
            slug=obj["slug"],
            color=obj["color"],
            is_public=obj["isPublic"],
        )


class GetTagsResponseAdapter(IAdapter[list[FiderAPIResponseType], list[Tag]]):
    @staticmethod
    def to_domain(obj: list[FiderAPIResponseType]) -> list[Tag]:
        return [TagAdapter.to_domain(tag) for tag in obj]
