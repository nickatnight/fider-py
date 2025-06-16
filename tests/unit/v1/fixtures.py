from unittest.mock import MagicMock

import pytest

from fiderpy.v1.resources import (
    CommentsClient,
    PostsClient,
    TagsClient,
    UsersClient,
    VotesClient,
)


@pytest.fixture
def mock_posts_client() -> PostsClient:
    return PostsClient(http=MagicMock())


@pytest.fixture
def mock_votes_client() -> VotesClient:
    return VotesClient(http=MagicMock())


@pytest.fixture
def mock_users_client() -> UsersClient:
    return UsersClient(http=MagicMock())


@pytest.fixture
def mock_comments_client() -> CommentsClient:
    return CommentsClient(http=MagicMock())


@pytest.fixture
def mock_tags_client() -> TagsClient:
    return TagsClient(http=MagicMock())
