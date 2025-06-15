from dataclasses import dataclass
from typing import Optional

from fiderpy.v1.resources.posts.response import User


@dataclass
class Comment:
    id: int
    content: str
    created_at: str
    user: User
    edited_at: Optional[str] = None
    edited_by: Optional[User] = None


@dataclass
class CreateCommentResponse:
    id: int
