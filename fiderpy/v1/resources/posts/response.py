from dataclasses import dataclass
from typing import Any, Optional


@dataclass
class CreatePostResponse:
    """Represents a response to a post creation request."""

    id: int
    number: int
    title: str
    slug: str


@dataclass
class User:
    id: int
    name: str
    role: str


ResponseUser = User


@dataclass
class PostResponse:
    text: str
    respondedAt: str
    user: ResponseUser
    original: Optional[Any] = None  # Could be None or another response


@dataclass
class Post:
    id: int
    number: int
    title: str
    slug: str
    description: str
    created_at: str
    user: User
    has_voted: bool
    votes_count: int
    comments_count: int
    status: str
    response: Optional[PostResponse]
    tags: list[str]
