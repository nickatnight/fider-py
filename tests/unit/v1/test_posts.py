from unittest.mock import MagicMock

from fiderpy.v1.resources import PostsClient, PostsService
from fiderpy.v1.resources.posts import request
from fiderpy.v1.utils.enums import FiderApiUrls


def test_service_get_posts_http_called_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = PostsService(client=PostsClient(http=mock_http))

    # Act
    _ = service.get_posts()

    # Assert
    mock_http.send.assert_called_once_with(
        path=FiderApiUrls.POSTS,
        params={"limit": 30},
    )


def test_service_get_posts_with_params_http_called_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = PostsService(client=PostsClient(http=mock_http))

    # Act
    _ = service.get_posts(
        request.GetPostsRequest(query="open+links", view="planned", tags="test")
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=FiderApiUrls.POSTS,
        params={"limit": 30, "query": "open+links", "view": "planned", "tags": "test"},
    )


def test_service_get_post_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = PostsService(client=PostsClient(http=mock_http))
    post_number = 123

    # Act
    _ = service.get_post(request.GetPostRequest(number=post_number))

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}",
    )


def test_service_create_post_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = PostsService(client=PostsClient(http=mock_http))
    create_request = request.CreatePostRequest(
        title="Test Post",
        description="Test Description",
    )

    # Act
    _ = service.create_post(create_request)

    # Assert
    mock_http.send.assert_called_once_with(
        path=FiderApiUrls.POSTS,
        method="POST",
        json={"title": "Test Post", "description": "Test Description"},
    )
