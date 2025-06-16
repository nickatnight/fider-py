from typing import cast

from fiderpy.v1.utils.enums import FiderApiUrls
from fiderpy.v1.utils.interfaces import IHttp
from fiderpy.v1.utils.types import FiderAPIResponseType, RequestExtra


class PostsClient:
    """API clients for /posts

    https://docs.fider.io/api/posts/
    """

    def __init__(self, http: IHttp) -> None:
        self.http = http

    def get_posts(self, request: RequestExtra) -> list[FiderAPIResponseType]:
        """Get all posts

        :param request:         Extra data to send with the request
        :return:                :class:`fiderpy.v1.utils.types.FiderAPIResponseType`
        """
        response = self.http.send(path=FiderApiUrls.POSTS, **request)

        return cast(list[FiderAPIResponseType], response.json())

    def get_post(self, number: int) -> FiderAPIResponseType:
        """Get a single post

        :param number:          Post number
        :return:                :class:`fiderpy.v1.utils.types.FiderAPIResponseType`
        """
        response = self.http.send(path=f"{FiderApiUrls.POSTS}/{number}")

        return cast(FiderAPIResponseType, response.json())

    def create_post(self, request: RequestExtra) -> FiderAPIResponseType:
        """Create a new post

        :param request:         Extra data to send with the request
        :return:                :class:`fiderpy.v1.utils.types.FiderAPIResponseType`
        """
        response = self.http.send(path=FiderApiUrls.POSTS, method="POST", **request)

        return cast(FiderAPIResponseType, response.json())
