from dataclasses import dataclass


@dataclass
class Tag:
    """Represents a tag in the system."""

    id: int
    name: str
    slug: str
    color: str
    is_public: bool


@dataclass
class CreateTagResponse:
    """Represents a response to a tag creation request."""

    id: int
    name: str
    slug: str
    color: str
    is_public: bool
