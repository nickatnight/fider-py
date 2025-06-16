# mypy: disable-error-code="return-value"
from typing import TYPE_CHECKING

from fiderpy.v1.resources.tags import request, response
from fiderpy.v1.resources.tags.adapters import (
    CreateTagResponseAdapter,
    GetTagsResponseAdapter,
)
from fiderpy.v1.utils.decorators import as_fider
from fiderpy.v1.utils.domain import FiderAPIResponse
from fiderpy.v1.utils.types import RequestExtra


if TYPE_CHECKING:
    from fiderpy.v1.resources.tags.client import TagsClient


class TagsService:
    def __init__(self, client: "TagsClient") -> None:
        self.client = client

    @as_fider(GetTagsResponseAdapter)
    def get_tags(self) -> FiderAPIResponse[list[response.Tag]]:
        return self.client.get_tags()

    @as_fider(CreateTagResponseAdapter)
    def create_tag(
        self, request: request.CreateTagRequest
    ) -> FiderAPIResponse[response.CreateTagResponse]:
        request_data: RequestExtra = {
            "json": {
                "name": request.name,
                "color": request.color,
                "isPublic": request.is_public,
            }
        }
        return self.client.create_tag(request=request_data)

    @as_fider(CreateTagResponseAdapter)
    def edit_tag(
        self, slug: str, request: request.EditTagRequest
    ) -> FiderAPIResponse[response.CreateTagResponse]:
        request_data: RequestExtra = {
            "json": {
                "name": request.name,
                "color": request.color,
                "isPublic": request.is_public,
            }
        }
        return self.client.edit_tag(slug=slug, request=request_data)

    @as_fider()
    def delete_tag(self, slug: str) -> FiderAPIResponse[dict]:
        return self.client.delete_tag(slug=slug)

    @as_fider()
    def tag_post(self, request: request.TagPostRequest) -> FiderAPIResponse[dict]:
        return self.client.tag_post(number=request.number, slug=request.slug)

    @as_fider()
    def untag_post(self, request: request.TagPostRequest) -> FiderAPIResponse[dict]:
        return self.client.untag_post(number=request.number, slug=request.slug)
