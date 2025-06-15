from fiderpy import Fider


# from fiderpy.v1.resources.users.request import CreateUserRequest


f = Fider(
    # api_key="GG4OCPGwIw3WnXqpsznjRXUHCLwIvtpUvh4dAZrHV5pq2dHE19YjAoyNjGJcyERB",
    host="https://demo.fider.io",
)
print("calling api")
response = f.posts.get_posts()
print("printing response")
print(response)
