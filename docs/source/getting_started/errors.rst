Errors
======

All API responses are wrapped in a :class:`fiderpy.v1.utils.domain.FiderAPIResponse` object...including errors.

.. code-block:: python

    >>> from fiderpy import Fider
    >>> fider = Fider(host="https://demo.fider.io", api_key="1234567890")
    >>> response = fider.posts.create_post(request=CreatePostRequest(title="Test Post", description="This is a test post"))
    >>> response
    FiderAPIResponse(
        message="There was an error with your request.",
        data=None,
        errors=[FiderError(message='API Key is invalid', field=None)]
    )

You can read more about errors in the `Fider API documentation <https://docs.fider.io/api/overview>`_.
