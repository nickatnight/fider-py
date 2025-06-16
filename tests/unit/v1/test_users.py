from unittest.mock import MagicMock

from fiderpy.v1.resources import UsersClient, UsersService
from fiderpy.v1.resources.users import request
from fiderpy.v1.utils.enums import FiderApiUrls


def test_service_get_users_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = UsersService(client=UsersClient(http=mock_http))

    # Act
    _ = service.get_users()

    # Assert
    mock_http.send.assert_called_once_with(
        path=FiderApiUrls.USERS,
    )


def test_service_create_user_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = UsersService(client=UsersClient(http=mock_http))
    create_request = request.CreateUserRequest(
        name="Test User",
        email="test@example.com",
        reference="test",
    )

    # Act
    _ = service.create_user(create_request)

    # Assert
    mock_http.send.assert_called_once_with(
        path=FiderApiUrls.USERS,
        method="POST",
        json={"name": "Test User", "email": "test@example.com", "reference": "test"},
    )
