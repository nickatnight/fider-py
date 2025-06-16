import logging
from typing import Optional

from fiderpy.v1 import resources
from fiderpy.v1.utils.http import RequestsClient


__version__ = "0.0.1"
logger = logging.getLogger(__name__)


class Fider:
    """API Client for Fider

    :param host:            Base URL of the Fider instance (no trailing slash)
    :param api_key:         API key for Fider. See here https://docs.fider.io/api/authentication
    """

    def __init__(
        self, host: str, api_key: Optional[str] = None, api_version: str = "v1"
    ) -> None:
        if host.endswith("/"):
            logger.warning(
                "Host URL should not end with a slash...removing it. Will raise error in future releases."
            )
            host = host[:-1]

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

    @property
    def tags(self) -> resources.TagsService:
        client = resources.TagsClient(http=self._http)

        return resources.TagsService(client=client)
