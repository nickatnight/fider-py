from fiderpy.v1.resources.posts.response import CreatePostResponse, Post, User
from fiderpy.v1.utils.interfaces import IAdapter
from fiderpy.v1.utils.types import FiderAPIResponseType


class CreatePostResponseAdapter(IAdapter[FiderAPIResponseType, CreatePostResponse]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> CreatePostResponse:
        return CreatePostResponse(
            id=obj["id"], number=obj["number"], title=obj["title"], slug=obj["slug"]
        )


class UserAdapter(IAdapter[FiderAPIResponseType, User]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> User:
        return User(
            id=obj["id"],
            name=obj["name"],
            role=obj["role"],
        )


class PostAdapter(IAdapter[FiderAPIResponseType, Post]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> Post:
        return Post(
            id=obj["id"],
            number=obj["number"],
            title=obj["title"],
            slug=obj["slug"],
            description=obj["description"],
            created_at=obj["createdAt"],
            user=UserAdapter.to_domain(obj=obj["user"]),
            has_voted=obj["hasVoted"],
            votes_count=obj["votesCount"],
            comments_count=obj["commentsCount"],
            status=obj["status"],
            response=obj.get("response"),
            tags=obj.get("tags", []),
        )


class GetPostResponseAdapter(IAdapter[FiderAPIResponseType, Post]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> Post:
        return PostAdapter.to_domain(obj=obj)


class GetPostsResponseAdapter(IAdapter[list[FiderAPIResponseType], list[Post]]):
    @staticmethod
    def to_domain(obj: list[FiderAPIResponseType]) -> list[Post]:
        return [PostAdapter.to_domain(post) for post in obj]
