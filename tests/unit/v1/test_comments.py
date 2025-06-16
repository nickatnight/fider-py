from unittest.mock import MagicMock

from fiderpy.v1.resources import CommentsClient, CommentsService
from fiderpy.v1.resources.comments import request
from fiderpy.v1.utils.enums import FiderApiUrls


def test_service_get_comments_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = CommentsService(client=CommentsClient(http=mock_http))
    post_number = 123

    # Act
    _ = service.get_comments(request.GetCommentsRequest(number=post_number))

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}{FiderApiUrls.COMMENTS}",
    )


def test_service_get_comment_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = CommentsService(client=CommentsClient(http=mock_http))
    post_number = 123
    comment_id = 456

    # Act
    _ = service.get_comment(
        request.GetCommentRequest(number=post_number, id=comment_id)
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}{FiderApiUrls.COMMENTS}/{comment_id}",
    )


def test_service_create_comment_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = CommentsService(client=CommentsClient(http=mock_http))
    post_number = 123
    content = "Test comment"

    # Act
    _ = service.create_comment(
        request.CreateCommentRequest(number=post_number, content=content)
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}{FiderApiUrls.COMMENTS}",
        method="POST",
        json={"content": content},
    )


def test_service_edit_comment_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock()
    service = CommentsService(client=CommentsClient(http=mock_http))
    post_number = 123
    comment_id = 456
    content = "Updated comment"

    # Act
    _ = service.edit_comment(
        request.EditCommentRequest(number=post_number, id=comment_id, content=content)
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}{FiderApiUrls.COMMENTS}/{comment_id}",
        method="PUT",
        json={"content": content},
    )


def test_service_delete_comment_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = CommentsService(client=CommentsClient(http=mock_http))
    post_number = 123
    comment_id = 456

    # Act
    _ = service.delete_comment(
        request.DeleteCommentRequest(number=post_number, id=comment_id)
    )

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{post_number}{FiderApiUrls.COMMENTS}/{comment_id}",
        method="DELETE",
    )
