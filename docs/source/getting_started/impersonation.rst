Impersonation
=============

The Fider API supports impersonation of users. This is useful when you need to perform actions on behalf of another user. The API key used must have "Administrator" role.

.. code-block:: python

    >>> from fiderpy import Fider
    >>> fider = Fider(host="https://demo.fider.io", api_key="1234567890")
    >>> fider.posts.create_post(request=CreatePostRequest(title="Test Post", description="This is a test post"), user_id="5")
