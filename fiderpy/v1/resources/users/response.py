from dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str
    role: str
    status: str


@dataclass
class CreateUserResponse:
    id: int
