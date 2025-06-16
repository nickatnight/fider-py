# fider-py
<p align="center">
    <a href="https://github.com/nickatnight/fider-py/actions">
        <img alt="GitHub Actions status" src="https://github.com/nickatnight/fider-py/actions/workflows/main.yml/badge.svg">
    </a>
    <a href="https://codecov.io/gh/nickatnight/fider-py">
        <img alt="Coverage" src="https://codecov.io/gh/nickatnight/fider-py/branch/main/graph/badge.svg?token=HgBDCeK3pF"/>
    </a>
    <a href="https://pypi.org/project/fider-py/">
        <img alt="PyPi Shield" src="https://img.shields.io/pypi/v/fider-py">
    </a>
    <a href="https://www.python.org/downloads/">
        <img alt="Python Versions Shield" src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white">
    </a>
    <a href="https://fider-py.readthedocs.io/en/latest/"><img alt="Read The Docs Badge" src="https://img.shields.io/readthedocs/fider-py"></a>
    <a href="https://github.com/nickatnight/fider-py/blob/master/LICENSE">
        <img alt="License Shield" src="https://img.shields.io/github/license/nickatnight/fider-py">
    </a>
</p>

## Features
- 🗣️ **Fider** [api routes](https://docs.fider.io/api/overview), including current beta
- ♻️ **Retry Strategy** Sensible defaults to reliably retry/back-off fetching data from coingecko
- ✏️ **Code Formatting** Fully typed with [mypy](https://mypy-lang.org/) and code formatters [black](https://github.com/psf/black) / [isort](https://pycqa.github.io/isort/)
- ⚒️ **Modern tooling** using [uv](https://docs.astral.sh/uv/), [ruff](https://docs.astral.sh/ruff/), and [pre-commit](https://pre-commit.com/)
- 📥 **GitHub Actions** CI/CD to automate [everything](.github/workflows/main.yml)
- ↩️ **Code Coverage** Fully tested using tools like [Codecov](https://about.codecov.io/)
- 🐍 **Python Support** All minor [versions](https://www.python.org/downloads/) from 3.10 are supported

## Installation
```sh
$ pip install fider-py
```

## Usage

```python
>>> from fiderpy import Fider

# unauthenticated client
>>> client = Fider(host="https://demo.fider.io")

# all API responses are wrapped in a FiderAPIResponse instance
>>> client.posts.get_posts()  # default limit is 30
FiderAPIResponse(
    message="Successfully fetched data!",
    data=[
        Post(
            id=1,
            number=1,
            title="Test Post",
            slug="test-post",
            description="This is a test post",
            created_at="2021-01-01T00:00:00Z",
            user=User(
                id=1,
                name="John Doe",
                role="admin"
            ),
            has_voted=False,
            votes_count=0,
            comments_count=0,
            status="open",
            response=None,
            tags=["test"]
        ),
    ],
    errors=None
)
```

## Documentation
See full documentation with examples [here](https://fider-py.readthedocs.io/en/latest/).
