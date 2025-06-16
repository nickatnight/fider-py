# mypy: disable-error-code="return-value"
from typing import TYPE_CHECKING

from fiderpy.v1.resources.votes import request, response
from fiderpy.v1.resources.votes.adapters import GetVotesResponseAdapter
from fiderpy.v1.utils.decorators import as_fider
from fiderpy.v1.utils.domain import FiderAPIResponse


if TYPE_CHECKING:
    from fiderpy.v1.resources.votes.client import VotesClient


class VotesService:
    """Service class for votes

    Developers has option to use this service directly or use the ``Fider`` client.
    """

    def __init__(self, client: "VotesClient") -> None:
        self.client = client

    @as_fider(GetVotesResponseAdapter)
    def get_votes(
        self, request: request.GetVotesRequest
    ) -> FiderAPIResponse[list[response.Vote]]:
        """Get all votes for a post

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.votes import request
            >>> from fiderpy.v1.resources.votes.service import VotesService

            >>> service = VotesService(client=VotesClient(http=http))
            >>> request = GetVotesRequest(number=1)
            >>> response = service.get_votes(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully fetched data!",
                data=[
                    Vote(
                        id=1,
                        user=User(
                            id=1,
                            name="John Doe",
                            role="user"
                        ),
                        created_at="2021-01-01T00:00:00Z"
                    ),
                ],
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.votes.request.GetVotesRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.get_votes(number=request.number)

    @as_fider()
    def delete_vote(self, request: request.DeleteVoteRequest) -> FiderAPIResponse[dict]:
        """When removing the vote from a post, the vote is removed from the current authenticated user. Impersonate another user to remove votes on behalf of them.

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.votes import request
            >>> from fiderpy.v1.resources.votes.service import VotesService

            >>> service = VotesService(client=VotesClient(http=http))
            >>> request = DeleteVoteRequest(number=1)
            >>> response = service.delete_vote(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully deleted vote!",
                data={},
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.votes.request.DeleteVoteRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.delete_vote(number=request.number)

    @as_fider()
    def create_vote(self, request: request.CreateVoteRequest) -> FiderAPIResponse[dict]:
        """When casting a vote upon a post, the vote is registered under the current authenticated user. Impersonate another user to vote on behalf of them.

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.votes import request
            >>> from fiderpy.v1.resources.votes.service import VotesService

            >>> service = VotesService(client=VotesClient(http=http))
            >>> request = CreateVoteRequest(number=1)
            >>> response = service.create_vote(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully created vote!",
                data={},
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.votes.request.CreateVoteRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.create_vote(number=request.number)
