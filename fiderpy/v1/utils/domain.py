from dataclasses import dataclass
from typing import Generic, Optional, TypeVar


T = TypeVar("T")


@dataclass
class FiderError:
    message: str
    field: Optional[str] = None


@dataclass
class FiderAPIResponse(Generic[T]):
    message: str
    data: T | None
    errors: list[FiderError] | None
