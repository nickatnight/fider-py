from fiderpy.v1.resources.votes.response import User, Vote
from fiderpy.v1.utils.interfaces import IAdapter
from fiderpy.v1.utils.types import FiderAPIResponseType


class UserAdapter(IAdapter[FiderAPIResponseType, User]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> User:
        return User(
            id=obj["id"],
            name=obj["name"],
            email=obj["email"],
        )


class VoteAdapter(IAdapter[FiderAPIResponseType, Vote]):
    @staticmethod
    def to_domain(obj: FiderAPIResponseType) -> Vote:
        return Vote(
            created_at=obj["createdAt"], user=UserAdapter.to_domain(obj=obj["user"])
        )


class GetVotesResponseAdapter(IAdapter[list[FiderAPIResponseType], list[Vote]]):
    @staticmethod
    def to_domain(obj: list[FiderAPIResponseType]) -> list[Vote]:
        return [VoteAdapter.to_domain(obj=vote) for vote in obj]
