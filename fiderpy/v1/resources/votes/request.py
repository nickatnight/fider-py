from dataclasses import dataclass


@dataclass
class DeleteVoteRequest:

    number: int


@dataclass
class CreateVoteRequest:

    number: int


@dataclass
class GetVotesRequest:
    number: int
