from typing import cast

from fiderpy.v1.utils.enums import FiderApiUrls
from fiderpy.v1.utils.interfaces import IHttp
from fiderpy.v1.utils.types import FiderAPIResponseType, RequestExtra


class PostsClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def get_posts(self, request: RequestExtra) -> list[FiderAPIResponseType]:
        response = self.http.send(path=FiderApiUrls.POSTS, **request)

        return cast(list[FiderAPIResponseType], response.json())

    def get_post(self, number: int) -> FiderAPIResponseType:
        response = self.http.send(path=f"{FiderApiUrls.POSTS}/{number}")

        return cast(FiderAPIResponseType, response.json())

    def create_post(self, request: RequestExtra) -> FiderAPIResponseType:
        response = self.http.send(path=FiderApiUrls.POSTS, method="POST", **request)

        return cast(FiderAPIResponseType, response.json())
