from typing import cast

from fiderpy.v1.utils.enums import FiderApiUrls
from fiderpy.v1.utils.interfaces import IHttp
from fiderpy.v1.utils.types import FiderAPIResponseType, RequestExtra


class TagsClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def get_tags(self) -> list[FiderAPIResponseType]:
        response = self.http.send(path=FiderApiUrls.TAGS)
        return cast(list[FiderAPIResponseType], response.json())

    def create_tag(self, request: RequestExtra) -> FiderAPIResponseType:
        response = self.http.send(
            path=FiderApiUrls.TAGS,
            method="POST",
            **request,
        )
        return cast(FiderAPIResponseType, response.json())

    def edit_tag(self, slug: str, request: RequestExtra) -> FiderAPIResponseType:
        response = self.http.send(
            path=f"{FiderApiUrls.TAGS}/{slug}",
            method="PUT",
            **request,
        )
        return cast(FiderAPIResponseType, response.json())

    def delete_tag(self, slug: str) -> dict:
        response = self.http.send(
            path=f"{FiderApiUrls.TAGS}/{slug}",
            method="DELETE",
        )
        return cast(dict, response.json())

    def tag_post(self, number: int, slug: str) -> dict:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.TAGS}/{slug}",
            method="POST",
        )
        return cast(dict, response.json())

    def untag_post(self, number: int, slug: str) -> dict:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.TAGS}/{slug}",
            method="DELETE",
        )
        return cast(dict, response.json())
