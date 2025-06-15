from fiderpy.v1.resources.users.response import CreateUserResponse, User
from fiderpy.v1.utils.interfaces import IAdapter
from fiderpy.v1.utils.types import FiderAPIResponseType


class CreateUserResponseAdapter(IAdapter[FiderAPIResponseType, CreateUserResponse]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> CreateUserResponse:
        return CreateUserResponse(id=obj["id"])


class UserAdapter(IAdapter[FiderAPIResponseType, User]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> User:
        return User(
            id=obj["id"],
            name=obj["name"],
            role=obj["role"],
            status=obj["status"],
        )


class GetUsersResponseAdapter(IAdapter[list[FiderAPIResponseType], list[User]]):
    @staticmethod
    def to_domain(obj: list[FiderAPIResponseType]) -> list[User]:
        return [UserAdapter.to_domain(obj=item) for item in obj]
