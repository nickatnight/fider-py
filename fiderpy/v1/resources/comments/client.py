from typing import cast

from fiderpy.v1.utils.enums import FiderApiUrls
from fiderpy.v1.utils.interfaces import IHttp
from fiderpy.v1.utils.types import FiderAPIResponseType, RequestExtra


class CommentsClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def get_comments(self, number: int) -> list[FiderAPIResponseType]:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.COMMENTS}"
        )
        return cast(list[FiderAPIResponseType], response.json())

    def get_comment(self, number: int, id: int) -> FiderAPIResponseType:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.COMMENTS}/{id}"
        )
        return cast(FiderAPIResponseType, response.json())

    def create_comment(
        self, number: int, request: RequestExtra
    ) -> FiderAPIResponseType:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.COMMENTS}",
            method="POST",
            **request,
        )
        return cast(FiderAPIResponseType, response.json())

    def edit_comment(self, number: int, id: int, request: RequestExtra) -> dict:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.COMMENTS}/{id}",
            method="PUT",
            **request,
        )
        return cast(dict, response.json())

    def delete_comment(self, number: int, id: int) -> dict:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.COMMENTS}/{id}",
            method="DELETE",
        )
        return cast(dict, response.json())
