# mypy: disable-error-code="return-value"
from dataclasses import asdict
from typing import TYPE_CHECKING, Any

from fiderpy.v1.resources.posts import request, response
from fiderpy.v1.resources.posts.adapters import (
    CreatePostResponseAdapter,
    GetPostResponseAdapter,
    GetPostsResponseAdapter,
)
from fiderpy.v1.utils.decorators import as_fider
from fiderpy.v1.utils.domain import FiderAPIResponse
from fiderpy.v1.utils.types import RequestExtra


if TYPE_CHECKING:
    from fiderpy.v1.resources.posts.client import PostsClient


class PostsService:
    def __init__(self, client: "PostsClient") -> None:
        self.client = client

    @as_fider(GetPostsResponseAdapter)
    def get_posts(
        self, request: request.GetPostsRequest = request.GetPostsRequest()
    ) -> FiderAPIResponse[list[response.Post]]:
        params: dict[str, Any] = {"params": {"limit": request.limit}}

        if request.query:
            params["query"] = request.query

        if request.view:
            params["view"] = request.view

        if request.tags:
            params["tags"] = request.tags

        request_data: RequestExtra = {"params": params}

        return self.client.get_posts(request=request_data)

    @as_fider(GetPostResponseAdapter)
    def get_post(
        self, request: request.GetPostRequest
    ) -> FiderAPIResponse[response.Post]:
        return self.client.get_post(number=request.number)

    @as_fider(CreatePostResponseAdapter)
    def create_post(
        self, request: request.CreatePostRequest
    ) -> FiderAPIResponse[response.CreatePostResponse]:
        request_data: RequestExtra = {"json": asdict(request)}

        return self.client.create_post(request=request_data)
