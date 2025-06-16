import logging
from typing import Optional

from fiderpy.v1 import resources
from fiderpy.v1.utils.http import RequestsClient


__version__ = "0.0.4"
logger = logging.getLogger(__name__)


class Fider:
    """API Client for Fider

    Example:

    .. code-block:: python

        >>> from fiderpy import Fider

        # Initialize the client
        >>> fider = Fider(host="https://demo.fider.io", api_key="1234567890")

        # Get all posts
        >>> fider.posts.get_posts()

        # Get a single post
        >>> fider.posts.get_post(request=GetPostRequest(number=1))

        # Get all users
        >>> fider.users.get_users()

        # Create a new user
        >>> fider.users.create_user(request=CreateUserRequest(name="John Doe", email="john@example.com", reference="1234567890"))

        # Create a new post
        >>> fider.posts.create_post(request=CreatePostRequest(title="Test Post", description="This is a test post"))

        # Delete a post
        >>> fider.posts.delete_post(request=DeletePostRequest(number=1))

        # Get all votes
        >>> fider.votes.get_votes(request=GetVotesRequest(number=1))

        # Create a vote
        >>> fider.votes.create_vote(request=CreateVoteRequest(number=1))

        # Delete a vote
        >>> fider.votes.delete_vote(request=DeleteVoteRequest(number=1))

        # Get all comments
        >>> fider.comments.get_comments(request=GetCommentsRequest(number=1))

        # Get a single comment
        >>> fider.comments.get_comment(request=GetCommentRequest(number=1, id=1))

        # Create a comment
        >>> fider.comments.create_comment(request=CreateCommentRequest(number=1, content="This is a test comment"))

        # Edit a comment
        >>> fider.comments.edit_comment(request=EditCommentRequest(number=1, id=1, content="This is a test comment"))

        # Delete a comment
        >>> fider.comments.delete_comment(request=DeleteCommentRequest(number=1, id=1))

        # Get all tags
        >>> fider.tags.get_tags()

        # Create a tag
        >>> fider.tags.create_tag(request=CreateTagRequest(name="Test Tag", color="#FF0000", is_public=True))

        # Edit a tag
        >>> fider.tags.edit_tag(request=EditTagRequest(slug="test-tag", name="Test Tag", color="#FF0000", is_public=True))

        # Delete a tag
        >>> fider.tags.delete_tag(request=DeleteTagRequest(slug="test-tag"))


    :param host:            Base URL of the Fider instance (no trailing slash)
    :param api_key:         API key for Fider. See here https://docs.fider.io/api/authentication
    :param api_version:     API version to use. Defaults to "v1"
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
