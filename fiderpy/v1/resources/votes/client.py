from typing import cast

from fiderpy.v1.utils.enums import FiderApiUrls
from fiderpy.v1.utils.interfaces import IHttp
from fiderpy.v1.utils.types import FiderAPIResponseType


class VotesClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def get_votes(self, number: int) -> list[FiderAPIResponseType]:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.VOTES}"
        )

        return cast(list[FiderAPIResponseType], response.json())

    def delete_vote(self, number: int) -> dict:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.VOTES}", method="DELETE"
        )

        return cast(dict, response.json())

    def create_vote(self, number: int) -> dict:
        response = self.http.send(
            path=f"{FiderApiUrls.POSTS}/{number}{FiderApiUrls.VOTES}", method="POST"
        )

        return cast(dict, response.json())
