from typing import Any
from unittest.mock import MagicMock

from fiderpy.v1.utils.decorators import as_fider
from fiderpy.v1.utils.domain import FiderAPIResponse, FiderError
from fiderpy.v1.utils.exceptions import FiderRequestError
from fiderpy.v1.utils.interfaces import IAdapter


class MockAdapter(IAdapter[dict, str]):
    @staticmethod
    def to_domain(obj: dict) -> str:
        return str(obj)


def test_as_fider_success_with_adapter() -> None:
    # Arrange
    @as_fider(success=MockAdapter)
    def mock_func() -> dict:
        return {"data": "test"}

    # Act
    result = mock_func()

    # Assert
    assert isinstance(result, FiderAPIResponse)
    assert result.message == "Successfully fetched data!"
    assert result.data == "{'data': 'test'}"
    assert result.errors is None


def test_as_fider_success_without_adapter() -> None:
    # Arrange
    @as_fider()
    def mock_func() -> dict:
        return {"data": "test"}

    # Act
    result = mock_func()

    # Assert
    assert isinstance(result, FiderAPIResponse)
    assert result.message == "Successfully fetched data!"
    assert result.data == {"data": "test"}
    assert result.errors is None


def test_as_fider_with_user_id() -> None:
    # Arrange
    @as_fider()
    def mock_func(*args: Any, **kwargs: Any) -> dict:
        return kwargs["request"]  # type: ignore[no-any-return]

    # Act
    result = mock_func(request={"headers": {}}, user_id="123")

    # Assert
    assert isinstance(result, FiderAPIResponse)
    assert result.data["headers"]["X-Fider-UserID"] == "123"  # type: ignore[index]


def test_as_fider_with_500_error() -> None:
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 500

    @as_fider()
    def mock_func() -> None:
        raise FiderRequestError(message="Server Error", response=mock_response)

    # Act
    result = mock_func()

    # Assert
    assert isinstance(result, FiderAPIResponse)
    assert result.data is None
    assert len(result.errors) == 1
    assert isinstance(result.errors[0], FiderError)
    assert "Server Error" in str(result.errors[0].message)


def test_as_fider_with_404_error() -> None:
    # Arrange
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_response.json.return_value = {"errors": [{"message": "resource not found"}]}

    @as_fider()
    def mock_func() -> None:
        raise FiderRequestError(message="Not found", response=mock_response)

    # Act
    result = mock_func()

    # Assert
    assert isinstance(result, FiderAPIResponse)
    assert result.data is None
    assert len(result.errors) == 1
    assert isinstance(result.errors[0], FiderError)
    assert "resource not found" in str(result.errors[0].message)


def test_as_fider_with_unexpected_error() -> None:
    # Arrange
    @as_fider()
    def mock_func() -> None:
        raise ValueError("Unexpected error")

    # Act
    result = mock_func()

    # Assert
    assert isinstance(result, FiderAPIResponse)
    assert result.data is None
    assert len(result.errors) == 1
    assert isinstance(result.errors[0], FiderError)
    assert "Unexpected error" in str(result.errors[0].message)
