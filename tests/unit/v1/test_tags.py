from unittest.mock import MagicMock

from fiderpy.v1.resources import TagsClient, TagsService
from fiderpy.v1.resources.tags import request
from fiderpy.v1.utils.enums import FiderApiUrls


def test_service_get_tags_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = TagsService(client=TagsClient(http=mock_http))

    # Act
    _ = service.get_tags()

    # Assert
    mock_http.send.assert_called_once_with(
        path=FiderApiUrls.TAGS,
    )


def test_service_create_tag_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = TagsService(client=TagsClient(http=mock_http))
    create_request = request.CreateTagRequest(
        name="Test Tag",
        color="FE422D",
        is_public=True,
    )

    # Act
    _ = service.create_tag(create_request)

    # Assert
    mock_http.send.assert_called_once_with(
        path=FiderApiUrls.TAGS,
        method="POST",
        json={"name": "Test Tag", "color": "FE422D", "isPublic": True},
    )


def test_service_edit_tag_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = TagsService(client=TagsClient(http=mock_http))
    edit_request = request.EditTagRequest(
        name="Updated Tag",
        color="063589",
        is_public=False,
    )
    slug = "test-tag"

    # Act
    _ = service.edit_tag(slug=slug, request=edit_request)

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.TAGS}/{slug}",
        method="PUT",
        json={"name": "Updated Tag", "color": "063589", "isPublic": False},
    )


def test_service_delete_tag_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = TagsService(client=TagsClient(http=mock_http))
    slug = "test-tag"

    # Act
    _ = service.delete_tag(slug=slug)

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.TAGS}/{slug}",
        method="DELETE",
    )


def test_service_tag_post_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = TagsService(client=TagsClient(http=mock_http))
    tag_request = request.TagPostRequest(
        number=123,
        slug="test-tag",
    )

    # Act
    _ = service.tag_post(tag_request)

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{tag_request.number}{FiderApiUrls.TAGS}/{tag_request.slug}",
        method="POST",
    )


def test_service_untag_post_http_called_with_expected_args() -> None:
    # Arrange
    mock_http = MagicMock(send=MagicMock())
    service = TagsService(client=TagsClient(http=mock_http))
    tag_request = request.TagPostRequest(
        number=123,
        slug="test-tag",
    )

    # Act
    _ = service.untag_post(tag_request)

    # Assert
    mock_http.send.assert_called_once_with(
        path=f"{FiderApiUrls.POSTS}/{tag_request.number}{FiderApiUrls.TAGS}/{tag_request.slug}",
        method="DELETE",
    )
