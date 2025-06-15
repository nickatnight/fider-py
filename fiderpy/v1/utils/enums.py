class SimpleEnum:
    @classmethod
    def all(cls) -> list[str]:
        return [v for k, v in cls.__dict__.items() if not k.startswith("__")]


class FiderApiUrls:
    POSTS = "/posts"
    COMMENTS = "/comments"
    VOTES = "/votes"
    USERS = "/users"
    TAGS = "/tags"
