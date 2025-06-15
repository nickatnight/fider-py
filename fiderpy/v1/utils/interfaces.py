import abc
from typing import Any, Generic, TypeVar


T = TypeVar("T")
A = TypeVar("A")


class IHttp(Generic[T], abc.ABC):
    """Interface for http requests libs"""

    @abc.abstractmethod
    def send(self, path: str, method: str = "get", **extra: Any) -> T:
        raise NotImplementedError


class IAdapter(Generic[A, T], abc.ABC):
    """Adapter interface

    :param A:                           API response object
    :param T:                           transport object
    """

    @staticmethod
    @abc.abstractmethod
    def to_domain(obj: A) -> T:
        """Converts an API response object to transport object

        :param obj:                     API response dict
        :return:                        transport object
        """
        raise NotImplementedError
