from unittest.mock import MagicMock

from fiderpy.fider import Fider, __version__


def test_default_client_http_called_with_correct_args(mocker: MagicMock) -> None:
    # Arrange
    mock_requests_client = mocker.patch("fiderpy.fider.RequestsClient")

    # Act
    _ = Fider(host="fake.com")

    # Assert
    mock_requests_client.assert_called_once_with(
        base_url="fake.com/api/v1",
        headers={
            "User-Agent": f"fiderpy/v{__version__}",
        },
    )


def test_client_properties(
    mocker: MagicMock,
) -> None:
    # Arrange
    mocker.patch("fiderpy.fider.RequestsClient")
    resources = ["users", "posts", "votes", "comments"]

    # Act
    client = Fider(host="fake.com")

    # Assert
    for resource in resources:
        assert hasattr(client, resource)
