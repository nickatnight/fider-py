from dataclasses import dataclass


@dataclass
class CreateTagRequest:
    """Represents a request to create a new tag."""

    name: str
    color: str
    is_public: bool


@dataclass
class EditTagRequest:
    """Represents a request to edit an existing tag."""

    name: str
    color: str
    is_public: bool


@dataclass
class TagPostRequest:
    """Represents a request to tag a post."""

    number: int
    slug: str
