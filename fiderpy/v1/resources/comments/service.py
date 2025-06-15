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
    def __init__(self, client: "CommentsClient") -> None:
        self.client = client

    @as_fider(GetCommentsResponseAdapter)
    def get_comments(
        self, request: request.GetCommentsRequest
    ) -> FiderAPIResponse[list[response.Comment]]:
        return self.client.get_comments(number=request.number)

    @as_fider(GetCommentResponseAdapter)
    def get_comment(
        self, request: request.GetCommentRequest
    ) -> FiderAPIResponse[response.Comment]:
        return self.client.get_comment(number=request.number, id=request.id)

    @as_fider(CreateCommentResponseAdapter)
    def create_comment(
        self, request: request.CreateCommentRequest
    ) -> FiderAPIResponse[response.CreateCommentResponse]:
        request_data: RequestExtra = {
            "json": {"content": request.content},
        }
        return self.client.create_comment(number=request.number, request=request_data)

    @as_fider()
    def edit_comment(
        self, request: request.EditCommentRequest
    ) -> FiderAPIResponse[dict]:
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
        return self.client.delete_comment(number=request.number, id=request.id)
