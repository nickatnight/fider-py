from fiderpy import Fider
from fiderpy.v1.resources.posts.request import GetPostsRequest


def test_fider_client() -> None:
    f = Fider(host="https://demo.fider.io", api_key="")
    print(f.posts.get_posts(request=GetPostsRequest()))
    raise
