from requests import Response


class BaseFiderError(Exception):
    """Base class for exceptions in this module."""

    pass


class FiderRequestError(BaseFiderError):
    def __init__(self, message: str, response: Response) -> None:
        self.message = message

        super().__init__(message)

        self.response = response
