import functools
from typing import Any, Callable, Optional, TypeVar, Union, cast

from fiderpy.v1.utils.adapters import FiderErrorAdapter
from fiderpy.v1.utils.domain import FiderAPIResponse, FiderError
from fiderpy.v1.utils.exceptions import FiderRequestError
from fiderpy.v1.utils.interfaces import IAdapter
from fiderpy.v1.utils.types import FiderAPIResponseType


F = TypeVar("F", bound=Callable[..., Any])
T = TypeVar("T")
A = TypeVar("A", bound=Union[FiderAPIResponseType, list[FiderAPIResponseType]])


def as_fider(
    success: Optional[type[IAdapter[A, T]]] = None,
) -> Callable[[F], F]:
    """
    Decorator to adapt a Fider API response to a consistent response domain object.

    :param success:             Success response adapter
    :return:                    Response domain object
    """

    def decorator_as_fider(func: F) -> F:
        @functools.wraps(func)
        def wrapper_as_fider(*args: Any, **kwargs: Any) -> FiderAPIResponse[T]:
            # Inject user_id into request dict if both are present in order to impersonate the user
            user_id = kwargs.get("user_id")
            request = kwargs.get("request")
            message = "Successfully fetched data!"
            data: Optional[T] = None
            errors: Optional[list[FiderError]] = None

            if user_id is not None and isinstance(request, dict):
                request["headers"].update(**{"X-Fider-UserID": user_id})

            try:
                response_json = func(*args, **kwargs)
            except FiderRequestError as request_err:
                if (
                    request_err.response.status_code >= 500
                    or request_err.response.status_code == 401
                ):
                    errors = [FiderError(message=str(request_err))]
                else:
                    errors = FiderErrorAdapter.to_domain(
                        obj=request_err.response.json()
                    )
            except Exception as err:
                errors = [FiderError(message=f"Unexpected error: {err}")]
            else:
                data = cast(T, response_json)

                if success:
                    data = success.to_domain(obj=response_json)

            return FiderAPIResponse(message=message, data=data, errors=errors)

        return cast(F, wrapper_as_fider)

    return decorator_as_fider
