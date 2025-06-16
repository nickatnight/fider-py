# mypy: disable-error-code="return-value"
from typing import TYPE_CHECKING

from fiderpy.v1.resources.tags import request, response
from fiderpy.v1.resources.tags.adapters import (
    CreateTagResponseAdapter,
    GetTagsResponseAdapter,
)
from fiderpy.v1.utils.decorators import as_fider
from fiderpy.v1.utils.domain import FiderAPIResponse
from fiderpy.v1.utils.types import RequestExtra


if TYPE_CHECKING:
    from fiderpy.v1.resources.tags.client import TagsClient


class TagsService:
    """Service class for tags

    Developers has option to use this service directly or use the ``Fider`` client.
    """

    def __init__(self, client: "TagsClient") -> None:
        self.client = client

    @as_fider(GetTagsResponseAdapter)
    def get_tags(self) -> FiderAPIResponse[list[response.Tag]]:
        """Get all tags

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.tags.service import TagsService

            >>> service = TagsService(client=TagsClient(http=http))
            >>> response = service.get_tags()
            >>> response
            FiderAPIResponse(
                message="Successfully fetched data!",
                data=[
                    Tag(
                        id=1,
                        name="bug",
                        slug="bug",
                        color="#FF0000",
                        isPublic=True
                    ),
                ],
                errors=None
            )

        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.get_tags()

    @as_fider(CreateTagResponseAdapter)
    def create_tag(
        self, request: request.CreateTagRequest
    ) -> FiderAPIResponse[response.CreateTagResponse]:
        """Create a new tag

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.tags import request
            >>> from fiderpy.v1.resources.tags.service import TagsService

            >>> service = TagsService(client=TagsClient(http=http))
            >>> request = CreateTagRequest(name="bug", color="#FF0000", is_public=True)
            >>> response = service.create_tag(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully created tag!",
                data=CreateTagResponse(
                    id=1,
                    name="bug",
                    slug="bug",
                    color="#FF0000",
                    isPublic=True
                ),
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.tags.request.CreateTagRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        request_data: RequestExtra = {
            "json": {
                "name": request.name,
                "color": request.color,
                "isPublic": request.is_public,
            }
        }
        return self.client.create_tag(request=request_data)

    @as_fider(CreateTagResponseAdapter)
    def edit_tag(
        self, request: request.EditTagRequest
    ) -> FiderAPIResponse[response.CreateTagResponse]:
        """Edit an existing tag

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.tags import request
            >>> from fiderpy.v1.resources.tags.service import TagsService

            >>> service = TagsService(client=TagsClient(http=http))
            >>> request = EditTagRequest(slug="bug", name="bug-fixed", color="#00FF00", is_public=True)
            >>> response = service.edit_tag(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully updated tag!",
                data=CreateTagResponse(
                    id=1,
                    name="bug-fixed",
                    slug="bug-fixed",
                    color="#00FF00",
                    isPublic=True
                ),
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.tags.request.EditTagRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        request_data: RequestExtra = {
            "json": {
                "name": request.name,
                "color": request.color,
                "isPublic": request.is_public,
            }
        }
        return self.client.edit_tag(slug=request.slug, request=request_data)

    @as_fider()
    def delete_tag(self, request: request.DeleteTagRequest) -> FiderAPIResponse[dict]:
        """Delete a tag

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.tags.service import TagsService

            >>> service = TagsService(client=TagsClient(http=http))
            >>> request = DeleteTagRequest(slug="bug")
            >>> response = service.delete_tag(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully deleted tag!",
                data={},
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.tags.request.DeleteTagRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.delete_tag(slug=request.slug)

    @as_fider()
    def tag_post(self, request: request.TagPostRequest) -> FiderAPIResponse[dict]:
        """Add a tag to a post

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.tags import request
            >>> from fiderpy.v1.resources.tags.service import TagsService

            >>> service = TagsService(client=TagsClient(http=http))
            >>> request = TagPostRequest(number=1, slug="bug")
            >>> response = service.tag_post(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully tagged post!",
                data={},
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.tags.request.TagPostRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.tag_post(number=request.number, slug=request.slug)

    @as_fider()
    def untag_post(self, request: request.TagPostRequest) -> FiderAPIResponse[dict]:
        """Remove a tag from a post

        Example:

        .. code-block:: python

            >>> from fiderpy.v1.resources.tags import request
            >>> from fiderpy.v1.resources.tags.service import TagsService

            >>> service = TagsService(client=TagsClient(http=http))
            >>> request = TagPostRequest(number=1, slug="bug")
            >>> response = service.untag_post(request=request)
            >>> response
            FiderAPIResponse(
                message="Successfully untagged post!",
                data={},
                errors=None
            )

        :param request:         :class:`fiderpy.v1.resources.tags.request.TagPostRequest`
        :return:                :class:`fiderpy.v1.utils.domain.FiderAPIResponse`
        """
        return self.client.untag_post(number=request.number, slug=request.slug)
