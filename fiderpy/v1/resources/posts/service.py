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
    """Service class for posts

    Developers has option to use this service directly or use the ``Fider`` client.
    """

    def __init__(self, client: "PostsClient") -> None:
        self.client = client

    @as_fider(GetPostsResponseAdapter)
    def get_posts(
        self, request: request.GetPostsRequest = request.GetPostsRequest()
    ) -> FiderAPIResponse[list[response.Post]]:
        """Get all posts

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.posts import request
            >>> from fiderpy.v1.resources.posts.service import PostsService

            >>> service = PostsService(client=PostsClient(http=http))
            >>> request = GetPostsRequest(limit=10, query="test", view="all", tags=["test"])
            >>> response = service.get_posts(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully fetched data!",
                data=[
                    Post(
                        id=1,
                        number=1,
                        title="Test Post",
                        slug="test-post",
                        description="This is a test post",
                        created_at="2021-01-01T00:00:00Z",
                        user=User(
                            id=1,
                            name="John Doe",
                            role="admin"
                        ),
                        has_voted=False,
                        votes_count=0,
                        comments_count=0,
                        status="open",
                        response=None,
                        tags=["test"]
                    ),
                ],
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.posts.request.GetPostsRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        params: dict[str, Any] = {"limit": request.limit}

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
        """Get a single post

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.posts import request
            >>> from fiderpy.v1.resources.posts.service import PostsService

            >>> service = PostsService(client=PostsClient(http=http))
            >>> request = GetPostRequest(number=1)
            >>> response = service.get_post(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully fetched data!",
                data=Post(
                    id=1,
                    number=1,
                    title="Test Post",
                    slug="test-post",
                    description="This is a test post",
                    created_at="2021-01-01T00:00:00Z",
                    user=User(
                        id=1,
                        name="John Doe",
                        role="user"
                    ),
                    has_voted=False,
                    votes_count=0,
                    comments_count=0,
                    status="open",
                    response=None,
                    tags=["test"]
                ),
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.posts.request.GetPostRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.get_post(number=request.number)

    @as_fider(CreatePostResponseAdapter)
    def create_post(
        self, request: request.CreatePostRequest
    ) -> FiderAPIResponse[response.CreatePostResponse]:
        """Create a new post

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.posts import request
            >>> from fiderpy.v1.resources.posts.service import PostsService

            >>> service = PostsService(client=PostsClient(http=http))
            >>> request = CreatePostRequest(title="Test Post", description="This is a test post")
            >>> response = service.create_post(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully created post!",
                data=CreatePostResponse(
                    id=1,
                    number=1,
                    title="Test Post",
                    slug="test-post"
                ),
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.posts.request.CreatePostRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        request_data: RequestExtra = {"json": asdict(request)}

        return self.client.create_post(request=request_data)
