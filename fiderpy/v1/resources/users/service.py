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
    """Service class for users

    Developers has option to use this service directly or use the ``Fider`` client.
    """

    def __init__(self, client: "UsersClient") -> None:
        self.client = client

    @as_fider(GetUsersResponseAdapter)
    def get_users(self) -> FiderAPIResponse[list[response.User]]:
        """Get all users

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.users.service import UsersService

            >>> service = UsersService(client=UsersClient(http=http))
            >>> response = service.get_users()
            >>> response
            FiderAPIResponse(
                message="Successfully fetched data!",
                data=[
                    User(
                        id=1,
                        name="John Doe",
                        role="user",
                        email="john@example.com",
                        status="active"
                    ),
                ],
                errors=None
            )

        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.get_users()

    @as_fider(CreateUserResponseAdapter)
    def create_user(
        self, request: request.CreateUserRequest
    ) -> FiderAPIResponse[response.CreateUserResponse]:
        """Create a new user

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.users import request
            >>> from fiderpy.v1.resources.users.service import UsersService

            >>> service = UsersService(client=UsersClient(http=http))
            >>> request = CreateUserRequest(name="John Doe", email="john@example.com")
            >>> response = service.create_user(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully created user!",
                data=CreateUserResponse(
                    id=1,
                    name="John Doe",
                    email="john@example.com",
                    role="user",
                    status="active"
                ),
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.users.request.CreateUserRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        request_data: RequestExtra = {"json": asdict(request)}

        return self.client.create_user(request=request_data)
