from typing import Any, cast

from fiderpy.v1.utils.enums import FiderApiUrls
from fiderpy.v1.utils.interfaces import IHttp
from fiderpy.v1.utils.types import RequestExtra


class UsersClient:
    def __init__(self, http: IHttp) -> None:
        self.http = http

    def get_users(self) -> list[dict[str, Any]]:
        response = self.http.send(path=FiderApiUrls.USERS)
        return cast(list[dict[str, Any]], response.json())

    def create_user(self, request: RequestExtra) -> dict:
        response = self.http.send(
            path=f"{FiderApiUrls.USERS}", method="POST", **request
        )
        return cast(dict, response.json())
