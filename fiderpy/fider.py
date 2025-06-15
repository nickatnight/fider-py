from typing import Optional

from fiderpy.v1 import resources
from fiderpy.v1.utils.http import RequestsClient


__version__ = "0.0.1"


class Fider:
    """API Client for Fider

    :param api_key:         The API key for Fider. See here https://docs.fider.io/api/authentication
    """

    def __init__(
        self, host: str, api_key: Optional[str] = None, api_version: str = "v1"
    ) -> None:
        headers = {"User-Agent": f"fiderpy/v{__version__}"}

        if api_key:
            headers["Authorization"] = f"Bearer {api_key}"

        self._http = RequestsClient(
            base_url=f"{host}/api/{api_version}",
            headers=headers,
        )

    @property
    def posts(self) -> resources.PostsService:
        client = resources.PostsClient(http=self._http)

        return resources.PostsService(client=client)

    @property
    def users(self) -> resources.UsersService:
        client = resources.UsersClient(http=self._http)

        return resources.UsersService(client=client)

    @property
    def votes(self) -> resources.VotesService:
        client = resources.VotesClient(http=self._http)

        return resources.VotesService(client=client)

    @property
    def comments(self) -> resources.CommentsService:
        client = resources.CommentsClient(http=self._http)

        return resources.CommentsService(client=client)
