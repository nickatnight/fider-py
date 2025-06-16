from unittest.mock import MagicMock

from fiderpy.v1.resources import VotesClient, VotesService
from fiderpy.v1.resources.votes import request
from fiderpy.v1.utils.enums import FiderApiUrls


def test_service_get_votes_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = VotesService(client=VotesClient(http=mock_http))
    post_number = 123

    # Act
    _ = service.get_votes(request.GetVotesRequest(number=post_number))

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}{FiderApiUrls.VOTES}",
    )


def test_service_create_vote_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = VotesService(client=VotesClient(http=mock_http))
    post_number = 123

    # Act
    _ = service.create_vote(request.CreateVoteRequest(number=post_number))

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}{FiderApiUrls.VOTES}",
        method="POST",
    )


def test_service_delete_vote_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = VotesService(client=VotesClient(http=mock_http))
    post_number = 123

    # Act
    _ = service.delete_vote(request.DeleteVoteRequest(number=post_number))

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}{FiderApiUrls.VOTES}",
        method="DELETE",
    )
