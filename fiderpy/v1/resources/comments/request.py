from dataclasses import dataclass


@dataclass
class GetCommentsRequest:
    number: int


@dataclass
class GetCommentRequest:
    number: int
    id: int


@dataclass
class CreateCommentRequest:
    number: int
    content: str


@dataclass
class EditCommentRequest:
    number: int
    id: int
    content: str


@dataclass
class DeleteCommentRequest:
    number: int
    id: int
