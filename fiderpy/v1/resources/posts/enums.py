from fiderpy.v1.utils.enums import SimpleEnum


class PostsViewEnum(SimpleEnum):
    """Posts view filter options

    https://docs.fider.io/api/posts#list-posts
    """

    ALL = "all"
    RECENT = "recent"
    MY_VOTES = "my-votes"
    MOST_WANTED = "most-wanted"
    MOST_DISCUSSED = "most-discussed"
    PLANNED = "planned"
    STARTED = "started"
    COMPLETED = "completed"
    DECLINED = "declined"
    TRENDING = "trending"
