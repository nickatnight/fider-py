from dataclasses import dataclass
from typing import Optional

from fiderpy.v1.resources.posts.enums import PostsViewEnum


@dataclass
class GetPostsRequest:
    """
    Represents a request to create or update a post.
    """

    query: Optional[str] = None
    view: Optional[str] = PostsViewEnum.ALL
    limit: Optional[int] = 30
    tags: Optional[str] = None


@dataclass
class CreatePostRequest:
    """Represents a request to create a new post."""

    title: str
    description: str


@dataclass
class GetPostRequest:
    """Represents a request to create a new post."""

    number: int
