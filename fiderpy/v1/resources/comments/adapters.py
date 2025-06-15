from fiderpy.v1.resources.comments.response import Comment, CreateCommentResponse
from fiderpy.v1.resources.posts.adapters import UserAdapter
from fiderpy.v1.utils.interfaces import IAdapter
from fiderpy.v1.utils.types import FiderAPIResponseType


class CommentAdapter(IAdapter[FiderAPIResponseType, Comment]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> Comment:
        edited_by = None
        if "editedBy" in obj:
            edited_by = UserAdapter.to_domain(obj=obj["editedBy"])

        return Comment(
            id=obj["id"],
            content=obj["content"],
            created_at=obj["createdAt"],
            user=UserAdapter.to_domain(obj=obj["user"]),
            edited_at=obj.get("editedAt"),
            edited_by=edited_by,
        )


class GetCommentsResponseAdapter(IAdapter[list[FiderAPIResponseType], list[Comment]]):
    @staticmethod
    def to_domain(obj: list[FiderAPIResponseType]) -> list[Comment]:
        return [CommentAdapter.to_domain(obj=comment) for comment in obj]


class GetCommentResponseAdapter(IAdapter[FiderAPIResponseType, Comment]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> Comment:
        return CommentAdapter.to_domain(obj=obj)


class CreateCommentResponseAdapter(
    IAdapter[FiderAPIResponseType, CreateCommentResponse]
):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> CreateCommentResponse:
        return CreateCommentResponse(id=obj["id"])
