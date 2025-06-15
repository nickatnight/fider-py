# mypy: disable-error-code="return-value"
from dataclasses import asdict
from typing import TYPE_CHECKING

from fiderpy.v1.resources.users import request, response
from fiderpy.v1.resources.users.adapters import (
    CreateUserResponseAdapter,
    GetUsersResponseAdapter,
)
from fiderpy.v1.utils.decorators import as_fider
from fiderpy.v1.utils.domain import FiderAPIResponse
from fiderpy.v1.utils.types import RequestExtra


if TYPE_CHECKING:
    from fiderpy.v1.resources.users.client import UsersClient


class UsersService:
    def __init__(self, client: "UsersClient") -> None:
        self.client = client

    @as_fider(GetUsersResponseAdapter)
    def get_users(self) -> FiderAPIResponse[list[response.User]]:
        return self.client.get_users()

    @as_fider(CreateUserResponseAdapter)
    def create_user(
        self, request: request.CreateUserRequest
    ) -> FiderAPIResponse[response.CreateUserResponse]:
        request_data: RequestExtra = {"json": asdict(request)}

        return self.client.create_user(request=request_data)
