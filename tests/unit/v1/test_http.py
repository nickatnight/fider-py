from unittest.mock import MagicMock

import pytest

from fiderpy.v1.utils.exceptions import FiderRequestError
from fiderpy.v1.utils.http import (  # type: ignore
    RequestsClient,
    _get_headers,
    default_headers,
    requests,
)


def test_client_fider_request_error(mocker: MagicMock) -> None:
    # Arrange
    mocker.patch.object(
        requests.Session,
        "get",
        side_effect=requests.exceptions.HTTPError("Error"),
    )

    # Act
    client = RequestsClient()

    # Assert
    with pytest.raises(FiderRequestError):
        client.send("fakeurl.com")


def test_get_headers(mocker: MagicMock) -> None:
    # Arrange
    headers = {"test": "test"}
    headers_response = {**headers, **default_headers}

    # Assert
    assert _get_headers(headers=headers) == headers_response


def test_client_fider_other_error(mocker: MagicMock) -> None:
    # Arrange
    mocker.patch.object(
        requests.Session,
        "get",
        side_effect=ValueError("Error"),
    )

    # Act
    client = RequestsClient()

    # Assert
    with pytest.raises(ValueError):
        client.send("fakeurl")


def test_client_success_response(mocker: MagicMock) -> None:
    # Arrange
    mock_response = MagicMock()
    mock_response.json = MagicMock(return_value={"data": "test"})
    mocker.patch.object(
        requests.Session,
        "get",
        return_value=mock_response,
    )

    # Act
    client = RequestsClient()
    response = client.send("fakeurl")

    # Assert
    assert response.json() == {"data": "test"}
    mock_response.json.assert_called_once()
    mock_response.raise_for_status.assert_called_once()
