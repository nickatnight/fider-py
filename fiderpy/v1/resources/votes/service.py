# mypy: disable-error-code="return-value"
from typing import TYPE_CHECKING

from fiderpy.v1.resources.votes import request, response
from fiderpy.v1.resources.votes.adapters import GetVotesResponseAdapter
from fiderpy.v1.utils.decorators import as_fider
from fiderpy.v1.utils.domain import FiderAPIResponse


if TYPE_CHECKING:
    from fiderpy.v1.resources.votes.client import VotesClient


class VotesService:
    def __init__(self, client: "VotesClient") -> None:
        self.client = client

    @as_fider(GetVotesResponseAdapter)
    def get_votes(
        self, request: request.GetVotesRequest
    ) -> FiderAPIResponse[list[response.Vote]]:
        return self.client.get_votes(number=request.number)

    @as_fider()
    def delete_vote(self, request: request.DeleteVoteRequest) -> FiderAPIResponse[dict]:
        return self.client.delete_vote(number=request.number)

    @as_fider()
    def create_vote(self, request: request.CreateVoteRequest) -> FiderAPIResponse[dict]:
        return self.client.create_vote(number=request.number)
