# mypy: disable-error-code="return-value"
from typing import TYPE_CHECKING

from fiderpy.v1.resources.comments import request, response
from fiderpy.v1.resources.comments.adapters import (
    CreateCommentResponseAdapter,
    GetCommentResponseAdapter,
    GetCommentsResponseAdapter,
)
from fiderpy.v1.utils.decorators import as_fider
from fiderpy.v1.utils.domain import FiderAPIResponse
from fiderpy.v1.utils.types import RequestExtra


if TYPE_CHECKING:
    from fiderpy.v1.resources.comments.client import CommentsClient


class CommentsService:
    """Service class for comments

    Developers has option to use this service directly or use the ``Fider`` client.
    """

    def __init__(self, client: "CommentsClient") -> None:
        self.client = client

    @as_fider(GetCommentsResponseAdapter)
    def get_comments(
        self, request: request.GetCommentsRequest
    ) -> FiderAPIResponse[list[response.Comment]]:
        """Get all comments for a post

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.comments import request
            >>> from fiderpy.v1.resources.comments.service import CommentsService

            >>> service = CommentsService(client=CommentsClient(http=http))
            >>> request = GetCommentsRequest(number=1)
            >>> response = service.get_comments(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully fetched data!",
                data=[
                    Comment(
                        id=1,
                        content="This is a comment",
                        created_at="2021-01-01T00:00:00Z",
                        user=User(
                            id=1,
                            name="John Doe",
                            role="user"
                        )
                    ),
                ],
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.comments.request.GetCommentsRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.get_comments(number=request.number)

    @as_fider(GetCommentResponseAdapter)
    def get_comment(
        self, request: request.GetCommentRequest
    ) -> FiderAPIResponse[response.Comment]:
        """Get a single comment

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.comments import request
            >>> from fiderpy.v1.resources.comments.service import CommentsService

            >>> service = CommentsService(client=CommentsClient(http=http))
            >>> request = GetCommentRequest(number=1, id=1)
            >>> response = service.get_comment(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully fetched data!",
                data=Comment(
                    id=1,
                    content="This is a comment",
                    created_at="2021-01-01T00:00:00Z",
                    user=User(
                        id=1,
                        name="John Doe",
                        role="user"
                    )
                ),
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.comments.request.GetCommentRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.get_comment(number=request.number, id=request.id)

    @as_fider(CreateCommentResponseAdapter)
    def create_comment(
        self, request: request.CreateCommentRequest
    ) -> FiderAPIResponse[response.CreateCommentResponse]:
        """Create a new comment

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.comments import request
            >>> from fiderpy.v1.resources.comments.service import CommentsService

            >>> service = CommentsService(client=CommentsClient(http=http))
            >>> request = CreateCommentRequest(number=1, content="This is a comment")
            >>> response = service.create_comment(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully created comment!",
                data=CreateCommentResponse(
                    id=1,
                    content="This is a comment",
                    created_at="2021-01-01T00:00:00Z"
                ),
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.comments.request.CreateCommentRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        request_data: RequestExtra = {
            "json": {"content": request.content},
        }
        return self.client.create_comment(number=request.number, request=request_data)

    @as_fider()
    def edit_comment(
        self, request: request.EditCommentRequest
    ) -> FiderAPIResponse[dict]:
        """Edit an existing comment

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.comments import request
            >>> from fiderpy.v1.resources.comments.service import CommentsService

            >>> service = CommentsService(client=CommentsClient(http=http))
            >>> request = EditCommentRequest(number=1, id=1, content="Updated comment")
            >>> response = service.edit_comment(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully updated comment!",
                data={},
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.comments.request.EditCommentRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        request_data: RequestExtra = {
            "json": {"content": request.content},
        }
        return self.client.edit_comment(
            number=request.number, id=request.id, request=request_data
        )

    @as_fider()
    def delete_comment(
        self, request: request.DeleteCommentRequest
    ) -> FiderAPIResponse[dict]:
        """Delete a comment

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.comments import request
            >>> from fiderpy.v1.resources.comments.service import CommentsService

            >>> service = CommentsService(client=CommentsClient(http=http))
            >>> request = DeleteCommentRequest(number=1, id=1)
            >>> response = service.delete_comment(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully deleted comment!",
                data={},
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.comments.request.DeleteCommentRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.delete_comment(number=request.number, id=request.id)
