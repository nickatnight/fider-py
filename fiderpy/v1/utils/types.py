from typing import Any, Mapping, TypedDict

from typing_extensions import NotRequired


class RequestExtra(TypedDict):
    """Base request params structure."""

    params: NotRequired[dict]
    headers: NotRequired[dict]
    json: NotRequired[dict]


FiderAPIResponseType = Mapping[str, Any]
